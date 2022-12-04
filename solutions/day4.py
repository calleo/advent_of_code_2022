from typing import List


def range_to_set(nr_range: str) -> List[int]:
    left, right = nr_range.split("-")
    return [*range(int(left), int(right) + 1, 1)]


def day4_a(data) -> int:
    overlapping_pairs = 0
    for row in data:
        left, right = [set(range_to_set(nr_range=part)) for part in row.split(",")]
        intersection = left.intersection(right)
        if intersection == left or intersection == right:
            overlapping_pairs += 1
    return overlapping_pairs


def day4_b(data) -> int:
    overlapping_pairs = 0
    for row in data:
        left, right = [set(range_to_set(nr_range=part)) for part in row.split(",")]
        intersection = left.intersection(right)
        if len(intersection) > 0:
            overlapping_pairs += 1
    return overlapping_pairs
