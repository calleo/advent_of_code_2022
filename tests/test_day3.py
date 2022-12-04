from solutions.day3 import day3_a, priority, day3_b
import pytest


@pytest.mark.parametrize("filename", ("day3_a_sample.txt",))
def test_day3_a_sample(aoc_input):
    actual = day3_a(data=aoc_input)
    assert actual == 157


@pytest.mark.parametrize("filename", ("day3.txt",))
def test_day3_a(aoc_input):
    actual = day3_a(data=aoc_input)
    assert actual == 8088


@pytest.mark.parametrize("item, expected", [("a", 1), ("z", 26), ("A", 27), ("Z", 52)])
def test_priority(item: str, expected):
    actual = priority(item=item)
    assert actual == expected


@pytest.mark.parametrize("filename", ("day3_b_sample.txt",))
def test_day3_b_sample(aoc_input):
    actual = day3_b(data=aoc_input)
    assert actual == 70


@pytest.mark.parametrize("filename", ("day3.txt",))
def test_day3_b(aoc_input):
    actual = day3_b(data=aoc_input)
    assert actual == 2522
