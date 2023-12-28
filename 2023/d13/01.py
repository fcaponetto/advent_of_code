import sys
sys.path.append("..")
from utils import *


def get_line_point_of_incidence(line, i: int, j: int):
    mirrored = True
    while i < j:
        if line[i] != line[j]:
            mirrored = False
            break
        i += 1
        j -= 1

    if mirrored:
        return i
    else:
        return 0


def get_vertical_point_of_incidence(matrix):
    max_reflection = len(matrix[0])
    # if (max_reflection % 2) != 0:
    #     max_reflection -= 1
    i = 0
    j = max_reflection-1

    while i < j:
        for a in range(max_reflection-j):
            vertical_point = get_line_point_of_incidence(matrix[0], i+a, j+a)
        if vertical_point:
            break
        j -= 1

    return vertical_point


def get_horizontal_point_of_incidence(matrix):

    line = []
    for y in range(len(matrix)):
        line.append(matrix[y][0])

    # print(line)

    max_reflection = len(line)
    # if (max_reflection % 2) != 0:
    #     max_reflection -= 1
    i = 0
    j = max_reflection-1

    while i < j:
        for a in range(max_reflection-j):
            horizontal_point = get_line_point_of_incidence(line, i+a, j+a)
        if horizontal_point:
            break
        j -= 1
    # if not horizontal_point and max_reflection < len(line):
    #     horizontal_point = get_line_point_of_incidence(line, i+1, j+1)  # shift to the right

    return horizontal_point


def challenge_1(filename: str):
    lines = readfile(filename)

    patterns = []
    pattern = []
    for i, line in enumerate(lines):
        if line != '':
            pattern.append(list(line))
        if line == '' or i == len(lines)-1:
            print_matrix(*pattern)
            print(*zip(*pattern))
            patterns.append(pattern)
            pattern = []


    # print_matrix(patterns)

    # output = 0
    # for pattern in patterns:
    #
    #     rows = get_horizontal_point_of_incidence(pattern)
    #
    #     cols = 0
    #     # if rows == 0:
    #     cols = get_vertical_point_of_incidence(pattern)
    #     # if tmp != 0:
    #
    #     print(cols, rows)
    #
    #     output += cols + rows
    #
    # print(output)



def main():
    # filename = "data/simple.txt"
    filename = "data/challenge.txt"
    challenge_1(filename)


if __name__ == "__main__":
    main()