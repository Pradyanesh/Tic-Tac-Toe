import random
def displayBoard(board):
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   ' + board[0][0] + '   |   ' + board[0][1] + '   |   ' + board[0][2] + '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   ' + board[1][0] + '   |   ' + board[1][1] + '   |   ' + board[1][2] + '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   ' + board[2][0] + '   |   ' + board[2][1] + '   |   ' + board[2][2] + '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')

def enterMove(board):
    while True:
        move = int(input("Enter your move: "))
        if move<1 or move>9:
            print("Enter a valid move!")
            continue
        elif str(move) not in board[0] and str(move) not in board[1] and str(move) not in board[2]:
            print("The place is already taken!")
            continue
        else:
            for i in range(3):
                for j in range(3):
                    if str(move) == board[i][j]:
                        board[i][j] = 'O'
                        break
            break
        break

def makeListOfFreeFields(board):
    global free
    free = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X' or board[i][j] == 'O':
                pass
            else:
                free.append((i, j))
    for i, j in free:
        if numberOfMoves < 9:
            print(board[i][j], sep = ',', end = ' ')

def victoryFor(board, sign):
    if numberOfMoves < 9:
        if sign == "O":
            print("Checking to see if you are the winner....")
        else:
            print("Checking to see if computer is the winner....")
    
    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
        return True
    elif board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
        return True
    elif board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
        return True
    elif board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
        return True
    elif board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
        return True
    elif board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
        return True
    elif board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    elif board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True
    else:
        if numberOfMoves < 9:
            print("We do not have a winner yet!")

def drawMove(board):
    while True:
        i = random.randrange(3)
        j = random.randrange(3)
        if (i, j) in free:
            board[i][j] = "X"
            break
        else:
            continue


board = [['1', '2', '3'], ['4', 'X', '6'], ['7', '8', '9']]
numberOfMoves = 1
human = "O"
computer = "X"

print("Welcome to TIC TAC TOE!!!")
displayBoard(board)
print()
while numberOfMoves<9:
    enterMove(board)
    numberOfMoves += 1
    displayBoard(board)
    if victoryFor(board, human) == True:
        print("You defeated the computer!!! VICTORY!!!")
        break
    else:
        print("Here is the list of free spaces")
        makeListOfFreeFields(board)
        print()
    print()
    
    print("Computer's Move:")
    drawMove(board)
    numberOfMoves += 1
    displayBoard(board)
    print()

    if victoryFor(board, computer) == True:
        print("The computer has outsmarted you!!! Better luck next time!!!")
        break
    else:
        print("Here is the list of free spaces")
        makeListOfFreeFields(board)
        print()
    print()
else:
    if numberOfMoves >= 9:
        print("It's a TIE!!! Please play again!")


