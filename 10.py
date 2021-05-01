# Problem 10
"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""

import utils

if __name__ == '__main__':
    primes = utils.prime_sieve(2000000)
    total = 0
    for prime in primes:
        total += prime
    print(total)
