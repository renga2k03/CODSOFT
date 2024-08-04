import random
def checkforWin(board, symbol, opp_symbol, i, j):
    for rows in board:
        if rows[0] == rows[1] == rows[2] == symbol:
            return 10
        elif rows[0] == rows[1] == rows[2] == opp_symbol:
            return -10
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == symbol:
            return 10
        elif board[0][col] == board[1][col] == board[2][col] == opp_symbol:
            return -10
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        return 10
    elif board[0][0] == board[1][1] == board[2][2] == opp_symbol:
        return -10
    if board[0][2] == board[1][1] == board[2][0] == symbol:
        return 10
    elif board[0][2] == board[1][1] == board[2][0] == opp_symbol:
        return -10
    
    if i > -1 and j > -1:
        if board[i].count(opp_symbol) == 2 and symbol in board[i]:
            return 0.5
        elif board[i].count(symbol) == 2 and opp_symbol in board[i]:
            return -0.5
        if board[0][j] == board[1][j] == opp_symbol and board[2][j] == symbol or board[1][j] == board[2][j] == opp_symbol and board[0][j] == symbol or board[0][j] == board[2][j] == opp_symbol and board[1][j] == symbol:
            return 0.5
        elif board[0][j] == board[1][j] == symbol and board[2][j] == opp_symbol or board[1][j] == board[2][j] == symbol and board[0][j] == opp_symbol or board[0][j] == board[2][j] == symbol and board[1][j] == opp_symbol:
            return -0.5
        if i == j:
            if board[0][0] == board[1][1] == opp_symbol and board[2][2] == symbol or board[1][1] == board[2][2] == opp_symbol and board[0][0] == symbol:
                return 0.5
            elif board[0][0] == board[1][1] == symbol and board[2][2] == opp_symbol or board[1][1] == board[2][2] == symbol and board[0][0] == opp_symbol:
                return -0.5
            if board[0][0] == board[2][2] == opp_symbol and board[1][1] == symbol or board[0][2] == board[2][0] == opp_symbol and board[1][1] == symbol:
                return 0.5
            elif board[0][0] == board[2][2] == symbol and board[1][1] == opp_symbol or board[0][2] == board[2][0] == symbol and board[1][1] == opp_symbol:
                return -0.5
        elif i == 2 and j == 0 or i == 0 and j == 2:
            if board[0][2] == board[1][1] == opp_symbol and board[2][0] == symbol or board[1][1] == board[2][0] == opp_symbol and board[0][2] == symbol:
                return 0.5
            elif board[0][2] == board[1][1] == symbol and board[2][0] == opp_symbol or board[1][1] == board[2][0] == symbol and board[0][2] == opp_symbol:
                return -0.5
    return 0

def isFull(board):
    for rows in board:
        for cols in rows:
            if cols == ' ':
                return False
    return True

def minimax(board, depth, turn, symbol, opp_symbol, i, j):
    val = checkforWin(board, symbol, opp_symbol, i, j)
    if val == 10 or val == -10:
        return val * depth
    if isFull(board):
        return 0
    if turn == "max":
        maxval = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = symbol
                    if val == 0.5:
                        maxval = max(maxval, minimax(board, depth - 0.5, "min", symbol, opp_symbol, i, j))
                    else:
                        maxval = max(maxval, minimax(board, depth - 1, "min", symbol, opp_symbol, i, j))
                    board[i][j] = ' '
        return maxval
    else:
        minval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = opp_symbol
                    if val == -0.5:
                        minval = min(minval, minimax(board, depth - 0.5, "max", symbol, opp_symbol, i, j))
                    else:
                        minval = min(minval, minimax(board, depth - 1, "max", symbol, opp_symbol, i, j))
                    board[i][j] = ' '
        return minval

