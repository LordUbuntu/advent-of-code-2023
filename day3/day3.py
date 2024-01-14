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
                    print("{} is a part number".format(''.join(number)))
                # reset digits for next number
                number = []
                part_number = False
            # remember digits of number in order
            if char.isdigit():
                number.append(char)
                print("digit: {}, number: {}".format(char, number))
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
                            print("pos {},{} and centre {},{} for symbol {}".format(i, j, row, col, schematic[y][x]))
                            part_number = True
    return total
