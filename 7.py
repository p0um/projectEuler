# Problem 7

"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?"""

import utils

if __name__ == '__main__':
    # According to prime number theorem, the number of primes before the number n is,
    # #p ~= n/ln(n), which means that to find the 10,001st prime, we have n ~= 117000

    n = 117000
    primes = utils.prime_sieve(n)
    while len(primes) < 10001:
        n = int(n * 1.10)  # Increment by 10% until we have enough primes
        utils.prime_sieve(n)

    print(primes[10000])
