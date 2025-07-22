# pylint: disable=missing-docstring


def sudoku_validator(grid):
    for i in range(9):
        row = set()
        col = set()
        box = set()
        for j in range(9):
            # Check row
            if grid[i][j] != 0:
                if grid[i][j] in row:
                    return False
                row.add(grid[i][j])
            # Check column
            if grid[j][i] != 0:
                if grid[j][i] in col:
                    return False
                col.add(grid[j][i])
            # Check 3x3 box
            box_row = 3 * (i // 3)
            box_col = 3 * (i % 3)
            if grid[box_row + j // 3][box_col + j % 3] != 0:
                if grid[box_row + j // 3][box_col + j % 3] in box:
                    return False
                box.add(grid[box_row + j // 3][box_col + j % 3])
    return True
