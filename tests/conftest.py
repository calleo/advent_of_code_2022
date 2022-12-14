import pytest
import os


@pytest.fixture
def aoc_input(filename: str):
    cwd = os.getcwd()

    # Support for test execution in IDEs that
    # uses the test/ folder as working directory
    if cwd.endswith("/tests"):
        path = f"inputs/{filename}"
    else:
        path = f"tests/inputs/{filename}"

    with open(path) as input_file:
        yield [row for row in input_file.readlines()]


@pytest.fixture
def aoc_input_strip(aoc_input):
    yield [row.strip() for row in aoc_input]
