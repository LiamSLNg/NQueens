from pprint import pprint

#Check if the new position is valid
def is_valid(board, row, col):
    #Check if colomn is on the vertical top
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    r = row
    c = col
    
    #Check upper left diagonal
    while (r > -1 and c > -1):
        if board[r][c] == 1:
            return False
        r = r - 1
        c = c - 1
  
    r = row
    c = col
    
    #Check upper right diagonal
    while (r > -1 and c < 4):
        if board[r][c] == 1:
            return False
        r = r - 1
        c = c + 1
    
    return True


def solve_queen(board, row):
    #If all required queens are placed, return True
    if row >= 4:
        return True

    #Consider the row and try placing a queen in all the columns one by one
    for i in range (4):
        if is_valid(board, row, i):

            #Place the queen on this board position
            board[row][i] = 1

            #Recursion to place all the remaining Queens
            if solve_queen(board, row + 1):
                return True

            #If this position doesn't work backtrack and do something else
            board[row][i] = -1    
    
    #If not all the required Queens can't be placed
    #Then this row should return False
    return False


if __name__ == '__main__':
    example_board = [
        [-1, -1, -1, -1],
        [-1, -1, -1, -1],
        [-1, -1, -1, -1],
        [-1, -1, -1, -1]
    ]
    print(solve_queen(example_board, 0))
    pprint(example_board)
