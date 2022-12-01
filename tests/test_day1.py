from solutions.day1 import day1_a, day1_b
import pytest


@pytest.fixture
def input_day1_sample():
    with open("tests/inputs/day1_a_sample.txt") as input_file:
        yield [row.strip() for row in input_file.readlines()]


@pytest.fixture
def input_day1():
    with open("tests/inputs/day1_a.txt") as input_file:
        yield [row.strip() for row in input_file.readlines()]


def test_day1_a_sample(input_day1_sample):
    actual = day1_a(data=input_day1_sample)
    assert actual == 24000


def test_day1_a(input_day1):
    actual = day1_a(data=input_day1)
    assert actual == 64929


def test_day1_b_sample(input_day1_sample):
    actual = day1_b(data=input_day1_sample)
    assert actual == 45000


def test_day1_b(input_day1):
    actual = day1_b(data=input_day1)
    assert actual == 193697
