from solutions.day1 import day1_a, day1_b
import pytest


@pytest.mark.parametrize("filename", ("day1_sample.txt",))
def test_day1_a_sample(aoc_input):
    actual = day1_a(data=aoc_input)
    assert actual == 24000


@pytest.mark.parametrize("filename", ("day1.txt",))
def test_day1_a(aoc_input):
    actual = day1_a(data=aoc_input)
    assert actual == 64929


@pytest.mark.parametrize("filename", ("day1_sample.txt",))
def test_day1_b_sample(aoc_input):
    actual = day1_b(data=aoc_input)
    assert actual == 45000


@pytest.mark.parametrize("filename", ("day1.txt",))
def test_day1_b(aoc_input):
    actual = day1_b(data=aoc_input)
    assert actual == 193697
