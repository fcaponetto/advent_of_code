import sys

sys.path.append('..')
from utils import *
import math


def lcm(a, b):
    """Compute the Least Common Multiple of a and b."""
    return abs(a * b) // math.gcd(a, b)


def challenge_1(filename: str):
    lines = readfile(filename)

    directions = ""
    nodes = {}
    start_nodes = []

    for i, line in enumerate(lines):
        if i == 0:
            directions = line
            continue
        if i == 1:
            continue
        node, children = split_line(line, ' = ')
        if node.endswith('A'):
            start_nodes.append(node)
        children = split_line(children[1:-1], ',')
        nodes[node] = [child.strip() for child in children]

    curr_nodes = start_nodes
    i, steps = 0, 1
    route_durations = []
    while i < len(directions):
        dir = directions[i]

        for j, node in enumerate(curr_nodes):
            curr_nodes[j] = nodes[node][0 if dir == "L" else 1]

        if any(node.endswith('Z') for node in curr_nodes):
            route_durations.append(steps)
        if len(route_durations) == len(curr_nodes):
            break

        steps += 1
        i = (i + 1) % len(directions)

    # LCM is useful in situations where you have multiple cyclic processes and
    # you want to find out when they all align or complete a cycle simultaneously, like this case
    output = route_durations[0]
    for step in route_durations[1:]:
        output = lcm(output, step)

    print(output)


# f = "data/simple2.txt"
f = "data/challenge.txt"
challenge_1(f)
