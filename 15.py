# Problem 15
"""Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?"""

# Since we want to move from the top left to the bottom right,
# we need to move n times to the right and n times downwards.

# This means that we need 2n moves, n of which will be in one direction.
# In other words, the number of possible routes will be 2nCn (combination)

import math


def combination(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))


if __name__ == '__main__':
    n = 20
    print(combination(2 * n, n))
