# Problem 14
"""The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million."""

sequence_length = {}


def collatz_sequence(n: int) -> int:
    if n == 1:
        return 1
    elif n in sequence_length:
        return sequence_length[n]
    else:
        if n & 1:
            # Odd
            length = 1 + collatz_sequence(3 * n + 1)
            sequence_length[n] = length
            return length
        else:
            # Even
            length = 1 + collatz_sequence(n // 2)
            sequence_length[n] = length
            return length


if __name__ == '__main__':
    longest_number = 0
    longest_length = 0
    for i in range(1, 1000000):
        length = collatz_sequence(i)
        if length > longest_length:
            longest_number = i
            longest_length = length

    print(longest_number)
