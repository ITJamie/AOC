import pathlib
import sys
import json


def parse(puzzle_input):
    """Parse input."""
    return puzzle_input.split()


def part1(puzzle_input):
    """Solve part 1."""
    print(json.dumps(puzzle_input))
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
        print(calculated_num)
    print(f"total: {sum(output)}")

def part2(puzzle_input):
    print("do stuff")


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        file1 = open(path, "r")
        lines = file1.read().splitlines()

        print(part1(lines))
