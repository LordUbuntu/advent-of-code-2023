# Jacobus Burger (2023)


# Part 1
# Count ID numbers of all the games which are possible (don't exceed maximum value
#   for any color at any one time)
def part1(filename):
    total = 0
    for game in open(filename, "r").readlines():
        # parse game
        id = int(game.split()[1].strip(':'))  # game ID number
        counts = game.split()[2:]  # number of each color
        counts = [count.strip(" ,;:") for count in counts]  # sanitize

        # check for any impossible games
        possible = True
        for i in range(0, len(counts) - 1, 2):
            count, color = counts[i : i + 2]
            if color == "red" and int(count) > 12:
                possible = False
                break
            if color == "green" and int(count) > 13:
                possible = False
                break
            if color == "blue" and int(count) > 14:
                possible = False
                break

        # tally possible games
        if possible:
            total += id
    return total


# Part 2
# Find the maximum occuring value for each color, then add their power to total
from functools import reduce
from operator import mul
def part2(filename):
    total = 0
    for game in open(filename, "r").readlines():
        # parse game
        id = int(game.split()[1].strip(':'))  # game ID number
        counts = game.split()[2:]  # number of each color
        counts = [count.strip(" ,;:") for count in counts]  # sanitize

        # keep track of maximum color occuring (minimum needed to be possible)
        rgb_max = {"red": 0, "green": 0, "blue": 0}
        for i in range(0, len(counts) - 1, 2):
            count, color = counts[i : i + 2]
            rgb_max[color] = max(rgb_max[color], int(count))

        # add power to total
        total += reduce(mul, rgb_max.values())
    return total


if __name__ == "__main__":
    print(part1("input/test1.txt"))
    print(part1("input/part1.txt"))
    print(part2("input/test2.txt"))
    print(part2("input/part2.txt"))
