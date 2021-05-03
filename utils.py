import math
from typing import List, Set


# -- Primes --

def prime_sieve(n: int) -> List[int]:
    """
    Returns all primes that are smaller or equal to n.

    :param n: The limit of primes to calculate
    :return: An array containing all primes smaller or equal to n
    """

    if n < 2:
        return []  # No primes smaller than 2

    # Fill an array with the value True if index is odd, False if even
    sieve = [bool(i & 1) for i in range(n + 2)]

    primes = [2]

    i = 3
    while True:
        multiple = i ** 2  # We can start checking at prime^2, since previous multiples will already have been checked
        if multiple > n:
            # First multiple is bigger than n, reached end of possible primes
            break

        # Mark all multiples of i as not prime
        while multiple < n:
            sieve[multiple] = False
            multiple += i

        # Save i in the primes array
        primes.append(i)

        # Find next value of i (next index in array that is true)
        i += 1
        while not sieve[i]:
            i += 1

    # Add remaining primes to array
    i = primes[-1] + 1
    while i < n:
        if sieve[i]:
            primes.append(i)
        i += 1

    return primes


# -- General --

def divisors(n: int) -> Set[int]:
    """
    Returns a set containing all the divisors of a number.

    :param n: The number for which we want to find the divisors.
    :return: A set containing the divisors.
    """
    if n == 1:
        return {1}

    divs = [1, n]

    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            divs.append(i)
            divs.append(n // i)
    return set(divs)  # Return as set to remove duplicates.
