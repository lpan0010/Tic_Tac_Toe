# Tic_Tac_Toe
A console based game for knots and crosses

To run this game, you will need to run the Game.py file. 

The implementation details: 

Game.py file is where the game starts. It uses SquareBoard.py to create a instance of a square board by giving it bounds of how large they want the sqaure board to be.

After this, Game.py will call playGame function to start playing the game. 

In this function, there is a loop which will run forever until the game has ended. 

Below I have outlined step by step of what the loop does, 
- Get coordinates from the user
- Check to see if the input is valid format or "q" (I assumed that "q" meant quit the game)
- Check to see if the coordinates are in bounds and not taken up
- Once the coordinates are valid it will then add it to the board

The game can end when either the board is filled, or there is a row, column or diagonal that is filled.

To check if a row, column or diagonal is filled I use the last move that the player has entered and check if that position's row is filled, column is filled and if the position given is on the main diagonal, check if the diagonal is filled. If it meets one of these conditions, then we can end the game.
i.e. Given a move of 1,1. I would check if row 1 is filled with same symbols, then check if column 1 is filled with same symbols. Then check if 1,1 is on a diagonal, then check the whole diagonal.


