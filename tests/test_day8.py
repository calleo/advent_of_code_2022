import pytest
from solutions.day8 import day8_a, is_visible, day8_b, get_visible_count, get_adjacent

GRID_1 = [[1, 1, 1], [1, 2, 1], [1, 1, 1]]

GRID_2 = [[1, 2, 1], [2, 2, 2], [1, 2, 1]]


@pytest.mark.parametrize(
    "grid,x,y,expected",
    [
        (GRID_2, 1, 1, False),
        (GRID_1, 0, 0, True),
        (GRID_1, 2, 2, True),
        (GRID_2, 1, 1, False),
    ],
)
def test_is_visible(grid, x: int, y: int, expected: bool):
    actual = is_visible(grid=grid, x=x, y=y)
    assert actual is expected


@pytest.mark.parametrize(
    "points,expected",
    [
        ([1, 2, 2, 3], 1),
        ([1, 1, 2, 3], 1),
        ([5, 2, 4, 2], 3),
        ([5, 2, 4, 5], 3),
        ([], 0),
        ([1], 0),
        ([5, 3, 5, 3], 2),
        ([5, 4, 9], 2),
    ],
)
def test_get_visible_count(points, expected: int):
    actual = get_visible_count(points=points)
    assert actual == expected


def test_get_adjacent():
    grid = [
        [3, 0, 3, 7, 3],
        [2, 5, 5, 1, 2],
        [6, 5, 3, 3, 2],
        [3, 3, 5, 4, 9],
        [3, 5, 3, 9, 0],
    ]
    left, top, right, bottom = get_adjacent(grid=grid, x=2, y=3)
    assert left == [3, 3]
    assert top == [3, 5, 3]
    assert right == [4, 9]
    assert bottom == [3]


@pytest.mark.parametrize("filename", ("day8_sample.txt",))
def test_day8_a_sample(aoc_input_strip):
    actual = day8_a(data=aoc_input_strip)
    assert actual == 21


@pytest.mark.parametrize("filename", ("day8.txt",))
def test_day8_a(aoc_input_strip):
    actual = day8_a(data=aoc_input_strip)
    assert actual == 1703


@pytest.mark.parametrize("filename", ("day8_sample.txt",))
def test_day8_b_sample(aoc_input_strip):
    actual = day8_b(data=aoc_input_strip)
    assert actual == 8


@pytest.mark.parametrize("filename", ("day8.txt",))
def test_day8_b(aoc_input_strip):
    actual = day8_b(data=aoc_input_strip)
    assert actual == 496650
