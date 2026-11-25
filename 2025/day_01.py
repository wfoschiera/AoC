"""Advent of Code 2025, day 1: https://adventofcode.com/2025/day/1"""

from pathlib import Path

INPUT = Path(__file__).with_suffix(".txt")

test_data = """\
"""


def parse(data: str) -> list[str]:
    return data.splitlines()


def part_1(data: str):
    raise NotImplementedError


def part_2(data: str):
    raise NotImplementedError


if __name__ == "__main__":
    # PART 1
    # TEST
    res = part_1(test_data)
    print(res)
    # assert res == ...

    # RESULT
    # res = part_1(INPUT.read_text())
    # print(res)

    # PART 2
    # TEST
    # res = part_2(test_data)
    # print(res)
    # assert res == ...

    # RESULT
    # res = part_2(INPUT.read_text())
    # print(res)
