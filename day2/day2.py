# Jacobus Burger (2023)


# Part 1
# The hardest part is reading the input lol
def part1(filename):
    total = 0
    for game in open(filename, "r").readlines():
        id = int(game.split()[1].strip(':'))  # game ID number
        counts = game.split()[2:]  # number of each color
        counts = [count.strip(" ,;:") for count in counts]  # sanitize
        rgb = [0, 0, 0]
        # parse totals
        for i in range(0, len(counts) - 1, 2):
            count, color = counts[i : i + 2]
            if color == "red":
                rgb[0] += int(count)
            if color == "green":
                rgb[1] += int(count)
            if color == "blue":
                rgb[2] += int(count)
        # if game is not possible, continue to next game
        if rgb[0] <= 12 and rgb[1] <= 13 and rgb[2] <= 14:
            total += id
        # print(game, id, counts, rgb, total)
    return total


if __name__ == "__main__":
    print(part1("input/test1.txt"))
    # print(part1("input/part1.txt"))
