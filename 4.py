# Problem 4
"""A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers."""


def is_palindrome(num: int) -> bool:
    str_num = str(num)
    length = len(str_num)
    i = 0

    while i < length // 2:
        if str_num[i] != str_num[-(i + 1)]:
            # Digits do not match
            return False
        i += 1

    # All digits match
    return True


if __name__ == '__main__':
    largest = 0
    for a in range(999, 0, -1):
        for b in range(a, 0, -1):
            product = a * b
            # Only check for palindrome if the product is larger than the current largest palindrome.
            if product > largest and is_palindrome(product):
                largest = product

    print(largest)
