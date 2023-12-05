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
dictionary = {
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
        if test:
            print(f"str: {string}\n\n")
        # scroll index across string
        number = ["", ""]
        for index in range(0, len(string)):
            # add char to number if it is a digit
            if string[index].isdigit():
                if test:
                    print(f"adding digit {string[index]}")
                if number[0] == "":
                    number[0] = string[index]
                else:
                    number[1] = string[index]
            # otherwise check if it's a recognized word
            else:
                if test:
                    print("checking against dictionary")
                # iterate over dictionary
                for word, digit in dictionary.items():
                    # check all characters match in both strings
                    if test:
                        print(f"word: {word}")
                    is_number = True
                    for i in range(0, len(word)):
                        if i + index >= len(string):
                            is_number = False
                            break
                        if test:
                            print(f"i: {i}, index: {index}\n str: {string[i + index]}, word: {word[i]}")
                        if string[i + index] != word[i]:
                            is_number = False
                            break
                    # if all characters match
                    if is_number:
                        # add digit
                        if test:
                            print(f"adding digit: {digit}")
                        if number[0] == "":
                            number[0] = digit
                        else:
                            number[1] = digit
                        break
            if test:
                print(f"i: {index}, ch: {string[index]}, num: {number}")
        if number[1] == "":
            number[1] = number[0]
        total += int("".join(number))
        if test:
            print("total:", total)
    return total


if __name__ == '__main__':
    # Part 1
    print("test run: ", part1("input/test1.txt"))
    print("true run: ", part1("input/part1.txt"))
    # Part 2
    print("test run: ", part2("input/test2.txt"))
    print("true run: ", part2("input/part2.txt"))
