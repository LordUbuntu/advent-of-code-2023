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
    # when a * is encountered adjacent to a number, find the start of the other number also adjacent to it, get the numeric string of both, and add their values together
    # scan pointer across grid
    for row in range(len(schematic)):
        for col in range(len(schematic[0])):
            char = schematic[row][col]
            # if a gear symbol
            if char == '*':
                print("* at {},{}".format(col, row))
                # check for adjacent numbers
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        y, x = row + i, col + j
                        if y < 0 or y >= len(schematic):
                            continue
                        if x < 0 or x >= len(schematic[0]):
                            continue
                        if schematic[y][x].isdigit():
                            print("{} at {},{}".format(schematic[y][x], y, x))
                            # find the start of both numbers and get their values
                            # first number
                            num_y, num_x = y, x
                            while num_x > 0 and schematic[num_y][num_x].isdigit():
                                if schematic[num_y][num_x - 1].isdigit():
                                    num_x -= 1
                                else:
                                    break
                            print("start of num is {},{}".format(num_y, num_x))
                            queue = []
                            while schematic[num_y][num_x].isdigit():
                                queue.append(schematic[num_y][num_x])
                                num_x += 1
                            print("number is {}".format(''.join(queue)))
                                # once the start is found, collect digits in queue in order from left to right
                                # then join those digits into a string
                                # then turn into an int
                            # get their product
                            # add to total
    return total
