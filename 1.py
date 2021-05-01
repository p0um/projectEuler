# Problem 1
"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000."""

if __name__ == "__main__":
    total = 0

    # Start with multiples of three
    # Ignore every fifth multiple of three, since this number is also a multiple of 5
    # which will be added in the next loop (don't want duplicates)
    n = 3
    i = 1
    while n < 1000:
        if i % 5 == 0:
            i = 1
        else:
            i += 1
            total += n
        n += 3

    # Multiples of 5
    n = 5
    while n < 1000:
        total += n
        n += 5

    print(total)
