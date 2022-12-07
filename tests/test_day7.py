import pytest
from solutions.day7 import day7_a, day7_b


@pytest.mark.parametrize("filename", ("day7_sample.txt",))
def test_day7_a_sample(aoc_input_strip):
    actual = day7_a(data=aoc_input_strip)
    assert actual == 95437


@pytest.mark.parametrize("filename", ("day7.txt",))
def test_day7_a(aoc_input_strip):
    actual = day7_a(data=aoc_input_strip)
    assert actual == 1648397


@pytest.mark.parametrize("filename", ("day7_sample.txt",))
def test_day7_b_sample(aoc_input_strip):
    actual = day7_b(data=aoc_input_strip)
    assert actual == 24933642


@pytest.mark.parametrize("filename", ("day7.txt",))
def test_day7_b(aoc_input_strip):
    actual = day7_b(data=aoc_input_strip)
    assert actual == 1815525
