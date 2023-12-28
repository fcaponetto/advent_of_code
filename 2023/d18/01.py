import sys
sys.path.append("..")
from utils import *

# Direction Constants
UP = (0, 1)
DOWN = (0, -1)
LEFT = (-1, 0)
RIGHT = (1, 0)

directions = {
    'U': UP,
    'D': DOWN,
    'L': LEFT,
    'R': RIGHT
}

def challenge_1(filename):
    lines = readfile(filename)

    boundary_coordinates = [(0, 0)]
    tot_length = 0
    for line in lines:
        direction, distance = split_line(line, ' ')[0:2]
        dx, dy = directions[direction]
        distance = int(distance)

        latest_x, latest_y = boundary_coordinates[-1]
        boundary_coordinates.append(((latest_x + dx) * distance, (latest_y + dy) * distance))
        tot_length += distance

    print(tot_length)

def main():
    filename = "data/simple.txt"
    # filename = "data/challenge.txt"
    challenge_1(filename)

if __name__ == "__main__":
    main()