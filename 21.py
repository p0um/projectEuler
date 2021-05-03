# Problem 21
"""Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000."""
import utils


def d(n: int) -> int:
    total = 0
    for divisor in utils.divisors(n):
        if divisor != n:
            total += divisor
    return total


# Used to avoid summing the same pair twice (a, b) and (b, a)
already_seen = {}

if __name__ == '__main__':
    total = 0
    for a in range(2, 10000):
        b = d(a)

        if d(b) == a and a != b and a not in already_seen:
            total += a + b
            already_seen[b] = 0

    print(total)
