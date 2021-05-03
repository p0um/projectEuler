# Problem 18
"""By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

              75
             95 64
            17 47 82
           18 35 87 10
          20 04 82 47 65
         19 01 23 75 03 34
        88 02 77 73 07 63 67
       99 65 04 28 06 16 70 92
      41 41 26 56 83 40 80 70 33
     41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
   70 11 33 28 77 73 17 78 39 68 17 57
  91 71 52 38 17 14 91 43 58 50 27 29 48
 63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
However, Problem 67, is the same challenge with a triangle containing one-hundred rows;
it cannot be solved by brute force, and requires a clever method! ;o)"""

# Instead of solving from top to bottom, go from the bottom to the top and use memoization to remember largest
# route possible from a specific position.

from typing import List, Tuple, Dict

problem_input = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23""".split("\n")
pyramid = [[int(i) for i in row.split(" ")] for row in problem_input]


def possible_next_move(row: int, col: int) -> List[Tuple[int, int]]:
    # We know the possible moves will always be one row below (the number will be one bigger)
    # and the column will be the current column and the current column + 1
    return [(row + 1, col), (row + 1, col + 1)]


largest_road: Dict[Tuple[int, int], int] = {}


def find_largest_road(position: Tuple[int, int]) -> int:
    row, col = position
    if row == 14:
        # Last row, biggest road is value of cell
        return pyramid[row][col]
    elif position in largest_road:
        return largest_road[position]
    else:
        left_move, right_move = possible_next_move(row, col)
        largest_road[position] = pyramid[row][col] + max(find_largest_road(left_move), find_largest_road(right_move))
        return largest_road[position]

        # for move in possible_next_move(row, col):
        #     largest_road[row, col] = find_largest_road(move[0], move[1])
        #     total += largest_road[row, col]
        # return total


if __name__ == '__main__':
    print(find_largest_road((0, 0)))
