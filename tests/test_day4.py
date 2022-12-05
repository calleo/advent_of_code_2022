import pytest
from typing import Set
from solutions.day4 import day4_a, day4_b, range_to_set


@pytest.mark.parametrize("filename", ("day4_sample.txt",))
def test_day4_a_sample(aoc_input_strip):
    actual = day4_a(data=aoc_input_strip)
    assert actual == 2


@pytest.mark.parametrize("filename", ("day4.txt",))
def test_day4_a_sample(aoc_input_strip):
    actual = day4_a(data=aoc_input_strip)
    assert actual == 490


@pytest.mark.parametrize("filename", ("day4_sample.txt",))
def test_day4_b_sample(aoc_input_strip):
    actual = day4_b(data=aoc_input_strip)
    assert actual == 4


@pytest.mark.parametrize("filename", ("day4.txt",))
def test_day4_b(aoc_input_strip):
    actual = day4_b(data=aoc_input_strip)
    assert actual == 921


@pytest.mark.parametrize(
    "nr_range, expected", [("1-2", [1, 2]), ("500-505", [500, 501, 502, 503, 504, 505])]
)
def test_range_to_set(nr_range: str, expected: Set[int]):
    actual = range_to_set(nr_range=nr_range)
    assert actual == expected
