import sys

sys.path.append('..')
from utils import *


def convert_to_digits(input_string: str):
    digit_mapping = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    for key, value in digit_mapping.items():
        if key in input_string:
            # to overcome the issue of common characters used for both digits spelled out with letters
            # the digit spelled with letter becomes NumberDigitNumber
            # Eg. eightwothree ->eight8eightwo2twothree3three
            input_string = input_string.replace(key, key + value + key)

    return input_string


def challenge_2(filename: str):
    lines = readfile(filename)

    output = 0
    for line in lines:
        line = convert_to_digits(line)
        i = 0
        j = len(line) - 1

        two_digits = [0, 0]
        found1, found2 = False, False

        while not found1 or not found2:
            if not line[i].isnumeric():
                i += 1
            elif not found1:
                found1 = True
                two_digits[0] = (line[i])

            if not line[j].isnumeric():
                j -= 1
            elif not found2:
                found2 = True
                two_digits[1] = line[j]
        curr = (int(str(two_digits[0]) + str(two_digits[1])))
        output += curr

    print(output)


# f = "data/simple2.txt"
f = "data/challenge2.txt"
challenge_2(f)
