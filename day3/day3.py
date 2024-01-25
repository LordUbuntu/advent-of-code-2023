# Jacobus Burger (2023)
# Advent of Code Day 3
from itertools import product
from functools import reduce
from operator import mul


# consider rewriting part1 to take advantage of dfs from part2
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
    for row in range(len(schematic)):
        for col in range(len(schematic[0])):
            char = schematic[row][col]
            if char == '*':
                # get coordinates of digits around '*'
                # REMEMBER: (y,x) not (x,y)
                numbers = nums(schematic, (row, col))
                # skip if there isn't a pair of numbers
                if len(numbers) != 2:
                    continue
                # sort coordinates of each digit in each number by ascending x
                numbers = [
                    sorted(number, key=lambda coordinate: coordinate[1])
                    for number in numbers
                ]
                # convert coordinates of numbers into digit characters
                numbers = [
                    ''.join(
                        schematic[digit[0]][digit[1]]
                        for digit in number
                    )
                    for number in numbers
                ]
                # convert number strings to int values
                numbers = [int(number) for number in numbers]
                # add ratio to total
                total += reduce(mul, numbers)
    return total


# this will return a list of lists of digits representing adjacent numbers to a given symbol
def nums(G: list, vi: tuple) -> list:
    known = []  # avoid duplication of coords
    numbers = []
    # go through each starting point around the centre
    for i, j in product(range(vi[0] - 1, vi[0] + 2), range(vi[1] - 1, vi[1] + 2)):
        # only dive on "islands" of digits
        if not G[i][j].isdigit():
            continue
        # skip digits that are already known
        if (i, j) in known:
            continue
        # perform dfs along x of number to get its digits
        y = i
        visited, passed, stack = [], [], [(i, j)]
        while stack:
            v = stack.pop()
            visited.append(v)
            known.append(v)
            # scan adjacent tiles along x
            for x in range(v[1] - 1, v[1] + 2):
                if (y, x) in passed:
                    continue
                if (y, x) in known:
                    continue
                if x < 0 or x >= len(G[0]):
                    passed.append((y, x))
                    continue
                if G[y][x].isdigit():
                    if (y, x) not in visited:
                        stack.append((y, x))
                else:
                    passed.append((y, x))
        # visited is now a list of digits (a number)
        # if visited is not empty, add it to the list of numbers
        if visited:
            numbers.append(visited)
    # return the list of numbers
    return numbers
