import sys
sys.path.append('..')
from utils import *

reference = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def challenge_1(filename):
    lines = readfile(filename)

    cubes_in_game = {}

    for line in lines:
        game_bags = split_line(line, ':')
        game_id = game_bags[0].split()[-1]
        bags = split_line(game_bags[1], ';')

        cubes_in_game[game_id] = {
            'red': 0,
            'green': 0,
            'blue': 0
        }

        for bag in bags:
            numbers_colors = split_line(bag, ',')
            for number_color in numbers_colors:
                number_color = split_line(number_color, ' ')
                # if the color of the cubes in the subset is greater than the previous subset,
                # then update it
                if int(number_color[0]) > cubes_in_game[game_id][number_color[1]]:
                    cubes_in_game[game_id][number_color[1]] = int(number_color[0])

    output = 0
    for game_id, colors in cubes_in_game.items():
        if not any(colors[color] > reference[color] for color in reference):
            output += int(game_id)
    print(output)


# f = "data/simple.txt"
f = "data/challenge.txt"
challenge_1(f)
