# Jacobus Burger (2023)
# Advent of Code Day 3

def part1(filename):
    def bound(n, low, high): return max(low, min(high, n))
    total = 0
    schematic = [line.strip() for line in open(filename).readlines()]
    # scan pointer across grid
    for row in range(len(schematic)):
        for col in range(len(schematic[0])):
            pass
            # if a digit
            # if not
    return total
