player = 'O'
computer = 'X'
board = {
    1: ' ',
    2: ' ',
    3: ' ',
    4: ' ',
    5: ' ',
    6: ' ',
    7: ' ',
    8: ' ',
    9: ' ',
}

def printBoard(board):
    for key in board.keys():
        straightLine = '|'
        if key % 3 == 0:
            straightLine = ''

        print(board[key] + straightLine, end='')

        if key % 3 == 0:
            print('')

def spaceIsFree(position):
    return board[position] == ' '


def checkForDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True

def checkForWin():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False

def checkWhichMarkWin(mark):
    if (board[1] == board[2] and board[1] == board[3] and board[1] == mark):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False

def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)

        if(checkForDraw()):
            print('Draw')
            return

        if(checkForWin()):
            if letter == 'X':
                print('Computer wins')
            else:
                print('You win')

    else:
        print('Cant insert')
        position = int(input('Enter new position: '))
        insertLetter(letter, position)

def playerMove():
    position = int(input('Enter the position for O: '))
    insertLetter(player, position)
    return


def minimax(board, isMaximizing):
    if checkWhichMarkWin(computer):
        return 100
    elif checkWhichMarkWin(player):
        return -100
    elif checkForDraw():
        return 0

    if isMaximizing:
        bestScore = -1000

        for key in board.keys():
            if (board[key] == ' '):
                board[key] = computer
                score = minimax(board, False)
                board[key] = ' '
                if score > bestScore:
                    bestScore = score
        return bestScore

    else:
        bestScore = 1000

        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                score = minimax(board, True)
                board[key] = ' '
                if score < bestScore:
                    bestScore = score
        return bestScore

def computerMove():
    # ეს რიცხვები პირობითია
    bestScore = -1000
    bestMove = 0


    for key in board.keys():
        if(board[key] == ' '):
            board[key] = computer
            score = minimax(board, False)
            board[key] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = key

    insertLetter(computer, bestMove)
    return


printBoard(board)

# სანამ მოგებული არცერთი მოთამაშეა თამაშობს კომპიუტერი, შემდეგ მოთამაშე
while not checkForWin():
    computerMove()
    playerMove()