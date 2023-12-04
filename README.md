# Advent of Code 2023

My solutions to this year's Advent of Code

## Day 1

### Part 1

The goal is to read the first and last digit of each string, add them together, and return the total.

To do this, we:
* read each string in
* start an index pointer `l` at the start of the string and an index pointer `r` at the end of it.
* We move `l` forwards, `r` backwards, and stop each when they find a digit in the string (potentially overlapping on the same digit)
* Thus we get the first and last digit, which we stick together to make a single two-digit number, adding each to a list
* Finally, we do an add reduce on the list of numbers to get the sum, and print that

The implementation(s) can be found in [Day 1 Part 1]().

### Part 2

The difference this time is that there are number-words instead of just digits which need to be treated like digits. Otherwise this is just problem 1 again.

So to do this we:
* find and replace the first instance of a number word (ordered from longest words to smallest words for greedy match)
* do the same for the last instance (all strings reversed to keep replacement simple)
* finally, continue on to doing exactly what was done in Part 1.

More specifically, we need to do a sliding window to match greedily the first and last shortest string qnd replace them with their digits.
A potential better future approach is to do a single slide left to right matching for words or digits and keeping mind the firet and last ones.

The implementation(s) can be found in [Day 1 Part 2]().
