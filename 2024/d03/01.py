from utils import *
import re

# Regular expression to match 'mul(X,Y)' where X and Y are digits
pattern = r"mul\((\d+),(\d+)\)"


def challenge(filename: str):
    line = readfile(filename)
    line = ''.join(line)

    # Find all matches
    matches = [(int(x), int(y)) for x, y in re.findall(pattern, line)]

    result = sum(x * y for x, y in matches)

    print(result)


# data = 'data/simple.txt'
data = 'data/input.txt'
challenge(data)
