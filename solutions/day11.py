from typing import List, Callable, Dict, Any
import yaml
from dataclasses import dataclass
from functools import reduce


@dataclass
class Monkey:
    name: str
    items: List[int]
    operation: Callable
    divisor: int
    recipients: Dict[bool, int]
    worrying_divisor: int
    inspections: int = 0

    def throw(self, monkeys: List[Any]):
        while len(self.items) > 0:
            item = self.items.pop()
            new_item = self.operation(old=item)

            # Ugly!
            if self.worrying_divisor == 3:
                new_item = int(new_item / self.worrying_divisor)
            else:
                new_item = new_item % self.worrying_divisor

            remainder = new_item % self.divisor

            recipient = self.recipients[remainder == 0]
            rec_monkey = monkeys[recipient]
            rec_monkey.receive(item)
            self.inspections += 1

    def receive(self, item: int):
        self.items.insert(0, item)


class MonkeyBusiness:
    def __init__(self, monkeys: List[Monkey]):
        self.monkeys = monkeys

    def play(self, rounds: int):
        for _ in range(rounds):
            for index, monkey in enumerate(self.monkeys):
                monkey.throw(monkeys=self.monkeys)


def create_operation(operation, value) -> Callable:
    # Ugly!
    def _operation(old: int) -> int:
        if value == "old":
            return int(old) * int(old)
        else:
            _value = int(value)
            if operation == "*":
                return int(value) * _value
            elif operation == "+":
                return int(value) + _value

    return _operation


def parse_config(data: List[str], worrying_divisor: int = None) -> List[Monkey]:
    data = [row.replace("  If ", "If ") for row in data]
    config = yaml.safe_load("\n".join(data))
    monkeys = []

    for monkey, values in config.items():
        if isinstance(values["Starting items"], str):
            items = [int(item) for item in values["Starting items"].split(",")]
            items.reverse()
        else:
            items = [int(values["Starting items"])]

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
                name=monkey,
                items=items,
                operation=operation,
                divisor=divisor,
                recipients=recipients,
                worrying_divisor=worrying_divisor,
            )
        )

    if worrying_divisor is None:
        super_divisor = reduce(lambda x, y: x * y, [m.divisor for m in monkeys])

        for monkey in monkeys:
            monkey.worrying_divisor = super_divisor

    return monkeys


def calc_monkey_business(
    data: List[str], rounds: int, worrying_divisor: int = None
) -> int:
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
    return calc_monkey_business(data=data, rounds=10_000)