def ai_move(board, symbol, turns):
    if symbol == 'X':
        opp_symbol = 'O'
    elif symbol == 'O':
        opp_symbol = 'X'
    if symbol == 'X':
        if turns == 0:
            return (1, 1)
        elif turns == 2:
            if board[0][0] == 'O':
                return (2, 2)
            elif board[0][2] == 'O':
                return (2, 0)
            elif board[2][0] == 'O':
                return (0, 2)
            elif board[2][2] == 'O':
                return (0, 0)
            else:
                return random.choice([(0, 0),(0, 2),(2, 0),(2, 2)])
    if symbol == 'O':
        if turns == 1 and board[1][1] == ' ':
            return (1, 1)
        if turns == 3:
            if board[1][1] == 'X' and board[2][2] == 'X' and board[0][0] == 'O' or board[1][1] == 'X' and board[0][0] == 'X' and board[2][2] == 'O':
                if board[0][2] == ' ' and board[2][0] == ' ':
                    return random.choice([(0, 2),(2, 0)])
                if board[0][2] == ' ':
                    return (0, 2)
                elif board[2][0] == ' ':
                    return (2, 0)
            elif board[0][0] == 'X' and board[2][2] == 'X' and board[1][1] == 'O' or board[0][2] == 'X' and board[2][0] == 'X' and board[1][1] == 'O':
                bestmoves = [(0, 1),(1, 0),(1, 2),(2, 1)]
                while True:
                    move = random.choice(bestmoves)
                    if board[move[0]][move[1]] == ' ':
                        break
                return move
            elif board[1][1] == 'X' and board[2][0] == 'X' and board[0][2] == 'O' or board[1][1] == 'X' and board[0][2] == 'X' and board[2][0] == 'O':
                if board[0][0] == ' ' and board[2][2] == ' ':
                    return random.choice([(0, 0),(2, 2)])
                if board[0][0] == ' ':
                    return (0, 0)
                elif board[2][2] == ' ':
                    return (2, 2)
    max = -float('inf')
    maxmove = (-1, -1)
    print("Moves Scores")
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = symbol
                nodeval = minimax(board, 9, "max", symbol, opp_symbol, i, j)
                if max < 90 and checkforWin(board, symbol, opp_symbol, i, j) == 0.5:
                    max = 88
                    maxmove = (i, j)
                    print(i, j, '   ', 88)
                elif nodeval > max:
                    maxmove = (i, j)
                    max = nodeval
                    print(i, j, '   ', nodeval)
                else:
                    print(i, j, '   ', nodeval)
                board[i][j] = ' '
    return maxmove

def print_the_board(board):
    print(" ____________\n")
    for rows in board:
        print("| ", end="")
        for cols in rows:
            print(cols, end=" | ")
        print("\n")
    print(" ____________\n")

board = [[' ', ' ', ' '] , [' ', ' ', ' '] , [' ', ' ', ' ']]
turns = 0
player = input("Enter Player 1 (X) or Player 2 (O) : ")
print_the_board(board)
while turns <= 9:
    if player == "Player 1":
        move_x = input("Enter the coords of your move : ").split()
        move_x = [int(i) for i in move_x]
        board[move_x[0]][move_x[1]] = 'X'
        turns += 1
        print_the_board(board)
        if checkforWin(board, 'X', 'O', -1, -1) == 10:
            print(" ________________________\n")
            print("\t  X wins")
            print(" ________________________\n")
            break
        if checkforWin(board, 'O', 'X', -1, -1) == 10:
            print(" ________________________\n")
            print("\t  O wins")
            break
        if turns == 9:
            print(" ________________________\n")
            print("\t   Draw")
            print(" ________________________\n")
            break
        move_o = ai_move(board, 'O', turns)
        board[move_o[0]][move_o[1]] = 'O'
        turns += 1
        print_the_board(board)
        if checkforWin(board, 'X', 'O', -1, -1) == 10:
            print(" ________________________\n")
            print("\t  X wins")
            print(" ________________________\n")
            break
        if checkforWin(board, 'O', 'X', -1, -1) == 10:
            print(" ________________________\n")
            print("\t  O wins")
            print(" ________________________\n")
            break
    elif player == "Player 2":
        move_x = ai_move(board, 'X', turns)
        board[move_x[0]][move_x[1]] = 'X'
        turns += 1
        print_the_board(board)
        if checkforWin(board, 'X', 'O', -1, -1) == 10:
            print(" ________________________\n")
            print("\t  X wins")
            print(" ________________________\n")
            break
        if checkforWin(board, 'O', 'X', -1, -1) == 10:
            print(" ________________________\n")
            print("\t  O wins")
            print(" ________________________\n")
            break
        if turns == 9:
            print(" ________________________\n")
            print("\t   Draw")
            print(" ________________________\n")
            break
        move_o = input("Enter the coords of your move : ").split()
        move_o = [int(i) for i in move_o]
        board[move_o[0]][move_o[1]] = 'O'
        turns += 1
        if checkforWin(board, 'X', 'O', -1, -1) == 10:
            print(" ________________________\n")
            print("\t  X wins")
            print(" ________________________\n")
            break
        if checkforWin(board, 'O', 'X', -1, -1) == 10:
            print(" ________________________\n")
            print("\t  O wins")
            print(" ________________________\n")
            break
        print_the_board(board)