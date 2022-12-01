from collections import defaultdict


def _get_elves_calories(data):
    elves = defaultdict(lambda: 0)
    elves_count = 0
    for line in data:
        if len(line) == 0:
            elves_count += 1
        else:
            elves[elves_count] += int(line)
    return elves


def day1_a(data):
    elves = _get_elves_calories(data=data)
    return max(elves.values())


def day1_b(data):
    elves = _get_elves_calories(data=data)
    elves = sorted(elves.values())
    elves.reverse()
    return sum(elves[:3])
