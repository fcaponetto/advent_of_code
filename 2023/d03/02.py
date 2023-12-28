import sys

sys.path.append('..')
from utils import *


def extract_number_positions(input_string: str) -> list:
    """
    It extracts the start and end position of a digit
    :rtype: list of tuples that include start-end positions
    """
    result = []
    current_number = ''
    for i, char in enumerate(input_string):
        if char.isdigit():
            current_number += char
        elif current_number:
            result.append((i - len(current_number), i - 1, int(current_number)))
            current_number = ''

    # trailing number
    if current_number:
        result.append((len(input_string) - len(current_number), len(input_string) - 1, int(current_number)))

    return result


def is_star(char):
    return char == '*'


def extract_star_positions(input_string: str) -> list:
    """
    It extracts the start and end position of a star
    :rtype: list of tuples that include start-end positions
    """
    result = []
    current_symbol = ''

    for i, char in enumerate(input_string):
        if is_star(char):
            current_symbol += char
        elif current_symbol:
            result.append(i - len(current_symbol))
            current_symbol = ''

    # trailing number
    if current_symbol:
        result.append(len(input_string) - len(current_symbol))

    return result


def challenge_2(filename: str):
    lines = readfile(filename)
    output = 0
    gears = []

    for idx, line in enumerate(lines):

        star_pos = extract_star_positions(line)
        for s in star_pos:

            # given the current stars, check against numbers the current row
            num_pos = extract_number_positions(line)
            p_n = 0
            p_r = 0
            for n in num_pos:
                # must be adjacent
                if n[0] - s == 1 or s - n[1] == 1:
                    # the start is a pivot between two numbers
                    gears.append(n[2])
                    if n[0] - p_r == 2:
                        gears.append(p_n)
                    p_r = n[1]
                    p_n = n[2]

            # given current stars, check against the numbers in the previous row
            if idx > 0:
                num_pos = extract_number_positions(lines[idx-1])

                for n in num_pos:
                    # must be within len(number) + 1
                    if -1 <= n[0] - s <= 1 or -1 <= n[1] - s <= 1:
                        gears.append(n[2])

            # given current stars, check against the numbers in the following row
            if idx < len(lines) - 1:
                num_pos = extract_number_positions(lines[idx+1])

                for n in num_pos:
                    # must be within len(number) + 1
                    if -1 <= n[0] - s <= 1 or -1 <= n[1] - s <= 1:
                        gears.append(n[2])

            # if even, pop last element because it's not valid combination
            if len(gears) % 2 != 0:
                gears.pop()

    for i in range(0, len(gears) - 1, 2):
        output += gears[i] * gears[i + 1]

    print(output)


# f = "data/simple.txt"
f = "data/challenge.txt"
challenge_2(f)
