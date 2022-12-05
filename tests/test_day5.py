import pytest
from solutions.day5 import day5_a, get_stacks, get_moves, day5_b


@pytest.mark.parametrize("filename", ("day5_sample.txt",))
def test_day5_a_sample(aoc_input):
    actual = day5_a(data=aoc_input)
    assert actual == "CMZ"


@pytest.mark.parametrize("filename", ("day5.txt",))
def test_day5_a(aoc_input):
    actual = day5_a(data=aoc_input)
    assert actual == "VPCDMSLWJ"


@pytest.mark.parametrize("filename", ("day5_sample.txt",))
def test_day5_b_sample(aoc_input):
    actual = day5_b(data=aoc_input)
    assert actual == "MCD"


@pytest.mark.parametrize("filename", ("day5.txt",))
def test_day5_b_sample(aoc_input):
    actual = day5_b(data=aoc_input)
    assert actual == "TPWCGNCCG"


@pytest.mark.parametrize("filename", ("day5_sample.txt",))
def test_get_stacks(aoc_input):
    actual = get_stacks(data=aoc_input)
    assert actual == {1: ["Z", "N"], 2: ["M", "C", "D"], 3: ["P"]}


@pytest.mark.parametrize("filename", ("day5_sample.txt",))
def test_get_moves(aoc_input):
    actual = get_moves(data=aoc_input)
    assert actual == [(1, 2, 1), (3, 1, 3), (2, 2, 1), (1, 1, 2)]
