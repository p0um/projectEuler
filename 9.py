# Problem 9
"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""

# The 3 rules we have are:
#   (1) a < b < c
#   (2) a + b + c = 1000
#   (3) a^2 + b^2 = c^2

# We can isolate c in (2) to get c = 1000 - a - b
# Plugging that in (3), we get a^2 + b^2 = (1000 - a - b)^2
# Solving for b, we get that b = 1000(500 - a)/(1000 - a)  <-- a cannot be 1000 to avoid division by 0


if __name__ == '__main__':
    for a in range(1, 1000):
        b = 1000 * (500 - a) / (1000 - a)
        # b has to be a natural number that is bigger than a
        if b != int(b) or b < a:
            continue

        b = int(b)
        c = 1000 - a - b
        print(a * b * c)
        break
