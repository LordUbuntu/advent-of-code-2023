# Advent of Code 2023

My solutions to this year's Advent of Code

## Day 1

### Part 1

The goal is to read the first and last digit of each string, add them together, and return the total.

To do this, we:
* read each `string` in from the specified `filename`
* starting on `index` 0, we iterate over the length of `string`
  * each iteration, we get the character at the current `index`
  * if the character is a digit we record that as the 10s digit
  * otherwise we record the current digit as the 1s digit
* Thus we get the first and last digit, which we join together to make a single `number`
* Finally, we convert that string representation to an integer and add it to the `total`
* return `total`

### Part 2

This time we operate by the same principle but with a sliding window to match against substrings (number words) in addition to matching single digits. 

To do this we:
* utilize `index` to point to the start of the window
  * check if the character in `string` at `index` is a digit
    * if it is
      * record the digit like in part one and continue
    * otherwise
      * iterate over the dictionary of number words greedily (from shortest)
        * if all characters match, record the equivalent digit as in part 1
* finally, join the number, add its value to `total`, and return `total`

### Comments

Interestingly both of these solutions are single-pass.

The implementation(s) can be found in [Day 1]().



## Day 2

### Part 1

This one is trivial. We only need to check if the limits of red, green, or blue cubes
was violated at any one time (if there were any occurrences of them exceeding 12, 13,
and 14 respectively). Then we just tally the total of the id's of all games which did
not.

To do this we:
* read each line, parsing red, green, and blue `counts` along with the `id` number
  * if any `count` for any `color` exceeds its maximum
    * continue to next game
  * otherwise
    * add game `id` to `total`
* return `total`
