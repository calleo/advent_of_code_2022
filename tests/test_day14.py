from solutions.day14 import day14_a
import pytest


@pytest.mark.parametrize("filename", ("day14_sample.txt",))
def test_day14_a_sample(aoc_input_strip):
    actual = day14_a(data=aoc_input_strip, infinity=True)
    assert actual == 24


@pytest.mark.parametrize("filename", ("day14.txt",))
def test_day14_a(aoc_input_strip):
    actual = day14_a(data=aoc_input_strip, infinity=True)
    assert actual == 805


@pytest.mark.parametrize("filename", ("day14_sample.txt",))
def test_day14_b_sample(aoc_input_strip):
    actual = day14_a(data=aoc_input_strip, infinity=False)
    assert actual == 93


@pytest.mark.parametrize("filename", ("day14.txt",))
def test_day14_b_sample(aoc_input_strip):
    actual = day14_a(data=aoc_input_strip, infinity=False)
    assert actual == 25161
