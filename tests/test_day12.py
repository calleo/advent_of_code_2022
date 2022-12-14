from solutions.day12 import day12_a, day12_b
import pytest


@pytest.mark.parametrize("filename", ("day12_sample.txt",))
def test_day11_a_sample(aoc_input_strip):
    actual = day12_a(data=aoc_input_strip)
    assert actual == 31


@pytest.mark.parametrize("filename", ("day12.txt",))
def test_day11_a(aoc_input_strip):
    actual = day12_a(data=aoc_input_strip)
    assert actual == 408


@pytest.mark.parametrize("filename", ("day12_sample.txt",))
def test_day11_b_sample(aoc_input_strip):
    actual = day12_b(data=aoc_input_strip)
    assert actual == 29


@pytest.mark.parametrize("filename", ("day12.txt",))
def test_day11_b(aoc_input_strip):
    actual = day12_b(data=aoc_input_strip)
    assert actual == 399
