import pytest
from solutions.day9 import day9_a, is_adjacent


@pytest.mark.parametrize("filename", ("day9_sample.txt",))
def test_day9_a_sample(aoc_input_strip):
    head, tail, actual = day9_a(data=aoc_input_strip)
    assert head == {"x": 2, "y": 2}
    assert tail == {"x": 1, "y": 2}
    assert actual == 13


@pytest.mark.parametrize("filename", ("day9.txt",))
def test_day9_a(aoc_input_strip):
    head, tail, actual = day9_a(data=aoc_input_strip)
    assert actual == 5858


@pytest.mark.parametrize(
    "moves,end_pos,tail_seen",
    [
        (["R 3", "U 2"], ({"x": 3, "y": 2}, {"x": 3, "y": 1}), 4),
        (["R 3", "U 2", "L 2"], ({"x": 1, "y": 2}, {"x": 2, "y": 2}), 5),
        (["R 1", "L 2"], ({"x": -1, "y": 0}, {"x": 0, "y": 0}), 1),
        (["U 2", "L 1", "D 1"], ({"x": -1, "y": 1}, {"x": 0, "y": 1}), 2),
        (["U 2", "L 0", "D 0"], ({"x": 0, "y": 2}, {"x": 0, "y": 1}), 2),
        (["D 2", "L 2", "D 1", "R 2"], ({"x": 0, "y": -3}, {"x": -1, "y": -2}), 3),
        (["U 2", "L 2"], ({"x": -2, "y": 2}, {"x": -1, "y": 2}), 3),
        (["U 2", "R 2"], ({"x": 2, "y": 2}, {"x": 1, "y": 2}), 3),
        (["D 2", "L 2"], ({"x": -2, "y": -2}, {"x": -1, "y": -2}), 3),
        (["D 2", "R 2"], ({"x": 2, "y": -2}, {"x": 1, "y": -2}), 3),
        (["U 1", "R 2"], ({"x": 2, "y": 1}, {"x": 1, "y": 1}), 2),
        (["U 1", "L 2"], ({"x": -2, "y": 1}, {"x": -1, "y": 1}), 2),
        (["D 1", "R 2"], ({"x": 2, "y": -1}, {"x": 1, "y": -1}), 2),
        (["D 1", "L 2"], ({"x": -2, "y": -1}, {"x": -1, "y": -1}), 2),
        (["R 1", "U 13", "R 10", "D 12"], ({"x": 11, "y": 1}, {"x": 11, "y": 2}), 33),
    ],
)
def test_day9_a_small(moves, end_pos, tail_seen):
    head, tail, seen = day9_a(data=moves)
    assert (
        head,
        tail,
    ) == end_pos
    assert seen == tail_seen


@pytest.mark.parametrize(
    "head,tail,expected",
    [
        ({"x": 0, "y": 0}, {"x": 0, "y": 0}, True),
        ({"x": 0, "y": 0}, {"x": 1, "y": 0}, True),
        ({"x": 0, "y": 0}, {"x": -1, "y": 0}, True),
        ({"x": 0, "y": 0}, {"x": 0, "y": 1}, True),
        ({"x": 0, "y": 0}, {"x": 1, "y": 1}, True),
        ({"x": 0, "y": 0}, {"x": -1, "y": 1}, True),
        ({"x": 0, "y": 0}, {"x": 0, "y": -1}, True),
        ({"x": 0, "y": 0}, {"x": 1, "y": -1}, True),
        ({"x": 0, "y": 0}, {"x": -1, "y": -1}, True),
        ({"x": 0, "y": 0}, {"x": 0, "y": -2}, False),
        ({"x": 0, "y": 0}, {"x": 0, "y": 2}, False),
        ({"x": 0, "y": 0}, {"x": 2, "y": 0}, False),
        ({"x": 0, "y": 0}, {"x": -2, "y": 0}, False),
    ],
)
def test_is_adjacent(head, tail, expected):
    actual = is_adjacent(head=head, tail=tail)
    assert actual == expected
