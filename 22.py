# Problem 22
"""Using p022_names.txt, a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order.
Then working out the alphabetical value for each name, multiply this value by its alphabetical
position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?"""

names = open("files/p022_names.txt").read().replace("\"", "").split(",")
names.sort()


def name_score(name: str) -> int:
    total = 0
    for letter in name:
        total += ord(letter) - 64  # Find int value of char and offset by 64 such that A is 1 and Z is 26
    return total


if __name__ == '__main__':
    total = 0
    for i in range(len(names)):
        total += (i + 1) * name_score(names[i])

    print(total)
