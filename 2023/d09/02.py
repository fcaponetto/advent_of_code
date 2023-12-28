import sys

sys.path.append('..')
from utils import *


def challenge_1(filename: str):
    lines = readfile(filename)

    histories = []
    for line in lines:
        line = extract_numbers(line)
        histories.append(line)

    differences = {}
    output = 0
    for history in histories:
        level = 1
        differences[level-1] = history
        res = 0
        while history:
            diff = [history[i] - history[i - 1] for i in range(1, len(history))]
            differences[level] = diff

            if all(d == 0 for d in diff):
                break

            history = diff
            level += 1

        while level >= 0:
            res = differences[level][0] - res
            level -= 1

        output += res

    print(output)



def main():
    # filename = "data/simple.txt"
    filename = "data/challenge.txt"
    challenge_1(filename)


if __name__ == "__main__":
    main()
