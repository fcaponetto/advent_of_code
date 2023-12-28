import sys

sys.path.append('..')
from utils import *

# Direction Constants
UP = (0, -1) # TODO double-check why up is y=-1
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Movement rules based on the current symbol and the previous direction
moves = {
    ('S', DOWN): DOWN,
    # If the current symbol is '|' and the previous move was DOWN or UP, continue in the same direction
    ('|', DOWN): DOWN,
    ('|', UP): UP,

    # If the current symbol is '-' and the previous move was RIGHT or LEFT, continue in the same direction
    ('-', RIGHT): RIGHT,
    ('-', LEFT): LEFT,

    # For each corner symbol ('L', 'J', '7', 'F'), define the new direction based on the previous move
    # 'L' symbol rules
    ('L', LEFT): UP,     # Turn upward if coming from left
    ('L', DOWN): RIGHT,  # Turn right if coming from down

    # 'J' symbol rules
    ('J', RIGHT): UP,    # Turn upward if coming from right
    ('J', DOWN): LEFT,   # Turn left if coming from down

    # '7' symbol rules
    ('7', RIGHT): DOWN,  # Turn downward if coming from right
    ('7', UP): LEFT,     # Turn left if coming from up

    # 'F' symbol rules
    ('F', LEFT): DOWN,   # Turn downward if coming from left
    ('F', UP): RIGHT     # Turn right if coming from up
}


def challenge_1(filename: str):
    matrix = make_char_matrix(filename)

    start_pos = (0, 0)
    # Find start
    for y, line in enumerate(matrix):
        if 'S' in line:
            x = line.index('S')
            start_pos = (x, y)
            break

    # Initial position
    curr_pos = start_pos
    curr_pipe = 'S'
    curr_dir = DOWN
    steps = 1

    while curr_pos != start_pos or steps == 1:
        curr_dir = moves[(curr_pipe, curr_dir)]
        curr_pos = (curr_pos[0] + curr_dir[0], curr_pos[1] + curr_dir[1])
        curr_pipe = matrix[curr_pos[1]][curr_pos[0]]

        steps += 1

    print('Solution:', int(steps/2))


def main():
    # filename = "data/simple.txt"
    filename = "data/challenge.txt"
    challenge_1(filename)


if __name__ == "__main__":
    main()