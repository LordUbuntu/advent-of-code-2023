# Day 1, Jacobus Burger (2023)


def solution(filename, test=False):
    total = 0
    for string in open(filename, "r").readlines():
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
    print("test run: ", solution("test1.txt", True))
    print("true run: ", solution("part1.txt"))
