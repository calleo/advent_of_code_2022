from solutions.day13 import day13_a, day13_b
import pytest


@pytest.mark.parametrize("filename", ("day13_sample.txt",))
def test_day11_a_sample(aoc_input_strip):
    actual = day13_a(data=aoc_input_strip)
    assert actual == 13


@pytest.mark.parametrize("filename", ("day13.txt",))
def test_day11_a(aoc_input_strip):
    actual = day13_a(data=aoc_input_strip)
    assert actual == 6428


@pytest.mark.parametrize("filename", ("day13_sample.txt",))
def test_day11_b(aoc_input_strip):
    expected = [
        [],
        [[]],
        [[[]]],
        [1, 1, 3, 1, 1],
        [1, 1, 5, 1, 1],
        [[1], [2, 3, 4]],
        [1, [2, [3, [4, [5, 6, 0]]]], 8, 9],
        [1, [2, [3, [4, [5, 6, 7]]]], 8, 9],
        [[1], 4],
        [[2]],
        [3],
        [[4, 4], 4, 4],
        [[4, 4], 4, 4, 4],
        [[6]],
        [7, 7, 7],
        [7, 7, 7, 7],
        [[8, 7, 6]],
        [9],
    ]
    actual, answer = day13_b(data=aoc_input_strip)
    assert actual == expected
    assert answer == 140


@pytest.mark.parametrize("filename", ("day13.txt",))
def test_day11_b(aoc_input_strip):
    actual, answer = day13_b(data=aoc_input_strip)
    assert answer == 22464
