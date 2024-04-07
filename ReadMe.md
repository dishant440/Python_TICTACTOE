# Tic Tac Toe Game

This is a simple implementation of the classic game Tic Tac Toe in Python. The game allows two players to take turns marking spaces on a 3x3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game. If all spaces are filled without any player achieving a winning condition, the game ends in a tie.

## How to Play

1. Run the script.
2. Enter the name of Player 1 (e.g., "dishant") 
3. Enter the name of Player 2 (e.g., "joey")
4. Players take turns entering positions on the board by inputting a number from 1 to 9.
5. The game will continue until one player wins or until all spaces on the board are filled (resulting in a tie).


### Board Class

The `Board` class represents the game board. It has the following methods:

- `__init__()`: Initializes the game board with empty cells.
- `display()`: Displays the current state of the board.
- `mark_cell(position, mark)`: Marks a cell on the board with the specified mark.
- `is_cell_empty(position)`: Checks if a cell on the board is empty.
- `check_winner(mark)`: Checks if the specified player's marks form a winning combination on the board.

### Player Class

The `Player` class represents a player in the game. It has the following methods:

- `__init__(name, mark)`: Initializes the player with a name and a mark ('X' or 'O').
- `make_move(board)`: Allows the player to make a move by inputting a position on the board.

### playGame() Function

The `playGame()` function sets up the game by creating a board and two players. It then loops through the game process, displaying the board, allowing each player to make a move, and checking for a winner or a tie. The game ends when a player wins or when all cells on the board are filled.

## Example Usage

```python
playGame()
```

This will start the game, allowing two players to take turns playing Tic Tac Toe.

## Note

- This implementation assumes valid user inputs and does not include extensive error handling. Players are expected to input valid positions within the range of 1 to 9.
- The game does not include any AI opponent; it is designed for two human players.