from Coordinates import Coordinates
from Board import Board

def endGame(board):
    #Check if 3 in row

    #Check if all places are filled
    if board.filled == board.length * board.length:
        return True

    return False


def playGame(board):
    while endGame(board) == False:
        # coordinates = ""
        if board.playerOneTurn:
            coordinates = input("Player 1 enter a coord x,y to place your X or enter 'q' to give up: ")
        else:
            coordinates = input("Player 2 enter a coord x,y to place your X or enter 'q' to give up: ")

        coordinates = makeCoordinate(coordinates)
        if board.checkPosition(coordinates):
            print("\nMove accepted, here's the current board:\n")
            board.addPosition(coordinates)
            board.playerOneTurn = not board.playerOneTurn
            print(board)
        else:
            print("\nMove not accepted, please pick another one\n")


def makeCoordinate(coordinates):
    x,y = coordinates.split(",")
    x = int(x)
    y = int(y)

    return Coordinates(x, y)


print("Welcome to Tic Tac Toe!\n")
print("Here's the current board:\n")

playerOneSymbol = "X"
playerTwoSymbol = "O"
TicTacToeBoard = Board(3, playerOneSymbol, playerTwoSymbol)

print(TicTacToeBoard)

playGame(TicTacToeBoard)











