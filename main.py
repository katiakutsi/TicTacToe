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

        # ყოველი სიმბოლოს ჩასმისას ვამოწმებთ ფრე ხომ არ არის უკვე ან რომელიმე მოთამაშემ ხომ არ მოიგო
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
    # რადგან minimax ფუნქცია რეკურსიულია გვჭირდება პირობა რომლის შემდეგაც ფუნცია დაასრულებს მუშაობას
    # ანუ თუ რომელიმე მოთამაშე მოიგებს ან თუ ფრე იქნება
    if checkWhichMarkWin(computer):
        return 100
    elif checkWhichMarkWin(player):
        return -100
    elif checkForDraw():
        return 0

    # ვამოწმებთ მოთამაშე მინიმიზაციას აკეთებს თუ მაქსიმიზაციას
    # ამ მეთოდში ხდება იგივე რაც computerMove() მეთოდში გამოკლებით იმისა რომ
    # აქ არ ხდება დამახსოვრება პოზიციის
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

    # გადავივლით დაფის ყველა პოზიციაზე
    for key in board.keys():
        # და ვამოწმებთ თუ შეუვსებელია ეს პოზიცია
        if(board[key] == ' '):
            # თუ შეუვსებელია მაშინ დროებით ვავსებთ X-ით
            board[key] = computer
            # ვითვლით შეფასებას ამ პოზიციით შევსებისთვის
            score = minimax(board, False)
            # ვასუფთავებთ ისევ პოზიციას და
            board[key] = ' '
            # თუ მიმდინარე შეფასება მეტია საუკეთესო შეფასებაზე მაშინ ვინახავთ საუკეთესო შეფასებას და
            # მის პოზიციას
            if score > bestScore:
                bestScore = score
                bestMove = key

    # მას შემდეგ რაც ციკლი მორჩება მუშაობას გვექნება უკვე საუკეთესო პოზიცია ახალი სვლისთვის
    insertLetter(computer, bestMove)
    return


printBoard(board)

# სანამ მოგებული არცერთი მოთამაშეა თამაშობს კომპიუტერი, შემდეგ მოთამაშე
while not checkForWin():
    computerMove()
    playerMove()