# Problem 16
"""2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?"""


def smart_power(x, n):
    """
    This function tries to optimize the way powers are found. By converting the power to binary and only multiplying
    x to the power of 2^i, where the ith bit is 1 in the binary representation, we can reduce the number
    of multiplications needed.

    Example:
        2^7, binary(7)=111
        2^(2^0) * 2^(2^1) * 2^(2^2) = 2^1 * 2^2 * 2^4 = 2^7

        2^5, binary(5)=101
        2^(2^0) * 2^(2^2) = 2^1 * 2^4 = 2^5
    """

    binary = "{0:b}".format(n)
    powers = {}
    i = 1
    powered_x = x
    for _ in range(len(binary)):
        powers[i] = powered_x
        i *= 2
        powered_x *= powered_x

    result = 1
    i = 1
    for bit in binary[::-1]:
        if bit == "1":
            result *= powers[i]
        i *= 2
    return result


if __name__ == '__main__':
    total = 0
    for digit in str(smart_power(2, 1000)):
        total += int(digit)
    print(total)
