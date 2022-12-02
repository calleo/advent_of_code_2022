MOVES = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
BEAT_BY = {1: 2, 2: 3, 3: 1}
BEATS = {1: 3, 2: 1, 3: 2}


def _score(them, you) -> int:
    if them == you:
        return 3 + you
    elif BEAT_BY[them] == you:
        return 6 + you
    else:
        return you


def day2_a(data):
    score = 0
    for row in data:
        them, you = [MOVES[move] for move in row.split(" ")]
        score += _score(them, you)

    return score


def day2_b(data):
    score = 0
    for row in data:
        them, result = row.split(" ")
        them = MOVES[them]

        if result == "X":
            you = BEATS[them]
        elif result == "Y":
            you = them
        else:
            you = BEAT_BY[them]

        score += _score(them, you)

    return score
