from more_itertools import grouper
from typing import List


def priority(item: str):
    return ord(item) - 38 if item.isupper() else ord(item) - 96


def to_rucksack(row: str) -> List[int]:
    return [priority(item=char) for char in row]


def day3_a(data):
    value = 0
    for row in data:
        row = to_rucksack(row)
        comp1, comp2 = row[: int(len(row) / 2)], row[int(len(row) / 2) :]
        value += sum(set(comp1).intersection(set(comp2)))
    return value


def day3_b(data):
    value = 0
    for group in grouper(data, 3):
        badge = (
            set(to_rucksack(group[0]))
            .intersection(set(to_rucksack(group[1])))
            .intersection(set(to_rucksack(group[2])))
        )
        value += sum(badge)

    return value
