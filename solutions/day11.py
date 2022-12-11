from typing import List, Callable, Dict, Any
import yaml
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Monkey:
    items: List[int]
    operation: Callable
    divisor: int
    recipients: Dict[bool, int]
    worrying_divisor: int
    inspections: int = 0

    def debug(self, msg: str):
        print(f"{datetime.now().isoformat()[:19]} Debug: {msg}")

    def throw(self, monkeys: List[Any]):
        while len(self.items) > 0:
            item = self.items.pop()

            self.debug("Operation Start")
            new_item = self.operation(old=item)
            self.debug("Operation End")

            if self.worrying_divisor != 1:
                new_item = int(new_item / self.worrying_divisor)

            # self.debug("Divisor Start")
            recipient = self.recipients[new_item % self.divisor == 0]
            self.debug("Divisor End")

            # self.debug("Receive Start")
            monkeys[recipient].receive(new_item)
            # self.debug("Receive End")

            self.inspections += 1

    def receive(self, item: int):
        self.items.insert(0, item)


class MonkeyBusiness:
    def __init__(self, monkeys: List[Monkey]):
        self.monkeys = monkeys

    def play(self, rounds: int):
        for round in range(rounds):
            for monkey in self.monkeys:
                monkey.throw(monkeys=self.monkeys)
            if round % 10 == 0:
                print(f"Completed round: {round}")


def create_operation(operation, value):
    def _operation(old):
        if value == "old":
            _value = old
        else:
            _value = int(value)
        if operation == "*":
            # This take a very long time!!
            print(f"Multiplying")
            return old * _value
        elif operation == "+":
            print(f"Adding")
            return old + _value
        else:
            raise Exception(f"Unknown operation {operation}")

    return _operation


def parse_config(data: List[str], worrying_divisor: int) -> List[Monkey]:
    data = [row.replace("  If ", "If ") for row in data]
    config = yaml.safe_load("\n".join(data))
    monkeys = []

    for monkey, values in config.items():
        if isinstance(values["Starting items"], str):
            items = [int(item) for item in values["Starting items"].split(",")]
            items.reverse()
        else:
            items = [values["Starting items"]]

        op_parts = values["Operation"].split(" ")
        operation = create_operation(
            operation=op_parts[3].strip(), value=op_parts[4].strip()
        )
        divisor = int(values["Test"].removeprefix("divisible by"))
        recipients = {
            True: int(values["If true"].removeprefix("throw to monkey")),
            False: int(values["If false"].removeprefix("throw to monkey")),
        }
        monkeys.append(
            Monkey(
                items=items,
                operation=operation,
                divisor=divisor,
                recipients=recipients,
                worrying_divisor=worrying_divisor,
            )
        )

    return monkeys


def calc_monkey_business(data: List[str], rounds: int, worrying_divisor: int) -> int:
    monkeys = parse_config(data=data, worrying_divisor=worrying_divisor)
    game = MonkeyBusiness(monkeys=monkeys)
    game.play(rounds=rounds)

    inspections = [monkey.inspections for monkey in monkeys]
    inspections.sort()
    inspections.reverse()

    return inspections[0] * inspections[1]


def day11_a(data: List[str]):
    return calc_monkey_business(data=data, rounds=20, worrying_divisor=3)


def day11_b(data: List[str]):
    return calc_monkey_business(data=data, rounds=10_000, worrying_divisor=1)


if __name__ == "__main__":
    with open("tests/inputs/day11_sample.txt") as file:
        actual = day11_b(data=file.readlines())
