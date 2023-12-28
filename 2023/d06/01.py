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


def challenge_1(filename: str):
    lines = readfile(filename)

    constraints = []
    for idx, line in enumerate(lines):
        line = split_line(line, ":")[-1]
        values = extract_numbers(line)

        if idx == 0:
            for value in values:
                constraints.append(value)

        if idx == 1:
            for j, value in enumerate(values):
                constraints[j] = (constraints[j], value)

    output = 1
    for constraint in constraints:
        interval = solve_equation_2([-1, constraint[0], -constraint[1]])
        sol1_float = interval[0]
        sol2_float = interval[1]
        sol1_int = math.ceil(sol1_float)
        sol2_int = math.floor(sol2_float)
        output *= sol2_int - sol1_int + 1 - (sol1_float == sol1_int) - (sol2_float == sol2_int)
        # integers_in_solution_interval = [i for i in range(0, constraint[0]+1) if interval[0] < i < interval[1]]
        # output.append(len(integers_in_solution_interval))

    print(output)


"""
0   0*(7-0)
1   1*(7-1) = 6
2   2*(7-2) = 10 *         
3   3*(7-3) = 12 *
4   4*(7-4) = 12 *
5   5*(7-5) = 10 *
6   6*(7-6) = 6 
7   7*(7-7) = 0
-x^2 + 7x - 9 > 0
"""
# p = [-1, 7, -9]
# out = solve_equation_2(p)

# have a look here https://www.reddit.com/r/adventofcode/comments/18bwe6t/comment/kc71csv/

# f = "data/simple.txt"
f = "data/challenge.txt"
challenge_1(f)