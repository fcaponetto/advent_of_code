import sys

sys.path.append('..')
from utils import *


def add_extra_column_row(matrix):
    # Find rows without '#'
    rows_to_add = [i for i, row in enumerate(matrix) if '#' not in row]

    # Find columns without '#'
    cols_to_add = [j for j in range(len(matrix[0])) if all(matrix[i][j] != '#' for i in range(len(matrix)))]

    # Add an extra row at each position where needed reverse order because if we add from the top first, the original
    # next index is not valid anymore. Eg. you need to insert new rows at indices 2 and 5. If you insert at index 2
    # first, the row that was originally at index 5 will now be at index 6
    for i in sorted(rows_to_add, reverse=True):
        matrix.insert(i, ['.' for _ in range(len(matrix[0]))])

    # Add an extra column at each position where needed
    for j in sorted(cols_to_add, reverse=True):
        for row in matrix:
            row.insert(j, '.')


def find_galaxy(matrix):
    # Initialize the counter for numbering
    galaxies = []

    # Iterate through each cell in the matrix
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            # If a '#' is found, replace it with the current count
            if matrix[y][x] == '#':
                galaxies.append((x, y))

    return galaxies


def calculate_pairs(galaxies):
    pairs = []
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            # print(i+1, j+1, galaxies[i], galaxies[j])
            pairs.append((i+1, j+1, galaxies[i], galaxies[j]))

    return pairs


def challenge_1(filename: str):
    matrix = make_char_matrix(filename)

    add_extra_column_row(matrix)
    # print_matrix(matrix)
    galaxies = find_galaxy(matrix)
    galaxy_pairs = calculate_pairs(galaxies)
    print(len(galaxy_pairs))

    output = 0
    for i, j, star1, star2 in galaxy_pairs:
        tmp = abs(star1[0] - star2[0]) + abs(star1[1] - star2[1])
        print(i, j, star1, star2)
        output += tmp

    print(output)


def main():
    filename = "data/simple.txt"
    # filename = "data/challenge.txt"
    challenge_1(filename)


if __name__ == "__main__":
    main()
