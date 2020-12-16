# solver.py

def solve(board):

    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if validate(board, i, (row, col)):
            board[row][col] = i
            
            if solve(board):
                return True

            board[row][col] = 0
    
    return False


def validate(board, val, pos):

    # row validation
    for i in range(len(board[0])):
        if board[pos[0]][i] == val and pos[1] != i:
            return False
    
    # col validation
    for i in range(len(board)):
        if board[i][pos[1]] == val and pos[0] != i:
            return False

    """ quadrant verification part, graph below should help w math conceptualization
              |           |          
       0,0    |   0,1     |    0,2    
              |           |           
     --------------------------------
              |           |    
       1,0    |    1,1    |    1,2    
              |           |   
     --------------------------------
              |           |    
       2,0    |    2,1    |    2,2    
              |           |   
    """

    x_quad = pos[1] // 3
    y_quad = pos[0] // 3

    for i in range(y_quad * 3, y_quad * 3 + 3):

        for c in range(x_quad * 3, x_quad * 3 + 3):
            
            if board[i][c] == val and (i,c) != pos:
                return False

    # if we reach this, we're good
    return True

def print_board(board):

    #goes through board array
    for i in range(len(board)):
        row = board[i]
        if ((i % 3 == 0) & ((i != 0) & (i != 0))):
            print("--------------------------------")
        
        # iterates each individual row
        for c in range(len(row)):
            
            # only true every third column, and not at the end of the puzzle (8th column)
            if (((c+1) % 3 == 0) & (c != 8)):
                print(row[c], " | ", end=" ")
            else:
                print(row[c], end="  ")

        print()


#searches for first 0 in the board, returns tuple of location
def find_empty(board):

    for row in range(len(board)):
        
        for col in range(len(board[0])):
            if (board[row][col] == 0):
                return (row, col)

    #only returns None when board is solved
    return None