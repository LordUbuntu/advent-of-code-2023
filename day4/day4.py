# Jacobus Burger (2024)
# Advent of Code Day 4 (2023)


# Part 1
def part1(filename):
    # The solution to part 1 is simple. We need to count how many
    #   elements from the left are members of the right, then raise
    #   2 to the power of that count to get the number of points.
    # In python this is a simple matter of set intersection after
    #   processing the input.
    total = 0
    cards = [line.strip() for line in open(filename).readlines()]
    for card in cards:
        # get sets of numbers from boths sides of '|'
        A, B = card.split('|')
        A = {int(a) for a in A.split() if a.isdigit()}
        B = {int(b) for b in B.split() if b.isdigit()}
        winners = len(A.intersection(B))
        if winners:
            total += 2**(len(A.intersection(B)) - 1)
    return total


# Part 2
def part2(filename):
# This is the same as part 1 except we count the number of matches of each card and compound that with the cards that come after
    cards = [line.strip() for line in open(filename).readlines()]
    count = [1] * len(cards)
    for i in range(len(count) - 1):  # exclude last card winners
        # get number of matches for current card
        card = cards[i]
        A, B = card.split('|')
        A = {int(a) for a in A.split() if a.isdigit()}
        B = {int(b) for b in B.split() if b.isdigit()}
        score = len(A.intersection(B))
        # add extra cards after based on the given rule
        for _ in range(count[i]):
            for j in range(i + 1, min(len(count), i + score + 1)):
                count[j] += 1
    return sum(count) # return total
