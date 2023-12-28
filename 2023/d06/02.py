import sys
import math

sys.path.append('..')
from utils import *


def solve_equation(poly: [], x: int) -> int:
    n = len(poly)

    result = poly[0]
    for i in range(1, n):
        result = result * x + poly[i]

    return result


def solve_equation_2(poly: []) -> list:
    sol1 = (-poly[1] + math.sqrt(poly[1]**2 -(4*poly[0]*poly[2])))/(2*poly[0])
    sol2 = (-poly[1] - math.sqrt(poly[1]**2 -(4*poly[0]*poly[2])))/(2*poly[0])

    return [sol1, sol2]


def challenge_2(filename: str):
    lines = readfile(filename)

    constraints = 0
    for idx, line in enumerate(lines):
        line = split_line(line, ":")[-1]
        value = extract_and_combine_numbers(line)

        if idx == 0:
            constraints = value

        if idx == 1:
            constraints = (constraints, value)

    print(constraints)

    output = 1
    # for constraint in constraints:
    interval = solve_equation_2([-1, constraints[0], -constraints[1]])
    sol1_float = interval[0]
    sol2_float = interval[1]
    sol1_int = math.ceil(sol1_float)
    sol2_int = math.floor(sol2_float)
    output *= sol2_int - sol1_int + 1 - (sol1_float == sol1_int) - (sol2_float == sol2_int)
    # integers_in_solution_interval = [i for i in range(0, constraints[0]+1) if interval[0] < i < interval[1]]
    # output.append(len(integers_in_solution_interval))

    print(output)


# f = "data/simple.txt"
f = "data/challenge.txt"
challenge_2(f)
