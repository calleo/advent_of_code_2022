from typing import List, Dict, Tuple


def get_rocks(data: List[str]) -> Dict[Tuple[int, int],int]:
    rock = {}
    for line in data:
        line = [
            tuple([int(coo) for coo in point.strip().split(",")])
            for point in line.split("->")
        ]
        prev = None
        for point in line:
            if prev is None:
                rock[point] = 1
            else:
                if point[0] == prev[0]:
                    for i in range(min(point[1], prev[1]), max(point[1], prev[1]) + 1):
                        rock[(point[0], i)] = 1
                elif point[1] == prev[1]:
                    for i in range(min(point[0], prev[0]), max(point[0], prev[0]) + 1):
                        rock[(i, point[1])] = 1
            prev = point
    return rock


def day14_a(data: List[str], infinity:bool) -> int:
    rock = get_rocks(data=data)
    sand = {}
    last_rock = max([point[1] for point in list(rock.keys())])
    floor = max([point[1] for point in list(rock.keys())]) + 2

    while True:
        moving_sand = (500, 0)
        while True:
            next = (moving_sand[0], moving_sand[1] + 1)

            if next[1] > last_rock and infinity:
                # falling into infinity!
                return len(sand.keys())

            if next[1] == floor:
                # hit the floor, nothing else to do
                sand[moving_sand] = 1
                break

            if next in rock or next in sand:
                left = (next[0] - 1, next[1])
                right = (next[0] + 1, next[1])
                if left not in sand and left not in rock:
                    moving_sand = left
                elif right not in sand and right not in rock:
                    moving_sand = right
                else:
                    sand[moving_sand] = 1
                    #draw(rock=rock, sand=sand, floor=floor)
                    if next == (500, 1):
                        return len(sand.keys())
                    break
            else:
                moving_sand = next
        #draw(rock=rock, sand=sand, floor=floor)

def draw(rock, sand, floor):
    width = max([k[0] for k in rock.keys()] + [k[0] for k in sand.keys()])+2
    board = [["."]*width for _ in range(0, floor+2)]

    for y in range(0, len(board)):
        for x in range(0, width):
            if y == floor:
                board[y][x] = "#"
            elif (x, y) in rock:
                board[y][x] = "#"
            elif (x, y) in sand:
                board[y][x] = "o"
            else:
                board[y][x] = "."

    print(f"Units of sand: {len(sand.keys())}")
    for row in board:
        print(f"{''.join(row[470:])}")
