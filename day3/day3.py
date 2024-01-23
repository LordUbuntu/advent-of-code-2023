# Jacobus Burger (2023)
# Advent of Code Day 3


def part1(filename):
    total = 0
    schematic = [line.strip() for line in open(filename).readlines()]
    number = []  # contruct numbers from a queue of digits
    part_number = False
    # scan pointer across grid
    for row in range(len(schematic)):
        for col in range(len(schematic[0])):
            char = schematic[row][col]
            # terminate and add part number at end of numeric string
            if not char.isdigit():
                # add number to total if it's a part number
                if part_number:
                    total += int(''.join(number))
                # reset digits for next number
                number = []
                part_number = False
            # remember digits of number in order
            if char.isdigit():
                number.append(char)
            # check for adjacent part symbols around current number
            if len(number) > 0:
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        y, x = row + i, col + j
                        if y < 0 or y >= len(schematic):
                            continue
                        if x < 0 or x >= len(schematic[0]):
                            continue
                        if schematic[y][x] != '.' and not schematic[y][x].isdigit():
                            part_number = True
    return total


def part2(filename):
    total = 0
    schematic = [line.strip() for line in open(filename).readlines()]
    number = []  # contruct numbers from a queue of digits
    # same as part1 but this time only paying attention to *
    # when a * is encountered adjacent to a number, look for another adjacent number that isn't part of the same number, then find the start of both numbers, get their numeric value, and add their values together
    for row in range(len(schematic)):
        for col in range(len(schematic[0])):
            char = schematic[row][col]
            if char == '*':
                print("* at {},{}".format(col, row))
                # adjacency check
                ratio = 0
                # TODO: DFS, returning y and least x of each number
    return total


# where G is the schematic, and v is the starting coordinate symbol
def dfs(G, v):
    from itertools import product
    # start DFS for all digits around the given position
    visited, stack = [], [v]  # (y,x) for v
    while stack:
        for i, j in product(range(v[0] - 1, v[0] + 2), range(v[1] - 1, v[1] + 2)):
            if i < 0 or i > len(G):
                continue
            if j < 0 or j > len(G[0]):
                continue
        break











