class Board:
    def __init__(self, bounds, playerOneSymbol, playerTwoSymbol):
        self.playerOneSymbol = playerOneSymbol
        self.playerTwoSymbol = playerTwoSymbol
        self.playerOneTurn = True
        self.empty = "."
        self.length = bounds
        self.board = self.createBoard()
        self.filled = 0

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

    def addPosition(self, coordinates):
        x = coordinates.x - 1
        y = coordinates.y - 1

        if self.playerOneTurn:
            self.board[x][y] = self.playerOneSymbol
        else:
            self.board[x][y] = self.playerTwoSymbol

        self.filled += 1

    def checkPosition(self, coordinates):
        x = coordinates.x - 1
        y = coordinates.y - 1

        # Check if out of bounds
        if x < 0 or x > self.length - 1 or y < 0 or y > self.length -1:
            return False

        #Check if position already taken
        elif self.board[x][y] != self.empty:
            return False

        return True


