from utils import *


def challenge(filename: str):
    lines = readfile(filename)

    locIDs = []
    occurences = []
    for line in lines:
        values = extract_numbers(line)
        locIDs.append(values[0])
        occurences.append(values[1])

    similarity_score = 0
    for id in locIDs:
        similarity_score += id * occurences.count(id)

    print(similarity_score)


# data = 'data/simple.txt'
data = 'data/input.txt'
challenge(data)