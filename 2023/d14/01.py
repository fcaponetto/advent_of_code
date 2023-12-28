import sys
sys.path.append("..")
from utils import *


def compute_load(matrix):
    count = 0
    up = [0] * len(matrix[0])
    top = len(matrix)
    for y, row in enumerate(matrix):
        for x, col in enumerate(matrix[y]):
            if matrix[y][x] == 'O':
                if up[x] > 0:
                    matrix[y-up[x]][x] = matrix[y][x]
                    count += 1 * top - y + up[x]
                    matrix[y][x] = '.'
                    up[x] -= 1
                else:
                    count += top - y
            if matrix[y][x] == '#':
                up[x] = 0
            if matrix[y][x] == '.':
                up[x] += 1

    return count


def challenge_1(filename: str):
    matrix = make_char_matrix(filename)

    print_matrix(matrix)

    load = 0
    load += compute_load(matrix)

    print()
    print_matrix(matrix)

    print(load)


def main():
    filename = "data/simple.txt"
    # filename = "data/challenge.txt"
    challenge_1(filename)


if __name__ == "__main__":
    main()