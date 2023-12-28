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


def is_symbol(char):
    return not char.isalnum() and not char.isspace() and not char == '.'


def extract_symbol_positions(input_string: str) -> list:
    """
    It extracts the start and end position of a symbol
    :rtype: list of tuples that include start-end positions
    """
    result = []
    current_symbol = ''

    for i, char in enumerate(input_string):
        if is_symbol(char):
            current_symbol += char
        elif current_symbol:
            result.append(i - len(current_symbol))
            current_symbol = ''

    # trailing number
    if current_symbol:
        result.append(len(input_string) - len(current_symbol))

    return result


def challenge_1(filename: str):
    lines = readfile(filename)
    output = 0

    num_pos_prev = []
    sym_pos_prev = []
    for line in lines:
        num_pos = extract_number_positions(line)
        sym_pos = extract_symbol_positions(line)

        # given the current symbols, check against numbers the current row
        for s in sym_pos:
            for n in num_pos:
                # must be adjacent
                if n[0] - s == 1 or s - n[1] == 1:
                    output += n[2]
                    print(n[2])

        # given current symbols, check against the numbers in the previous row
        for s in sym_pos:
            for n in num_pos_prev:
                # must be within len(number) + 1
                if -1 <= n[0] - s <= 1 or -1 <= n[1] - s <= 1:
                    output += n[2]
                    print(n[2])

        # given the current numbers, check against the numbers in the previous symbols
        for n in num_pos:
            for s in sym_pos_prev:
                # must be within len(number) + 1
                if -1 <= n[0] - s <= 1 or -1 <= n[1] - s <= 1:
                    output += n[2]
                    print(n[2])

        # save it to be used in the next row
        num_pos_prev = num_pos
        sym_pos_prev = sym_pos

    print(output)


# f = "data/simple.txt"
f = "data/challenge.txt"
challenge_1(f)
