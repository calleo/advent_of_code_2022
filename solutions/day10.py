from typing import List
from collections import deque


def day10_a(data: List[str], cycles: int, x: int = 1) -> int:
    cycles_consumed = 0

    for line_no, instruction in enumerate(data):
        if instruction.startswith("addx"):
            cycles_consumed += 2
            if cycles_consumed < cycles:
                x += int(instruction.split(" ")[1])
            else:
                break
        else:
            cycles_consumed += 1
            if cycles_consumed >= cycles:
                break
    return x


def day10_b(data: List[str], width=40, height=6, sprite_width=3) -> List[str]:
    sprite = deque((["#"] * sprite_width) + (["."] * (width - sprite_width)))
    crt = [["."] * width for _ in range(height)]
    cycle = 0

    for instruction in data:
        cycles = 1 if instruction.startswith("noop") else 2
        shift_by = (
            int(instruction.split(" ")[1]) if instruction.startswith("addx") else 0
        )

        for _ in range(cycles):
            row = int(cycle / width)
            col = cycle - (row * width)
            if sprite[col] == "#":
                crt[row][col] = "#"
            cycle += 1

        sprite.rotate(shift_by)

    return ["".join(row) for row in crt]
