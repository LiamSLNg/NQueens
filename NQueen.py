from pprint import pprint

global N
N = 8

global usedPos
usedPos = []

#Check if the new position is valid
def is_valid(board, row, col):
    #Check if colomn is on the vertical top
    for i in range(row):
        if board[i][col] == "Q":
            return False
    
    r = row
    c = col
    
    #Check upper left diagonal
    while (r > -1 and c > -1):
        if board[r][c] == "Q":
            return False
        r = r - 1
        c = c - 1
  
    r = row
    c = col
    
    #Check upper right diagonal
    while (r > -1 and c < N):
        if board[r][c] == "Q":
            return False
        r = r - 1
        c = c + 1
    
    if (row, col) in usedPos:
        return False

    return True


def solve_queen(board, row):
    #If all required queens are placed, return True
    if row >= N:
        return True

    #Consider the row and try placing a queen in all the columns one by one
    for i in range (N):
        if is_valid(board, row, i):
            #Place the queen on this board position
            board[row][i] = "Q"
            usedPos.append((row, i))
            #Recursion to place all the remaining Queens
            if solve_queen(board, row + 1):
                return True

            #If this position doesn't work backtrack and do something else
            board[row][i] = "."    
            usedPos.remove((row, i))
    
    #If not all the required Queens can't be placed
    #Then this row should return False
    return False

if __name__ == '__main__':
    example_board = [["."] * N for i in range(N)]
    solutions = 0

    while (solve_queen(example_board, 0)):
        solutions = solutions + 1
        pprint(example_board)
        print("\n")
        example_board = [["."] * N for i in range(N)]

    print(solutions)

