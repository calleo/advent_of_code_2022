import pytest
from solutions.day11 import day11_a, day11_b


@pytest.mark.skip
@pytest.mark.parametrize("filename", ("day11_sample.txt",))
def test_day11_a_sample(aoc_input):
    actual = day11_a(data=aoc_input)
    assert actual == 10_605


@pytest.mark.skip
@pytest.mark.parametrize("filename", ("day11.txt",))
def test_day11_a(aoc_input):
    actual = day11_a(data=aoc_input)
    assert actual == 58_322


@pytest.mark.skip
@pytest.mark.parametrize("filename", ("day11_sample.txt",))
def test_day11_b_sample(aoc_input):
    actual = day11_b(data=aoc_input)
    assert actual == 2_713_310_158


@pytest.mark.skip
@pytest.mark.parametrize("filename", ("day11.txt",))
def test_day11_b_sample(aoc_input):
    actual = day11_b(data=aoc_input)
    assert actual == 13_937_702_909
