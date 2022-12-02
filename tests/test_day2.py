from solutions.day2 import day2_a
import pytest


@pytest.mark.skip
@pytest.mark.parametrize("filename", ("day2_sample.txt",))
def test_day2_a(aoc_input):
    actual = day2_a(data=aoc_input)
    assert actual == 15
