# ********************************
# Sudoku Solver using Backtracking
# ********************************

from time import time
# GIVE A BOARD (9x9) INPUT 

print("""
    ***********************************************
    *%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*
    *%%%%                                     %%%%*
    *%%%%      S U D O K U   S O L V E R      %%%%*
    *%%%%          (ONLY 9 x 9 GRID)          %%%%*
    *%%%%                                     %%%%*
    *%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*
    ***********************************************
    """)
def sudoku_checker():

    print("\nPlease enter below the known puzzle elements. The empty cells have to be denoted with '0'\n")

    board_list = []

    # GIVE INPUT PER ROW
    i = 0
    while i in range(9):
        print(f"Enter space separated elements of row {i}")
        try:
            row = [int(x) for x in input().strip().split()]
            board_list.append(row)
            i+=1
            continue
        except:
            break

    # GIVEN A BOARD FIND AN EMPTY SQUARE

    def empty(board):
        for i in range(9):
            for j in range(9):
                if board[i][j]==0:
                    return (i,j) # returns row, col

        return None

    # CHECK VALIDITY OF THE GIVEN BOARD

    def is_valid(board, number, position):

        # check row
        for i in range(9): # could change if puzzle is larger
            if board[position[0]][i] == number and position[1] != i:
                return False

        # check column
        for i in range(9):
            if board[i][position[1]] == number and position[0] != i:
                return False

        # check 3x3 cubes
        x0 = (position[1] //3) * 3
        y0 = (position[0] //3) * 3

        # loop through box
        for i in range(y0, y0 + 3):
            for j in range(x0 ,x0 + 3):
                if board[i][j] == number and (i,j) != position:
                    return False

        return True

    def pydoku(board):

        find = empty(board)
        if not find:
            return True
        else:
            row, col = find

        for i in range(1,10):
            # check if solution is valid
            if is_valid(board, i, (row, col)):
                # add to the board the solution
                board[row][col] = i
                # use solve function recursively 
                if pydoku(board):
                    return True

                board[row][col] = 0
        # if looping through all numbers return an invalid solution
        return False

    # FUNCTION TO PRINT HORIZONTAL AND VERTICAL LINES INSIDE THE BOARD
    def print_board(board):

        for i in range(9):  

            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - ")

            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(board[i][j])
                else:
                    print(str(board[i][j]) + " ", end="")

    while True:
        try:
            print('\nStarting to solve...\n')
            t0 = time()
            pydoku(board_list)
            t1 = time()
            print(f"Solved! Time usage: {t1 - t0:.2f} secs.\n")
            print_board(board_list)
            break
        except:
            print("Something's wrong. Please check your inputs.")
            break

while __name__ == "__main__":

    sudoku_checker()

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
