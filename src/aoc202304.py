import pathlib
import sys
import json
import re


def parse(puzzle_input):
    """Parse input."""
    return puzzle_input.split()


def part1(puzzle_input):
    """Solve part 1."""

    cards = []

    # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    for line in puzzle_input:
        card_wins = 0
        cardid = line.split("Card ")[1].split(":")[0]
        winning_nums = line.split(":")[1].split("|")[0].strip().replace("  ", " ").split(" ")
        choosen_nums = line.split(":")[1].split("|")[1].strip().replace("  ", " ").split(" ")
        print(f"Winning numbers: {winning_nums}")
        for winning_num in winning_nums:
            if winning_num in choosen_nums:
                card_wins = card_wins + 1
        # print(card_wins)

        card_value = 0
        if card_wins > 0:
            card_value = 1

            i = 1
            while i < card_wins:
                card_value = card_value * 2
                i += 1

        cards.append(card_value)

    print(f"Part 1: {sum(cards)}")


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
