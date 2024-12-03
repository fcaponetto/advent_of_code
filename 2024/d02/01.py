from utils import *


def check_array_trend(array):
    if all(array[i] <= array[i + 1] for i in range(len(array) - 1)):
        return True
    elif all(array[i] >= array[i + 1] for i in range(len(array) - 1)):
        return True
    else:
        return False


def is_safe_report(report):
    """Check if a report is safe using the original rules."""
    if not check_array_trend(report):
        return False

    previous = report[0]
    for level in report[1:]:
        if abs(level - previous) > 3 or abs(level - previous) < 1:
            return False
        previous = level

    return True


def challenge(filename: str):
    lines = readfile(filename)

    reports = []
    for line in lines:
        values = extract_numbers(line)
        reports.append(values)

    total_safe = 0
    for report in reports:
        if is_safe_report(report):
            total_safe += 1

    print(total_safe)


# data = 'data/simple.txt'
data = 'data/input.txt'
challenge(data)
