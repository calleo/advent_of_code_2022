from typing import List, Tuple, Dict


def is_adjacent(head, tail):
    adjacent = [
        {"x": head["x"] - 1, "y": head["y"] + 1},
        {"x": head["x"], "y": head["y"] + 1},
        {"x": head["x"] + 1, "y": head["y"] + 1},
        {"x": head["x"] - 1, "y": head["y"]},
        {"x": head["x"] + 1, "y": head["y"]},
        {"x": head["x"] - 1, "y": head["y"] - 1},
        {"x": head["x"], "y": head["y"] - 1},
        {"x": head["x"] + 1, "y": head["y"] - 1},
        {"x": head["x"], "y": head["y"]},
    ]
    return tail in adjacent


def move_tail(head, tail) -> dict[str, int]:
    if not is_adjacent(head, tail):
        if tail["x"] == head["x"]:
            if head["y"] > tail["y"]:
                tail["y"] += 1
            else:
                tail["y"] -= 1
        elif tail["y"] == head["y"]:
            if head["x"] > tail["x"]:
                tail["x"] += 1
            else:
                tail["x"] -= 1
        else:
            if head["x"] > tail["x"]:
                tail["x"] += 1
            else:
                tail["x"] -= 1
            if head["y"] > tail["y"]:
                tail["y"] += 1
            else:
                tail["y"] -= 1
    return tail


def day9(data: List[str], tails: int) -> Tuple[Dict[str, int], Dict[str, int], int]:
    seen = {}
    moves = [(move.split(" ")[0], int(move.split(" ")[1])) for move in data]
    head = {"x": 0, "y": 0}
    tails = [{"x": 0, "y": 0} for _ in range(tails)]

    for move in moves:
        for step in range(0, move[1]):
            if move[0] == "U":
                head["y"] += 1
            elif move[0] == "D":
                head["y"] -= 1
            elif move[0] == "L":
                head["x"] -= 1
            elif move[0] == "R":
                head["x"] += 1

            _next_head = {**head}
            for index, tail in enumerate(tails):
                tail = move_tail(_next_head, tail)
                _next_head = {**tail}
                if index == len(tails) - 1:
                    seen[f"{tail['x']}|{tail['y']}"] = 1

            # draw(head, tails)

    return head, tails[0], sum(seen.values())


def draw(head, tails):
    board = [["."] * 6 for _ in range(6)]
    board[5 - head["y"]][head["x"]] = "H"

    print("")
    print("")
    for index, tail in enumerate(tails):
        board[5 - tail["y"]][tail["x"]] = f"{index+1}"

    for row in board:
        line = "".join([f"[{col}]" for col in row])
        print(line)


if __name__ == "__main__":
    with open("../tests/inputs/day9_sample.txt") as input_file:
        lines = [row.strip() for row in input_file.readlines()]
        day9(data=lines, tails=10)
