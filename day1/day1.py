# Jacobus Burger (2023)
# Day 1


# Solution to Part 1
def part1(filename, test=False):
    total = 0
    for string in open(filename, "r").readlines():
        if test:
            print(f"str: {string}")
        number = ["", ""]
        for index in range(0, len(string)):
            # add first digit to number, then just add most recent digit to second place on number. Thus only needing one pass
            if string[index].isdigit():
                if number[0] == "":
                    number[0] = string[index]
                else:
                    number[1] = string[index]
            if test:
                print(f"i: {index}, ch: {string[index]}, num: {number}")
        if number[1] == "":
            number[1] = number[0]
        total += int("".join(number))
        if test:
            print("total:", total)
    return total


# Part 2
# TODO: simple find and replace won't work. Use a sliding window to match for the first word greedily (iterate over from longest word to the shortest starting with left pointer at 0 and going until left pointer is > length / 2. Then do the same in reverse from the right) and then replace THAT!
map = {
    "one": "1",
    "two": "2",
    "six": "6",
    "four": "4",
    "five": "5",
    "nine": "9",
    "three": "3",
    "seven": "7",
    "eight": "8",
}
def part2(filename, test=False):
    total = 0
    for string in open(filename, "r").readlines():
        # replace first occurence of word with number
        if test:
            print("k->v subst:")
        for key, value in map.items():
            if test:
                print(string)
            if string.find(key) != -1:
                string = string.replace(key, value, 1)
                break
        # replace last occurence of word with number (sdrawkcab)
        for key, value in map.items():
            if test:
                print(string)
            if string[::-1].find(key[::-1]) != -1:
                string = string[::-1].replace(key[::-1], value[::-1], 1)
                string = string[::-1]
                break
        # then continue with normal part1 solution
        if test:
            print(string)
            print("index | character")
        number = ""
        for l in range(0, len(string)):
            if test:
                print(l, string[l])
            if string[l].isdigit():
                number += string[l]
                break
        for r in range(len(string) - 1, -1, -1):
            if test:
                print(r, string[r])
            if string[r].isdigit():
                number += string[r]
                break
        if test:
            print("num:", number)
        total += int(number)
        if test:
            print("total:", total)
    return total


if __name__ == '__main__':
    # Part 1
    print("test run: ", part1("input/test1.txt", True))
    print("true run: ", part1("input/part1.txt"))
    # Part 2
    print("test run: ", part2("input/test2.txt", True))
    print("true run: ", part2("input/part2.txt"))
