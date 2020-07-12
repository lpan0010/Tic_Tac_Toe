class SquareBoard:
    def __init__(self, bounds, playerOneSymbol, playerTwoSymbol):
        self.playerOneSymbol = playerOneSymbol
        self.playerTwoSymbol = playerTwoSymbol
        self.playerOneTurn = True
        self.empty = "."
        self.length = bounds
        self.array = self.createBoard()
        self.filled = 0

    def __str__(self):
        boardString = ""
        for x in range(self.length):
            rowString = ""
            for y in range(self.length):
                rowString += self.array[x][y] + " "
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

    def addPosition(self, coordinates):
        x = coordinates.x - 1
        y = coordinates.y - 1

        #Checks to see if it is player one turn
        if self.playerOneTurn:
            self.array[x][y] = self.playerOneSymbol
        else:
            self.array[x][y] = self.playerTwoSymbol

        self.filled += 1

    def checkBounds(self, coordinates):
        x = coordinates.x - 1
        y = coordinates.y - 1

        # Check if out of bounds
        if x < 0 or x > self.length - 1 or y < 0 or y > self.length -1:
            return False

        return True
    def isEmpty(self, coordinates):
        x = coordinates.x - 1
        y = coordinates.y - 1

        # Check if position already taken
        if self.array[x][y] != self.empty:
            return False

        return True
