# Jacobus Burger (2023)
# Advent of Code Day 3
from itertools import product
from string import digits, punctuation


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
                # DFS all adjacent digits
                coords = dfs(schematic, (row, col), {*digits})
                # check there are two numbers, otherwise skip the rest
                # group coordinates of digits based on the same y value
                # sort coordinates of each number's digits by ascending x
                # reconstruct and get value of num from ordered coords
                # get their product and add to total
    return total


# where G is the schematic, and v is the starting coordinate symbol
def dfs(G: list, vi: tuple, symbols: set) -> set:
    """
    dfs(G, vi, symbols)

    Perform a depth first search on the 2D grid 'G' starting at
        the (y,x) coordinate of the initial vertex 'vi' which
        returns all coordinates which are in the set 'symbols'.
    """
    visited, passed, stack = [], [], [vi]  # (y,x) for v
    while stack:
        v = stack.pop()
        visited.append(v)
        # search adjacent digits
        for i, j in product(range(v[0] - 1, v[0] + 2), range(v[1] - 1, v[1] + 2)):
            if (i,j) in passed:
                continue
            if i < 0 or i >= len(G):
                passed.append((i,j))
                continue
            if j < 0 or j >= len(G[0]):
                passed.append((i,j))
                continue
            if G[i][j] in symbols:
                if (i, j) not in visited:
                    stack.append((i, j))
            else:
                passed.append((i,j))
            print(G[i][j], symbols, G[i][j] in symbols)
    visited.remove(vi)
    return set(visited)












