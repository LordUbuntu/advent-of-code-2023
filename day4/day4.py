# Jacobus Burger (2023)
# Advent of Code - Day 4


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
