# Problem 6
"""The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is,

3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""

# Sum of numbers from 1 to n: n(n+1)/2 = son
# Sum of squares from 1 to n: (2n+1)n(n+1)/6 or (2n+1)/3 * n(n+1)/2


if __name__ == '__main__':
    n = 100
    sum_of_numbers = n * (n + 1) // 2
    sum_of_squares = ((2 * n + 1) // 3) * sum_of_numbers
    print(sum_of_numbers ** 2 - sum_of_squares)
