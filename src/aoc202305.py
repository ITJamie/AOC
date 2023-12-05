import pathlib
import sys
import json
import re


def parse(puzzle_input):
    """Parse input."""
    return puzzle_input.split()


def part1(puzzle_input):
    """Solve part 1."""

    print(f"Part 1: ")


def part2(puzzle_input):
    """Solve part 2."""

    print(f"Part 2: ")


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        file1 = open(path, "r")
        lines = file1.read().splitlines()

        part1(lines)
        part2(lines)
