# Write your solution here
import copy
def print_sudoku(sudoku: list):
    for i, row in enumerate(sudoku):
        for j, num in enumerate(row):
            print("_" if num == 0 else num, end=" ")
            if (j + 1) % 3 == 0 and j != 8:
                print(" ", end="")  # Extra space between 3-column blocks
        print()
        if (i + 1) % 3 == 0 and i != 8:
            print()  # Extra newline between 3-row blocks

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    new_sudoku = []
    new_sudoku = copy.deepcopy(sudoku)
    new_sudoku[row_no][column_no] = number
    return new_sudoku
    



if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)
