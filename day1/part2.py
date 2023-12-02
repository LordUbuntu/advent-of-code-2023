# Jacobus Burger (2023)
# Day 1 Part 2


map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
def solution(filename, test=False):
    total = 0
    for string in open(filename, "r").readlines():
        # translate words to digits first
        for key, value in map.items():
            string = string.replace(key, value)
        # then continue with normal part1 solution
        if test:
            print("\n")
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
    print("test run: ", solution("test2.txt", True))
    print("true run: ", solution("part2.txt"))
