import sys

sys.path.append('..')
from utils import *


def challenge_1(filename: str):
    lines = readfile(filename)

    cards = []

    for line in lines:
        line = split_line(line, ":")[-1]
        numbers = split_line(line, "|")
        winning = extract_numbers(numbers[0])
        play = extract_numbers(numbers[1])
        cards.append([set(winning), set(play)])

    output = 0
    tmp = 1
    for card in cards:
        # the intersection method is used to find the common elements between the two sets.
        matches = card[0].intersection(card[1])

        for i in range(1, len(matches)):
            tmp += 1 * (2 ** (i-1))

        if matches:
            output += tmp
            tmp = 1

    print(output)


f = "data/simple.txt"
# f = "data/challenge.txt"
challenge_1(f)
