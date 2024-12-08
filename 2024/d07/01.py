from utils import *

class Equation:
    def __init__(self, value, inputs):
        self.value = value
        self.inputs = inputs


def parse_input(input_data):
    equations = []
    lines = readfile(input_data)
    for line in lines:
        parts = line.split(":")
        value = int(parts[0].strip())
        inputs = list(map(int, parts[1].strip().split()))
        equations.append(Equation(value, inputs))
    return equations


def check_operator(i, value, inputs, tmp_op):
    if value == tmp_op:
        return True
    if i >= len(inputs):
        return False

    tmp_op += inputs[i]
    if check_operator(i+1, value, inputs, tmp_op):
        return True
    tmp_op -= inputs[i]

    tmp_op *= inputs[i]
    if check_operator(i+1, value, inputs, tmp_op):
        return True


def challenge(equations):
    total = 0
    tmp_op = 0
    for equation in equations:
        if check_operator(0, equation.value, equation.inputs, tmp_op):
            total += equation.value
    return total

# input_data = 'data/simple.txt'
input_data = 'data/input.txt'
equations = parse_input(input_data)
res = challenge(equations)
print(res)

# 227921760109726
# 227921760682526 mio