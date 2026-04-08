import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True

# print the game board
def printBoard(board):
    print("\n")
    # Using f-strings to format the board rows
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

# take player input
def playerInput(board):
    while True:
        inp = input("Enter a number 1-9: ")
        if inp.isdigit():
            inp = int(inp)
            if 1 <= inp <= 9 and board[inp-1] == "-":
                board[inp-1] = currentPlayer
                break
            else:
                print("Oops, spot already taken or out of range!")
        else:
            print("Invalid input. Please enter a number 1-9.")

# check for win or tie
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

def checkWin(board):
    global gameRunning
    if checkHorizontal(board) or checkRow(board) or checkDiagonal(board):
        printBoard(board)
        # Using f-string for the win message
        print(f"The winner is {winner}!")
        gameRunning = False

def checkTie(board):
    global gameRunning
    if "-" not in board and gameRunning:
        printBoard(board)
        print("It is a tie!")
        gameRunning = False

# switch the player
def switchPlayer():
    global currentPlayer
    currentPlayer = "O" if currentPlayer == "X" else "X"

# def computer(board):
    while currentPlayer == "O" and gameRunning:
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()

# Main Game Loop
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin(board)
    checkTie(board)
    if gameRunning:
        switchPlayer()
        computer(board)
        checkWin(board)
        checkTie(board)