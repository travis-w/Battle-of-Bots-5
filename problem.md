**Reversi** is a two player board game which is played on a 10X10 grid of cells. Each player has an allocated color, Black ( First Player ) or White ( Second Player ) being conventional. Players take turns placing a stone of their color on a single cell. A player must place a stone on the board, in such a position that there exists at least one straight (horizontal, vertical, or diagonal) occupied line between the new stone and another stone of same color, with one or more contiguous other color stone between them.

<div style="text-align:center"><img src ="https://raw.githubusercontent.com/travis-w/Battle-of-Bots-5/master/reversi.png" /></div>

During a game, any stone of the opponent's color that are in a straight line and bounded by the stone just placed and another stone of the current player's color are turned over to the current player's color. The game will end when the board is completely filled or both the players don't have any move left. At the end of the game the player with majority of stone will win.

We will play it on an 10X10 grid. The top left of the grid is [0, 0] and the bottom right is [9, 9]. The rule is that a cell[i, j] is connected to any of top, left, right, or bottom cell.

__Input__  
The input will be a 10X10 matrix consisting only of 0, 1, 2 or 3. Then another line will follow which will contain a number - 1 or 2 which is your player id.

In the given matrix, top-left is [0, 0] and bottom-right is [9, 9].

In cell[row, column], row increases from top to bottom and column increases from left to right.

The cell marked 0 means it doesn't contain any stones. The cell marked 1 means it contains first player's stone which is Black in color. The cell marked 2 means it contains second player's stone which is white in color. The cell marked 3 means it is a valid place for player whose turn it is.

__Output__  
Print the coordinates of the cell separated by space, where you want to play your move. You must take care that you don't print invalid coordinates. For example, [1 1] might be a valid coordinate in the game play if cell[i,j]=3, but [9 10] will never be. Also if you play an invalid move or your code exceeds the time/memory limit while determining the move, you lose the game.

__Starting state__  
The starting state of the game is the state of the board before the game starts.

0 0 0 0 0 0 0 0 0 0  
0 0 0 0 0 0 0 0 0 0  
0 0 0 0 0 0 0 0 0 0  
0 0 0 0 0 0 0 0 0 0  
0 0 0 0 2 1 0 0 0 0  
0 0 0 0 1 2 0 0 0 0  
0 0 0 0 0 0 0 0 0 0  
0 0 0 0 0 0 0 0 0 0  
0 0 0 0 0 0 0 0 0 0  
0 0 0 0 0 0 0 0 0 0

__First Input__  
This is the input give to the first player at the start of the game.

0 0 0 0 0 0 0 0 0 0  
0 0 0 0 0 0 0 0 0 0  
0 0 0 0 0 0 0 0 0 0  
0 0 0 0 3 0 0 0 0 0  
0 0 0 3 2 1 0 0 0 0  
0 0 0 0 1 2 3 0 0 0  
0 0 0 0 0 3 0 0 0 0  
0 0 0 0 0 0 0 0 0 0  
0 0 0 0 0 0 0 0 0 0  
0 0 0 0 0 0 0 0 0 0  
1

__Scoring__  
The scores are calculated by running tournament of all submissions. Your latest submission will be taken into tournament. Scores are assigned according to the Glicko-2 rating system. For more information and questions, see Bot problem judge.
