from utils import *


def count_x_mas(filename: str):
    # Read and prepare the grid
    with open(filename) as f:
        puzzle = [line.strip() for line in f.readlines()]

    ROWS = len(puzzle)
    COLS = len(puzzle[0])
    target = "MAS"

    def check_diagonal(x, y, dx, dy):
        # Check if a diagonal matches "MAS" in forward or backward
        forward_match = True
        backward_match = True
        for i in range(3):  # Length of "MAS"
            nx, ny = x + i * dx, y + i * dy
            if not (0 <= nx < ROWS and 0 <= ny < COLS):
                return False, False
            if puzzle[nx][ny] != target[i]:
                forward_match = False
            if puzzle[nx][ny] != target[2 - i]:  # Reverse "MAS"
                backward_match = False
        return forward_match, backward_match

    total_count = 0

    # Iterate over each cell to find potential centers
    for r in range(1, ROWS - 1):  # Exclude edges
        for c in range(1, COLS - 1):  # Exclude edges
            if puzzle[r][c] == "A":  # Center of the X
                # Check diagonals
                tl_br_fw, tl_br_bw = check_diagonal(r - 1, c - 1, 1, 1)  # Top-left to bottom-right
                tr_bl_fw, tr_bl_bw = check_diagonal(r - 1, c + 1, 1, -1)  # Top-right to bottom-left

                # Count valid X-MAS patterns
                if (tl_br_fw or tl_br_bw) and (tr_bl_fw or tr_bl_bw):
                    total_count += 1

    print("Total X-MAS occurrences:", total_count)


# data = 'data/simple2.txt'
data = 'data/input.txt'
# challenge(data)
count_x_mas(data)