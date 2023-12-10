# Jacobus Burger (2023)
# Advent of Code Day 3

def part1(filename):
    total = 0
    schematic = [line.strip() for line in open(filename).readlines()]
    queue = []  # remember digits in order
    width, height = len(schematic[0]), len(schematic)
    part = False
