import pytest
from solutions.day6 import day6


@pytest.mark.parametrize("stream,expected", [
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
    ("nppdvjthqldpwncqszvftbrmjlhg", 6),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11)
])
def test_day6_a_sample(stream, expected):
    actual = day6(data=stream)
    assert actual == expected


@pytest.mark.parametrize("filename", ("day6.txt",))
def test_day6_a(aoc_input):
    actual = day6(data=aoc_input[0])
    assert actual == 1566


@pytest.mark.parametrize("stream,expected", [
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
    ("nppdvjthqldpwncqszvftbrmjlhg", 23),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26)
])
def test_day6_b_sample(stream, expected):
    actual = day6(data=stream, window_size=14)
    assert actual == expected


@pytest.mark.parametrize("filename", ("day6.txt",))
def test_day6_b(aoc_input):
    actual = day6(data=aoc_input[0], window_size=14)
    assert actual == 2265
