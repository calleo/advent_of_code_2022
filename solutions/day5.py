from textwrap import wrap
from collections import defaultdict


def get_stacks(data):
    stacks = defaultdict(lambda: [])
    for row in data:
        if "[" not in row:
            break
        for index, value in enumerate(wrap(row, 4, drop_whitespace=False)):
            value = value.strip().replace("[", "").replace("]", "")
            if len(value) > 0:
                stacks[index + 1].insert(0, value)
    return stacks


def get_moves(data):
    import re

    parse = False
    moves = []
    for line in data:
        if len(line.strip()) == 0:
            parse = True
            continue
        if parse:
            res = re.search(".+( [0-9]+ ).+( [0-9]+ ).+( [0-9]+).*", line)
            groups = res.groups()
            moves.append(
                (int(groups[0].strip()), int(groups[1].strip()), int(groups[2].strip()))
            )
    return moves


def stack_to_s(stacks) -> str:
    return "".join(
        [stacks[stack_index + 1].pop() for stack_index in range(len(stacks))]
    )


def day5_a(data) -> str:
    stacks = get_stacks(data=data)
    moves = get_moves(data=data)

    for move in moves:
        for _ in range(move[0]):
            stacks[move[2]].append(stacks[move[1]].pop())

    return stack_to_s(stacks=stacks)


def day5_b(data) -> str:
    stacks = get_stacks(data=data)
    moves = get_moves(data=data)

    for move in moves:
        lift = []
        for _ in range(move[0]):
            lift.insert(0, stacks[move[1]].pop())
        stacks[move[2]].extend(lift)

    return stack_to_s(stacks=stacks)
