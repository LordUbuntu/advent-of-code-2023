# Advent of Code 2023

My solutions to this year's Advent of Code

## Day 1

### Part 1

The goal is to read the first and last digit of each string, add them together, and return the total.

To do that, we
* read each string in
* start an index pointer `a` at the start of the string and an index pointer `b` at the end of it.
* We move `a` forwards, `b` backwards, and stop each when they find a digit in the string (potentially overlapping on the same digit)
* Thus we get the first and last digit, which we stick together to make a single two-digit number, adding each to a list
* Finally, we do an add reduce on the list of numbers to get the sum, and print that

The implementation(s) can be found in [Day 1]().
