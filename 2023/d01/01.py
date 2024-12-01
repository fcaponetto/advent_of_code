from utils import *


def challenge_1(filename: str):
    lines = readfile(filename)

    output = 0
    for line in lines:
        i = 0
        j = len(line) - 1

        two_digits = [0, 0]
        found1, found2 = False, False

        while not found1 or not found2:
            if not line[i].isnumeric():
                i += 1
            elif not found1:
                found1 = True
                two_digits[0] = (line[i])

            if not line[j].isnumeric():
                j -= 1
            elif not found2:
                found2 = True
                two_digits[1] = line[j]
        curr = (int(str(two_digits[0]) + str(two_digits[1])))
        output += curr

    print(output)


filename1 = "data/challenge1.txt"
challenge_1(filename1)
