import sys
sys.path.append("..")
from utils import *

import matplotlib.pyplot as plt
import numpy as np
def plot_two_lines(slope1, intercept1, slope2, intercept2, x_range):
    """
    Plot two lines given their slopes and y-intercepts.

    :param slope1: Slope of the first line
    :param intercept1: y-intercept of the first line
    :param slope2: Slope of the second line
    :param intercept2: y-intercept of the second line
    :param x_range: Range of x-values to plot
    """
    x_values = np.linspace(x_range[0], x_range[1], 400)
    y_values1 = slope1 * x_values + intercept1
    y_values2 = slope2 * x_values + intercept2

    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values1, label=f'Line 1: y = {slope1}x + {intercept1}')
    plt.plot(x_values, y_values2, label=f'Line 2: y = {slope2}x + {intercept2}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Plot of Two Lines')
    plt.legend()
    plt.grid(True)
    plt.show()


def get_slope(x1, x2, y1, y2):
    # Calculate the slope (m) using the two points (y2-y1)/(x2-x1)
    m = (y2 - y1) / (x2 - x1)
    return m


def get_y_intercept(x, y, m):
    # Now, use one of the points and the slope to find c (y-intercept)
    # y = m*x + c => c = y - m*x
    c = y - m * x
    return c


def get_intercept_point(c1, m1, c2, m2):
    try:
        # Solving for x: m1*x + c1 = m2*x + c2
        # Rearranging the equation: m1*x - m2*x = c2 - c1
        x_intercept = (c2 - c1) / (m1 - m2)

        # Finding y using one of the line equations
        # y = m2*x + c2
        y_intercept = m2 * x_intercept + c2

        return x_intercept, y_intercept
    except:
        # In case the solver fails
        return None


def get_second_point(x, y, vx, vy):
    return tuple((x + vx, y + vy))


def is_future(start1x, velocity1x, start2x, velocity2x, x, y):
    # you have to take care to test that time > 0 at the time of intersection. if the hailstone starts before the
    # intersection point but it goes backwards (negative velocity), therefore the intersection happens in the past (
    # t<0)
    if start1x < x and velocity1x < 0:
        return False
    if start1x > x and velocity1x > 0:
        return False
    if start2x < x and velocity2x < 0:
        return False
    if start2x > x and velocity2x > 0:
        return False
    return True


def challenge_1(filename: str):
    lines = readfile(filename)

    trajectories = []
    # min_range = 7
    min_range = 200_000_000_000_000
    max_range = 400_000_000_000_000
    for line in lines:
        line = split_line(line, "@")
        p1 = tuple(extract_numbers(line[0], ','))
        v = tuple(extract_numbers(line[1], ','))
        trajectories.append(p1 + v)  # Concatenate tuples

    interceptions = 0
    for i, trajectory in enumerate(trajectories):
        x1, y1, z1, vx1, vy1, vz1 = list(trajectory)

        tmpx, tmpy, = get_second_point(x1, y1, vx1, vy1)
        m1 = get_slope(x1, tmpx, y1, tmpy)
        c1 = get_y_intercept(x1, y1, m1)

        for j in range(i + 1, len(trajectories)):
            x2, y2, z2, vx2, vy2, vz2 = list(trajectories[j])

            tmpx, tmpy, = get_second_point(x2, y2, vx2, vy2)
            m2 = get_slope(x2, tmpx, y2, tmpy)
            c2 = get_y_intercept(x2, y2, m2)

            if m1 == m2:
                continue

            (x, y) = get_intercept_point(c1, m1, c2, m2)
            if (x, y) is not None:
                if min_range <= x <= max_range and min_range <= y <= max_range and is_future(x1, vx1, x2, vx2, x, y):
                    interceptions += 1

                    print(x1, "\n", trajectories[j])
                    print((x, y))
                    print()

                    # plot_two_lines(m1, c1, m2, c2, (min_range, max_range))

    print(interceptions)


def main():
    # filename = "data/simple.txt"
    filename = "data/hard.txt"
    challenge_1(filename)


if __name__ == "__main__":
    main()