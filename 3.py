# Problem 3
"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

if __name__ == "__main__":
    n = 600851475143
    potential_factor = 3  # Since we know n is not even, we can set initial factor at 3 and increment it by two
    biggest_factor = 0

    while n != 1:
        if n % potential_factor == 0:
            # Potential factor is a factor of n, divide by factor until not possible
            biggest_factor = potential_factor
            while n % potential_factor == 0:
                n //= potential_factor

        potential_factor += 2

    print(biggest_factor)
