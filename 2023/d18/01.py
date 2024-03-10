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
    boundary_points = 0
    for line in lines:
        direction, distance = split_line(line, ' ')[0:2]
        dx, dy = directions[direction]
        distance = int(distance)

        cur_x, cur_y = boundary_coordinates[-1]
        boundary_points += distance
        boundary_coordinates.append((cur_x + (dx * distance), cur_y + (dy * distance)))

    # Calculate the area of the polygon using the Shoelace formula
    # https://en.wikipedia.org/wiki/Shoelace_formula
    area = 0

    boundary_coordinates_size = len(boundary_coordinates)
    for i in range(len(boundary_coordinates)):
        # Calculate the signed area contribution of the current segment and add it to the total area
        area += boundary_coordinates[i][0] * \
                (boundary_coordinates[i - 1][1] - boundary_coordinates[(i + 1) % boundary_coordinates_size][1])

    area = abs(area) // 2

    # Use Pick's theorem to calculate the number of interior points
    # https://en.wikipedia.org/wiki/Pick%27s_theorem
    interior_points = area - boundary_points // 2 + 1

    print(interior_points + boundary_points)


def main():
    # filename = "data/simple.txt"
    filename = "data/input.txt"
    challenge_1(filename)

if __name__ == "__main__":
    main()