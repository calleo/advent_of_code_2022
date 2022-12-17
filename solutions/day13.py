from typing import List, Tuple
import json


def is_right(left, right) -> bool:
    for index in range(min(len(left), len(right))):
        l_item = left[index]
        r_item = right[index]

        if isinstance(l_item, int) and isinstance(r_item, list):
            l_item = [l_item]
        elif isinstance(r_item, int) and isinstance(l_item, list):
            r_item = [r_item]

        if isinstance(r_item, list) and isinstance(l_item, list):
            res = is_right(l_item, r_item)
            if res is not None:
                return res
        else:
            if l_item > r_item:
                return False
            elif r_item > l_item:
                return True

    if len(right) > len(left):
        return True
    elif len(left) > len(right):
        return False


def get_all_pairs(data: List[str]) -> List:
    pairs = []
    pair = []
    for row in data:
        if len(row) == 0:
            pairs.append(pair)
            pair = []
        else:
            pair.append(json.loads(row))

    pairs.append(pair)
    return pairs


def day13_a(data: List[str]) -> int:
    pairs = get_all_pairs(data=data)
    right_pairs = []
    for index, pair in enumerate(pairs):
        assert len(pair) == 2
        if is_right(pair[0], pair[1]):
            right_pairs.append(index + 1)

    return sum(right_pairs)


def day13_b(data: List[str]) -> Tuple[List, int]:
    sorted = []

    pairs = get_all_pairs(data=data)
    packets = [[[2]], [[6]]]
    for pair in pairs:
        packets.extend([pair[0], pair[1]])

    while len(packets) > 0:
        min = None
        for packet in packets:
            if min is None:
                min = packet
            elif is_right(packet, min):
                min = packet
        sorted.append(min)
        packets.remove(min)

    answer = (sorted.index([[2]]) + 1) * (sorted.index([[6]]) + 1)

    return sorted, answer
