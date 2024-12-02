from utils import *


def challenge(filename: str):
    lines = readfile(filename)

    locIDs1 = []
    locIDs2 = []
    for line in lines:
        values = extract_numbers(line)
        locIDs1.append(values[0])
        locIDs2.append(values[1])

    locIDs1.sort()
    locIDs2.sort()

    total_distance = 0
    for i in range(len(locIDs1)):
        total_distance += abs(locIDs1[i] - locIDs2[i])

    print(total_distance)


# data = 'data/simple.txt'
data = 'data/input.txt'
challenge(data)
