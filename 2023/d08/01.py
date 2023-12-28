import sys

sys.path.append('..')
from utils import *


def challenge_1(filename: str):
    lines = readfile(filename)

    directions = ""
    nodes = {}

    for i, line in enumerate(lines):
        if i == 0:
            directions = line
            continue
        if i == 1:
            continue
        node, children = split_line(line, ' = ')
        children = split_line(children[1:-1], ',')
        nodes[node] = [child.strip() for child in children]

    node = 'AAA'
    i, steps = 0, 1
    while i < len(directions):
        dir = directions[i]

        node = nodes[node][0 if dir == "L" else 1]

        if node == 'ZZZ':
            break

        steps += 1
        i = (i + 1) % len(directions)

    print(steps)


# f = "data/simple.txt"
f = "data/challenge.txt"
challenge_1(f)
