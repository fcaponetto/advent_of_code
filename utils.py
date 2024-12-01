def readfile(filename: str):
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]


def split_line(line: str, delimiter: str) -> list:
    return line.strip().split(delimiter)


def extract_numbers(line: str) -> list:
    return list(map(int, map(str.strip, line)))


def extract_numbers(line: str, delimiter: str) -> list:
    line = line.split(delimiter)
    return list(map(int, map(str.strip, line)))


def extract_and_combine_numbers(line: str) -> int:
    return int("".join(str(element) for element in extract_numbers(line)))


def make_char_matrix(filename: str) -> [[str]]:
    """
    Read input as a matrix.
    Split each line into chars.
    Example:
    abc
    def
    returns [['a', 'b', 'c'], ['d', 'e', 'f']]
    """
    lines = readfile(filename)
    return [list(x) for x in lines]


def print_matrix(matrix: str):
    for row in matrix:
        print(row)


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


# Function to rotate the matrix 90 degrees clockwise
def rotate_clockwise(mat):
    transposed = transpose(mat)
    return [list(reversed(col)) for col in transposed]


# Function to rotate the matrix 90 degrees counterclockwise
def rotate_counterclockwise(mat):
    # Transposing the matrix
    transposed = transpose(mat)
    # Reversing each row in the transposed matrix
    return transposed[::-1]



