from solutions.day2 import day2_a, day2_b
import pytest


@pytest.mark.parametrize("filename", ("day2_sample.txt",))
def test_day2_a_sample(aoc_input):
    actual = day2_a(data=aoc_input)
    assert actual == 15


@pytest.mark.parametrize("filename", ("day2.txt",))
def test_day2_a(aoc_input):
    actual = day2_a(data=aoc_input)
    assert actual == 13009


@pytest.mark.parametrize("filename", ("day2_sample.txt",))
def test_day2_b_sample(aoc_input):
    actual = day2_b(data=aoc_input)
    assert actual == 12


@pytest.mark.parametrize("filename", ("day2.txt",))
def test_day2_b(aoc_input):
    actual = day2_b(data=aoc_input)
    assert actual == 10398
