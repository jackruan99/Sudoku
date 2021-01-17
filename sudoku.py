import time

def solve_sudoku(board):
    return solve_helper(0, 0, board)
            

def solve_helper(row_number, col_number, board):
    if board[row_number][col_number] == 0:
        for value in range(1,10):
            if check_box(value, row_number, col_number, board):
                board[row_number][col_number] = value
                if col_number == 8 and row_number == 8:
                    return True
                elif col_number == 8:
                    if solve_helper(row_number+1, 0, board):
                        return True
                    else:
                        board[row_number][col_number] = 0
                else:
                    if solve_helper(row_number, col_number+1, board):
                        return True
                    else:
                        board[row_number][col_number] = 0
    else:
        if col_number == 8 and row_number == 8:
            return True
        elif col_number == 8:
            if solve_helper(row_number+1, 0, board):
                return True
        else:
            if solve_helper(row_number, col_number+1, board):
                return True
    
    return False

# checks if the value can be placed in the give box
def check_box(value, row_number, col_number, board):
    # checks if the value is already in the given row
    for col in range(9):
        if value == board[row_number][col]:
            return False

    # checks if the value is already in the given column
    for row in range(9):
        if value == board[row][col_number]:
            return False

    # checks if the value is already in the 3x3 grid it's in
    row_start = row_number // 3 * 3
    col_start = col_number // 3 * 3
    for i in range(3):
        for j in range(3):
            if value == board[row_start+i][col_start+j]:
                return False
    
    return True

# print the board with grid
def print_sudoku(board):
    print("-"*37)
    for i, row in enumerate(board):
        print(("|" + " {}   {}   {} |"*3).format(*[x if x != 0 else " " for x in row]))
        if i == 8:
            print("-"*37)
        elif i % 3 == 2:
            print("|" + "---+"*8 + "---|")
        else:
            print("|" + "   +"*8 + "   |")


# This is considered to be the hardest Sudoku puzzle
board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 3, 0, 0, 9, 0, 0],
            [0, 0, 1, 0, 8, 0, 0, 0, 2],
            [6, 0, 0, 0, 0, 4, 0, 0, 0],
            [3, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 4, 0, 0, 0, 0, 0, 0, 7],
            [0, 0, 7, 0, 0, 0, 3, 0, 0]]

# prints the unsolved board
print('Sudoku Puzzle:')
print_sudoku(board) 

# solves the puzzle
start = time.time()
solve_sudoku(board)
end = time.time()

# prints the solution board
print('Solution:')
print_sudoku(board) 

# prints the time the programs takes to solve the puzzle
print(f'Solved in: {end - start:.2f} seconds.')