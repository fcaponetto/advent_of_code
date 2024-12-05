from utils import *

word = "XMAS"

def challenge(filename: str):
    # Read the file
    lines = open(filename).readlines()

    # Prepare the grid
    puzzle = [line.strip() for line in lines]
    ROWS = len(puzzle)
    COLS = len(puzzle[0])
    word = "XMAS"
    word_len = len(word)

    # Depth-first search (DFS) function
    def dfs(r, c, i):
        if i == word_len:  # Found the full word
            return 1

        if (r < 0 or c < 0 or
            r >= ROWS or c >= COLS or
            puzzle[r][c] != word[i]):
            return 0

        # Temporarily mark the cell as visited
        original = puzzle[r][c]
        puzzle[r] = puzzle[r][:c] + "#" + puzzle[r][c+1:]

        # Explore all 8 directions
        count = (
            dfs(r, c+1, i+1) +  # Right
            dfs(r-1, c+1, i+1) +  # Up-Right
            dfs(r-1, c, i+1) +  # Up
            dfs(r-1, c-1, i+1) +  # Up-Left
            dfs(r, c-1, i+1) +  # Left
            dfs(r+1, c-1, i+1) +  # Down-Left
            dfs(r+1, c, i+1) +  # Down
            dfs(r+1, c+1, i+1)  # Down-Right
        )

        # Restore the original character after visiting
        puzzle[r] = puzzle[r][:c] + original + puzzle[r][c+1:]

        return count

    # Count all occurrences
    total_count = 0
    for r in range(ROWS):
        for c in range(COLS):
            if puzzle[r][c] == word[0]:  # Match first letter
                total_count += dfs(r, c, 0)

    print(total_count)



def count_xmas_occurrences(filename: str):
    lines = readfile(filename)

    grid = []
    for line in lines:
        grid.append(line.strip())

    rows, cols = len(grid), len(grid[0])
    target = "MAS"
    directions = [
        (0, 1),  # Horizontal right
        (0, -1),  # Horizontal left
        (1, 0),  # Vertical down
        (-1, 0),  # Vertical up
        (1, 1),  # Diagonal down-right
        (-1, -1),  # Diagonal up-left
        (1, -1),  # Diagonal down-left
        (-1, 1)  # Diagonal up-right
    ]

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def find_word(x, y, dx, dy):
        for k in range(len(target)):
            nx, ny = x + k * dx, y + k * dy
            if not is_valid(nx, ny) or grid[nx][ny] != target[k]:
                return False
        return True

    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'M':  # Potential start of "XMAS"
                for dx, dy in directions:
                    if find_word(i, j, dx, dy):
                        count += 1
    print(count)



data = 'data/simple.txt'
# data = 'data/input.txt'
# challenge(data)
count_xmas_occurrences(data)