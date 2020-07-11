from Coordinates import Coordinates

class Board:
    def __init__(self, bounds):
        self.X = "X"
        self.O = "O"
        self.empty = "."
        self.length = bounds
        self.board = self.createBoard()

    def __str__(self):
        boardString = ""
        for x in range(self.length):
            rowString = ""
            for y in range(self.length):
                rowString += self.board[x][y] + " "
            boardString += rowString + "\n"
        return boardString

    def createBoard(self):
        board = []
        for x in range(self.length):
            row = []
            for y in range(self.length):
                row.append(self.empty)
            board.append(row)
        return board

    def addPosition(self, coordinates ,isX):
        x = coordinates.x - 1
        y = coordinates.y - 1
        if isX:
            self.board[x][y] = self.X
        else:
            self.board[x][y] = self.O

    def checkPosition(self, coordinates):
        #Check if out of bounds
        x = coordinates.x - 1
        y = coordinates.y - 1
        if x < 0 or x > self.length - 1 or y < 0 or y > self.length -1:
            return False
        #Check if position already taken
        elif self.board[x][y] != self.empty:
            return False

        return True


