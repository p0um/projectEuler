# Problem 17
"""If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and
115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance
with British usage."""

units = {
    0: 0,
    1: 3,
    2: 3,
    3: 5,
    4: 4,
    5: 4,
    6: 3,
    7: 5,
    8: 5,
    9: 4
}

teens = {
    0: 3,
    1: 6,
    2: 6,
    3: 8,
    4: 8,
    5: 7,
    6: 7,
    7: 9,
    8: 8,
    9: 8
}

tens = {
    2: 6,
    3: 6,
    4: 5,
    5: 5,
    6: 5,
    7: 7,
    8: 6,
    9: 6
}

# Hundreds are simply units + "hundred"
hundreds = {}
for i in range(1, 10):
    hundreds[i] = units[i] + 7


def letters_in_word(n: int) -> int:
    if n == 1000:
        return 11

    length = 0

    hundreds_digit = n // 100
    tens_digit = n // 10 % 10
    units_digit = n % 10

    if hundreds_digit != 0:
        length += units[hundreds_digit]
        length += 7  # "hundred"
        if n % 100 != 0:
            # There are numbers after the hundreds place, ie not 100, 200, 300, etc...
            length += 3  # "and"

    if tens_digit == 0:
        # Only units
        length += units[units_digit]
    elif tens_digit == 1:
        # 10-19
        length += teens[units_digit]
    else:
        # 20-99
        length += tens[tens_digit]
        length += units[units_digit]

    return length


if __name__ == '__main__':
    total = 0
    for i in range(1, 1001):
        total += letters_in_word(i)
    print(total)

    print(letters_in_word(115))
