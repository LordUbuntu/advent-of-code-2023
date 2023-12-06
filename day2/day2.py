# Jacobus Burger (2023)


# Part 1
# The hardest part is reading the input lol
def part1(filename):
    total = 0
    for game in open(filename, "r").readlines():
        # parse game
        id = int(game.split()[1].strip(':'))  # game ID number
        counts = game.split()[2:]  # number of each color
        counts = [count.strip(" ,;:") for count in counts]  # sanitize

        # check for any impossible games
        possible = True
        for i in range(0, len(counts) - 1, 2):
            count, color = counts[i : i + 2]
            if color == "red" and int(count) > 12:
                possible = False
                break
            if color == "green" and int(count) > 13:
                possible = False
                break
            if color == "blue" and int(count) > 14:
                possible = False
                break

        # tally possible games
        if possible:
            total += id
        # print(id, total)
    return total


if __name__ == "__main__":
    print(part1("input/test1.txt"))
    print(part1("input/part1.txt"))
