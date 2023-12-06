# Jacobus Burger (2023)


# Part 1
def part1(filename):
    total = 0
    for game in open(filename, "r").readlines():
        id = int(game.split()[1].strip(':'))  # get game ID number
        rgb = [0, 0, 0]
        # parse totals
        for i in range(len(game)):
            if game[i].isdigit():
                count = int(game[i])
                color = game[i + 2]
                if color == 'r':
                    rgb[0] += count
                if color == 'g':
                    rgb[1] += count
                if color == 'b':
                    rgb[2] += count
        # if game is not possible, continue to next game
        if rgb[0] <= 12 and rgb[1] <= 13 and rgb[2] <= 14:
            total += id
        # print(game, rgb, id, total)
    return total


if __name__ == "__main__":
    print(part1("input/test1.txt"))
    print(part1("input/part1.txt"))
