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


def day9_a(data: List[str]) -> Tuple[Dict[str, int], Dict[str, int], int]:
    #seen_head = {}
    seen = {}
    moves = [(move.split(" ")[0], int(move.split(" ")[1])) for move in data]
    head = {"x": 0, "y": 0}
    tail = {"x": 0, "y": 0}
    #count = 0

    for move in moves:
        for step in range(0, move[1]):
            #count += 1
            #if count in (14,):
            #    pass
            if move[0] == "U":
                head["y"] += 1
            elif move[0] == "D":
                head["y"] -= 1
            elif move[0] == "L":
                head["x"] -= 1
            elif move[0] == "R":
                head["x"] += 1
            #else:
            #    raise Exception("DFDFD")

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
                    #print(f"Doing diagonal move: {count}")
                    if head["x"] > tail["x"]:
                        tail["x"] += 1
                    else:
                        tail["x"] -= 1
                    if head["y"] > tail["y"]:
                        tail["y"] += 1
                    else:
                        tail["y"] -= 1

            seen[f"{tail['x']}{tail['y']}"] = 1
            #seen_head[f"{head['x']}{head['y']}"] = 1

            #assert is_adjacent(head, tail)

    return head, tail, sum(seen.values())
