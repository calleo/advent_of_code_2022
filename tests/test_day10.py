import pytest
from solutions.day10 import day10_a, day10_b


@pytest.mark.parametrize("filename", ("day10_sample.txt",))
def test_day10_a_sample(aoc_input_strip):
    sum = 0
    for cycles, expected in [
        (20, 420),
        (60, 1140),
        (100, 1800),
        (140, 2940),
        (180, 2880),
        (220, 3960),
    ]:
        x = day10_a(data=aoc_input_strip, cycles=cycles) * cycles
        sum += x
        assert x == expected
    assert sum == 13140


@pytest.mark.parametrize(
    "instructions,cycles,expected",
    [(["noop"], 1, 1), (["addx 3"], 2, 4), (["noop", "addx 3"], 2, 1)],
)
def test_day9_a_small(instructions, cycles, expected):
    actual = day10_a(data=instructions, cycles=cycles)
    assert actual == expected


@pytest.mark.parametrize("filename", ("day10_sample.txt",))
def test_day10_a_sample_foo(aoc_input_strip):
    actual = day10_a(data=aoc_input_strip, cycles=220)
    assert actual == 18


@pytest.mark.parametrize("filename", ("day10.txt",))
def test_day10_a(aoc_input_strip):
    sum = 0
    for cycles in [
        20,
        60,
        100,
        140,
        180,
        220,
    ]:
        x = day10_a(data=aoc_input_strip, cycles=cycles) * cycles
        sum += x
    assert sum == 13680


@pytest.mark.parametrize("filename", ("day10_sample.txt",))
def test_day10_b_sample(aoc_input_strip):
    expected = [
        "##..##..##..##..##..##..##..##..##..##..",
        "###...###...###...###...###...###...###.",
        "####....####....####....####....####....",
        "#####.....#####.....#####.....#####.....",
        "######......######......######......####",
        "#######.......#######.......#######.....",
    ]
    actual_image = day10_b(data=aoc_input_strip)
    assert actual_image == expected


@pytest.mark.parametrize("filename", ("day10.txt",))
def test_day10_b(aoc_input_strip):
    # This image contains: PZGPKPEB
    expected = [
        "###..####..##..###..#..#.###..####.#####",
        "#..#....#.#..#.#..#.#.#..#..#.#....#..##",
        "#..#...#..#....#..#.##...#..#.###..###..",
        "###...#...#.##.###..#.#..###..#....#..#.",
        "#....#....#..#.#....#.#..#....#....#..##",
        "#....####..###.#....#..#.#....####.###..",
    ]
    actual_image = day10_b(data=aoc_input_strip)
    assert actual_image == expected
