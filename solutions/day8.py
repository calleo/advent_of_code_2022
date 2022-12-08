from typing import List


def grid_enum(grid):
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            yield x, y, grid[y][x]


def is_visible(grid: List[List[int]], x: int, y: int) -> bool:
    if x == 0 or x == (len(grid[0]) - 1):
        return True

    if y == 0 or y == (len(grid) - 1):
        return True

    point_value = grid[y][x]
    left = right = top = bottom = True
    for iter_x, iter_y, value in grid_enum(grid=grid):
        if iter_y == y and iter_x > x and value >= point_value:
            right = False
        if iter_y == y and iter_x < x and value >= point_value:
            left = False
        if iter_y > y and iter_x == x and value >= point_value:
            top = False
        if iter_y < y and iter_x == x and value >= point_value:
            bottom = False

    return any([left, right, top, bottom])


def day8_a(data: List[str]) -> int:
    grid = [[int(nr) for nr in row] for row in data]
    visible_count = 0

    for x, y, value in grid_enum(grid=grid):
        if is_visible(grid, x, y):
            visible_count += 1

    return visible_count


def get_adjacent(grid, x, y):
    left = list(reversed(grid[y][:x]))
    top = [grid[_y][x] for _y in reversed(range(0, y))]
    right = grid[y][x + 1 :]
    bottom = [grid[_y][x] for _y in range(y + 1, len(grid))]
    return left, top, right, bottom


def get_visible_count(points):
    count = 0

    if len(points) == 0:
        return 0

    view = points[1:]
    start = points[0]

    for point in view:
        count += 1
        if point >= start:
            break

    return count


def day8_b(data: List[str]) -> int:
    grid = [[int(nr) for nr in row] for row in data]
    visible = 0

    for x, y, value in grid_enum(grid=grid):
        left, top, right, bottom = get_adjacent(grid=grid, x=x, y=y)
        _visible = (
            get_visible_count(points=[value] + left)
            * get_visible_count(points=[value] + top)
            * get_visible_count(points=[value] + right)
            * get_visible_count(points=[value] + bottom)
        )
        visible = _visible if _visible > visible else visible

    return visible
