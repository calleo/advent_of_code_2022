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
