from Coordinates import Coordinates
from SquareBoard import SquareBoard
import re


def checkLeftRightDiagonal(move, board):
    length = board.length
    # if move on left to right diagonal
    if (move.x == move.y):
        #check the left to right diagonal
        previousPos = None
        x = 0
        y = 0
        while x < board.length and y < board.length:
            if previousPos == None:
                previousPos = board.array[x][y]
            elif board.array[x][y] != previousPos or board.array[x][y] == board.empty:
                return False
            x += 1
            y += 1
        return True
    return False

def checkRightLeftDiagonal(move, board):
    length = board.length
    # if move on right to left diagonal
    if (move.x + move.y == length + 1):
        previousPos = None
        x = 0
        y = board.length - 1
        # check the right to left diagonal
        while x < board.length and y >= 0:
            if previousPos == None:
                previousPos = board.array[x][y]
            elif board.array[x][y] != previousPos or board.array[x][y] == board.empty:
                return False
            x += 1
            y -= 1
        return True
    return False

def checkRow(move, board):
    previousPos = None
    for i in range(board.length):
        if previousPos == None:
            previousPos = board.array[move.x-1][i]
        elif board.array[move.x - 1][i] != previousPos or board.array[move.x-1][i] == board.empty:
            return False

    return True

def checkColumn(move, board):
    previousPos = None
    for i in range(board.length):
        if previousPos == None:
            previousPos = board.array[i][move.y - 1]
        elif board.array[i][move.y -1] != previousPos or board.array[i][move.y -1] == board.empty:
            return False

    return True

def endGame(board, lastMove):
    # Check start of the game
    if lastMove == None:
        print(board)
        return False
    # Check if previous move was invalid
    elif lastMove == False:
        return False
    # Check the current status of the game
    elif lastMove != None:
        # Check if 3 in row, column or diagonal
        if checkRow(lastMove, board) or checkColumn(lastMove, board) or checkRightLeftDiagonal(lastMove, board) or checkLeftRightDiagonal(lastMove, board):
            print("\nMove accepted, well done you've won the game!\n")
            print(board)
            return True
        # Check if all places are filled
        elif board.filled == board.length * board.length:
            print("\nMove accepted, both of the players are draw\n")
            print(board)
            return True
        #Continue on with the game
        else:
            print("\nMove accepted, here's the current board:\n")
            print(board)
            return False

    return False


def playGame(board):
    lastMove = None
    regex = r'^[0-9]+,[0-9]+$'

    while endGame(board, lastMove) == False:
        #Check if player one or two turn
        if board.playerOneTurn:
            coordinates = input("Player 1 enter a coord x,y to place your X or enter 'q' to give up: ")
        else:
            coordinates = input("Player 2 enter a coord x,y to place your O or enter 'q' to give up: ")

        #Check if the user wants to quit game
        if coordinates == "q":
            print("Ending game")
            quit()
        #Check if the coordinates are in the valid format
        elif re.match(regex, coordinates) == None:
            print("\nInvalid input. Please try entering your coord again in the format of x,y.\n")
            lastMove = False
        #Continue on with game
        else:
            coordinates = makeCoordinate(coordinates)
            #Check if the coordinates are in the bounds of the board and the current move does not have a piece there already
            if board.checkBounds(coordinates) and board.isEmpty(coordinates):
                board.addPosition(coordinates)
                board.playerOneTurn = not board.playerOneTurn
                lastMove = coordinates
            #Error handling when the coordinates are out of bounds
            elif board.checkBounds(coordinates) == False:
                print("\nOh no, this move is out of bounds! Try again...\n")
                lastMove = False
            #Error handling when the position is already taken
            else:
                print("\nOh no, a piece is already at this place! Try again...\n")
                lastMove = False


def makeCoordinate(coordinates):
    x,y = coordinates.split(",")
    x = int(x)
    y = int(y)

    return Coordinates(x, y)

def startGame():
    print("Welcome to Tic Tac Toe!\n")
    print("Here's the current board:\n")

    playerOneSymbol = "X"
    playerTwoSymbol = "O"
    TicTacToeBoard = SquareBoard(3, playerOneSymbol, playerTwoSymbol)

    playGame(TicTacToeBoard)

startGame()











