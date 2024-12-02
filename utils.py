def readfile(filename: str):
    with open(filename) as file:
        return [line.strip() for line in file.readlines()]


def split_line(line: str, delimiter: str) -> list:
    return line.strip().split(delimiter)


def extract_numbers(line: str, delimiter: str = None) -> list:
    """
    Extracts integers from a given string, splitting it by a specified delimiter.

    If no delimiter is specified, the function defaults to splitting the string
    by any whitespace (spaces, tabs, etc.).

    Args:
        line (str): The input string containing numbers.
        delimiter (str, optional): The delimiter used to split the string.
            - If `None`, the string is split by whitespace.

    Returns:
        list: A list of integers extracted from the input string.

    Examples:
        >>> extract_numbers("1 2 3")
        [1, 2, 3]

        >>> extract_numbers("4,5,6", ",")
        [4, 5, 6]

        >>> extract_numbers(" 7   8  9  ")
        [7, 8, 9]

        >>> extract_numbers("10|20|30", "|")
        [10, 20, 30]

        >>> extract_numbers("")
        []

        >>> extract_numbers("   ")
        []

    Notes:
        - The function trims any extra whitespace around each split element.
        - Raises a ValueError if any split element cannot be converted to an integer.
    """
    line = line.split(delimiter)  # Split the string using the specified delimiter
    return list(map(int, map(str.strip, line)))  # Strip whitespace and convert to integers


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



