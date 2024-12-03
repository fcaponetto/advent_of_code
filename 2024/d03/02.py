from utils import *
import re

# Regular expression to match 'mul(X,Y)' where X and Y are digits, or do() or don't()
mul_do_dont_patter = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"


def challenge(filename: str):
    line = readfile(filename)
    line = ''.join(line)

    enabled = True  # Mul instructions are enabled by default

    # Find all matches for mul(), do(), don't()
    matches = re.findall(mul_do_dont_patter, line)
    print(matches)

    result = 0
    for group in matches:
        if group == "do()":
            enabled = True
        elif group == "don't()":
            enabled = False
        elif enabled:  # Process mul(X, Y) if enabled
            values = group[4:-1].split(",")  # Extract numbers inside mul()
            result += int(values[0]) * int(values[1])

    print(result)


# data = 'data/simple2.txt'
data = 'data/input.txt'
challenge(data)
