import pathlib
import sys
import json
import re


def parse(puzzle_input):
    """Parse input."""
    return puzzle_input.split()


def part1(puzzle_input):
    """Solve part 1."""
    games = {}

    # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    for line in puzzle_input:
        gameid = line.split("Game ")[1].split(":")[0]
        hands = line.split(":")[1].split(";")
        print(gameid)
        print(hands)
        games[gameid] = {}
        # games[gameid]['hands'] = []
        games[gameid]["max_seen"] = {}
        games[gameid]["max_seen"]["red"] = 0
        games[gameid]["max_seen"]["green"] = 0
        games[gameid]["max_seen"]["blue"] = 0
        for hand in hands:
            for cube in hand.split(","):
                cube = cube.strip()
                print(cube)
                cube_count = int(cube.split(" ")[0])
                cube_colour = cube.split(" ")[1]
                if cube_count > games[gameid]["max_seen"][cube_colour]:
                    games[gameid]["max_seen"][cube_colour] = cube_count
            print("")
        print(games[gameid])

    overall_max = {}
    overall_max["red"] = 12
    overall_max["green"] = 13
    overall_max["blue"] = 14

    good_game_ids = []

    for gameid in games:
        good_game = True
        for overallmax_colour in overall_max:
            if games[gameid]["max_seen"][overallmax_colour] > overall_max[overallmax_colour]:
                good_game = False
        if good_game:
            good_game_ids.append(int(gameid))

    print(good_game_ids)
    print(sum(good_game_ids))


def part2(puzzle_input):
    output = []


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        file1 = open(path, "r")
        lines = file1.read().splitlines()

        part1(lines)
        part2(lines)
