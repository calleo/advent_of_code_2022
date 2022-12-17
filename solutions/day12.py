from typing import List, Tuple, Optional
from dataclasses import dataclass
from collections import defaultdict

START = 83
END = 69
MAX_STEPS_ALLOWED = 1000


@dataclass
class Path:
    path: List[Tuple[int, int]]
    failed: bool
    complete: bool


def day12_a(data: List[str]) -> int:
    board = get_board(data=data)
    start, end = None, None

    for y, row in enumerate(board):
        if START in row:
            start = (row.index(START), y)
        if END in row:
            end = (row.index(END), y)

    return solve(board=board, start=start, end=end)


def day12_b(data: List[str]) -> int:
    board = get_board(data=data)
    starts = []
    end = None, None

    for y, row in enumerate(board):
        if y == 0 or y == len(board) - 1:
            for x, col in enumerate(row):
                if col in [START, ord("a")]:
                    starts.append((x, y))
        else:
            if row[0] in [START, ord("a")]:
                starts.append((0, y))
            if row[-1] in [START, ord("a")]:
                starts.append((len(row) - 1, y))

        if END in row:
            end = (row.index(END), y)

    solutions = [solve(board=board, start=start, end=end) for start in starts]

    return min(filter(None, solutions))


def solve(
    board: List[List[int]], start: Tuple[int, int], end: Tuple[int, int]
) -> Optional[int]:
    start = Path(path=[start], failed=False, complete=False)
    incomplete = [start]
    complete = []
    best_sub_paths = defaultdict(lambda: MAX_STEPS_ALLOWED)

    while len(incomplete) > 0:
        new_paths = []

        for path in incomplete:
            accessible = get_accessible_paths(board=board, path=path)

            for step in accessible:
                new_path = Path(path=path.path + [step], failed=False, complete=False)

                # if step has been reached in fewer steps, fail it
                if len(new_path.path) >= best_sub_paths[step]:
                    new_path.failed = True
                else:
                    best_sub_paths[step] = len(new_path.path)

                if step == end:
                    new_path.complete = True
                    complete.append(new_path)
                elif not new_path.failed:
                    new_paths.append(new_path)

            if len(accessible) == 0:
                path.failed = True

        incomplete = new_paths

    if len(complete) == 0:
        return None

    return sorted([len(path.path) - 1 for path in complete if path.complete])[0]


def get_accessible_paths(board, path: Path) -> List[Tuple[int, int]]:
    current = path.path[-1]
    current_altitude = get_altitude(board=board, step=current)

    steps = [
        (current[0] - 1, current[1]),
        (current[0] + 1, current[1]),
        (current[0], current[1] - 1),
        (current[0], current[1] + 1),
    ]

    return [
        step
        for step in steps
        if len(board[0]) > step[0] >= 0
        and len(board) > step[1] >= 0
        and step not in path.path
        and get_altitude(board=board, step=step) <= (current_altitude + 1)
        and get_altitude(board=board, step=step) != START
    ]


def get_altitude(board, step: Tuple[int, int]) -> chr:
    alt = board[step[1]][step[0]]
    if alt == START:
        return ord("a")
    elif alt == END:
        return ord("z")
    else:
        return alt


def get_board(data: List[str]) -> List[List[int]]:
    return [[ord(col) for col in list(row)] for row in data]
