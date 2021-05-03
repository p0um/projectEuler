# Problem 19
"""You are given the following information, but you may prefer to do some research for yourself.

* 1 Jan 1900 was a Monday.
* Thirty days has September,
  April, June and November.
  All the rest have thirty-one,
  Saving February alone,
  Which has twenty-eight, rain or shine.
  And on leap years, twenty-nine.
* A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?"""

from typing import Tuple


def find_tomorrow(day: int, month: int, year: int) -> Tuple[int, int, int]:
    end_of_month = 31
    if month in [4, 6, 9, 11]:
        end_of_month = 30
    elif month == 2:
        # February, check if leap
        if year % 4 == 0 and (year % 100 != 0 or (year % 100 == 0 and year % 400 == 0)):
            # Multiple of 4, given not century unless multiple of 400 means leap year
            end_of_month = 29
        else:
            end_of_month = 28

    if day == end_of_month:
        # Need to change month, check if we also need to change year
        if month == 12:
            year += 1
            month = 1
        else:
            month += 1
        day = 1
    else:
        # Only need to increment day
        day += 1

    return day, month, year


if __name__ == '__main__':
    # First Sunday of 1901 was 6 Jan 1901
    day, month, year = 6, 1, 1901
    total = 0

    while year < 2001:
        if day == 1:
            total += 1

        for _ in range(7):
            day, month, year = find_tomorrow(day, month, year)

    print(total)
