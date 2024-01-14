# Jacobus Burger (2023)
# Advent of Code Day 3

def part1(filename):
    def bound(n, low, high): return max(low, min(high, n))
    total = 0
    schematic = [line.strip() for line in open(filename).readlines()]
    number = []  # contruct numbers from a queue of digits
    # scan pointer across grid
    for row in range(len(schematic)):
        for col in range(len(schematic[0])):
            char = schematic[row][col]
            if char.isdigit():
                number.append(char)
                print("digit: {}, number: {}".format(char, number))
            else:
                print(''.join(number))
                number = []
    return total
