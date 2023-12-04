import pathlib
import sys
import json
import re


def parse(puzzle_input):
    """Parse input."""
    return puzzle_input.split()


written_nums = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

digitnames = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def translate(v: str) -> str:
    return v if v.isdigit() else str(digitnames.index(v) + 1)


def part1(puzzle_input):
    """Solve part 1."""
    # print(json.dumps(puzzle_input))
    output = []
    for line in puzzle_input:
        first_num = None
        last_num = None
        for character in line:
            if character.isdigit():
                if not first_num:
                    first_num = character
                last_num = character
        calculated_num = f"{first_num}{last_num}"
        output.append(int(calculated_num))
        # print(calculated_num)
    print(f"Part 1: {sum(output)}")


def part2(puzzle_input):
    output = []

    for line in puzzle_input:
        first_num = None
        last_num = None

        nums = re.findall(r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))", line)
        result = int(translate(nums[0]) + translate(nums[-1]))
        output.append(result)
    print(f"Part 2: {sum(output)}")


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        file1 = open(path, "r")
        lines = file1.read().splitlines()

        part1(lines)
        part2(lines)
