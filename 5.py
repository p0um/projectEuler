# Problem 5
"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

# The number wanted can be found by combining the prime factorization of the numbers smaller than 20

from typing import Dict


def prime_factorization(num: int) -> Dict[int, int]:
    factors = {}

    # Check for 2 individually so we can increment by two in the next loop
    while num % 2 == 0:
        num //= 2
        factors[2] = factors.get(2, 0) + 1

    i = 3
    while num != 1:
        while num % i == 0:
            # Divide until not possible and increment the power of the factor
            num //= i
            factors[i] = factors.get(i, 0) + 1
        i += 2

    return factors


if __name__ == '__main__':
    # Get prime factors of all numbers below twenty, only keep largest power for every prime factor
    largest_factors = {}

    for i in range(2, 21):
        factors = prime_factorization(i)

        for key in factors.keys():
            if factors[key] > largest_factors.get(key, 0):
                largest_factors[key] = factors[key]

    # Convert the factors to a real number
    result = 1
    for factor, power in largest_factors.items():
        result *= factor ** power

    print(result)
