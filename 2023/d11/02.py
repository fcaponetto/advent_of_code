import sys

sys.path.append('..')
from utils import *


def find_empty_star_row_colum(matrix):
    # Find rows without '#'
    empty_rows = [i for i, row in enumerate(matrix) if '#' not in row]

    # Find columns without '#'
    empty_col = [j for j in range(len(matrix[0])) if all(matrix[i][j] != '#' for i in range(len(matrix)))]

    return [empty_rows, empty_col]

from bisect import bisect
def find_galaxy(matrix, empty_rows_cols):
    # Initialize the counter for numbering
    galaxies = []

    expand_by = 1_000_000 - 1
    # Iterate through each cell in the matrix
    # for y in range(len(matrix)):
    for y, row in enumerate(matrix):
        # for x in range(len(matrix[y])):
        for x, col in enumerate(matrix[y]):
            if matrix[y][x] == '#':
                dx = expand_by * bisect(empty_rows_cols[1], x)
                # dx = bisect(empty_rows_cols[1], x)
                dy = expand_by * bisect(empty_rows_cols[0], y)
                # dy = bisect(empty_rows_cols[0], y)
                galaxies.append((x + dx, y + dy))

    return galaxies


def calculate_pairs(galaxies):
    pairs = []
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            # print(i+1, j+1, galaxies[i], galaxies[j])
            pairs.append((i+1, j+1, galaxies[i], galaxies[j]))

    return pairs


def challenge_2(filename: str):
    matrix = make_char_matrix(filename)

    for x in range(len(matrix)):  # Iterate over each column index
        print(matrix[x])

    empty_rows_cols = find_empty_star_row_colum(matrix)
    print_matrix(matrix)
    galaxies = find_galaxy(matrix, empty_rows_cols)
    galaxy_pairs = calculate_pairs(galaxies)
    print(len(galaxy_pairs))

    output = 0
    for i, j, first, second in galaxy_pairs:
        tmp = abs(first[0] - second[0]) + abs(first[1] - second[1])
        print(i, j, first, second)
        output += tmp

    print(output)


def main():
    # filename = "data/simple.txt"
    filename = "data/challenge.txt"
    challenge_2(filename)


if __name__ == "__main__":
    main()
