class TicTacToeFIFO:
    def __init__(self):
        # Initialize a 3x3 board with empty spaces
        self.board = [[" " for _ in range(3)] for _ in range(3)]

        # Dictionary to track each player's moves in order (FIFO)
        self.moves = {"X": [], "O": []}

        # Start the game with player "X"
        self.current_player = "X"

    def display_board(self):
        # Display the current state of the board
        for row in self.board:
            print("|".join(row))  # Print cells in the row separated by '|'
            print("-" * 5)        # Separator line between rows

    def make_move(self, row, col):
        # Reject the move if the cell is already occupied
        if self.board[row][col] != " ":
            print("Cell already taken!")
            return False

        # Enforce FIFO: if player already has 3 marks, remove the oldest one
        if len(self.moves[self.current_player]) == 3:
            old_row, old_col = self.moves[self.current_player].pop(0)
            self.board[old_row][old_col] = " "  # Clear the oldest mark

        # Place the current player's mark
        self.board[row][col] = self.current_player

        # Record the new move
        self.moves[self.current_player].append((row, col))

        # Display the updated board
        self.display_board()

        # Check if the current player has won
        if self.check_win(self.current_player):
            print(f"Player {self.current_player} wins!")
            return True  # End the game

        # Switch to the other player
        self.current_player = "O" if self.current_player == "X" else "X"
        return False  # Continue the game

    def check_win(self, player):
        
        b = self.board

        # Check all rows and columns for a winning line
        for i in range(3):
            if all(b[i][j] == player for j in range(3)):  # Row match
                return True
            if all(b[j][i] == player for j in range(3)):  # Column match
                return True

        # Check both diagonals for a win
        if all(b[i][i] == player for i in range(3)):  # Top-left to bottom-right
            return True
        if all(b[i][2 - i] == player for i in range(3)):  # Top-right to bottom-left
            return True

        # No win found
        return False


# Start the game
game = TicTacToeFIFO()
game.display_board()  # Show the empty board

# Main game loop
while True:
    try:
        # Ask the current player to input their move
        row = int(input(f"Player {game.current_player}, enter row (0-2): "))
        col = int(input(f"Player {game.current_player}, enter col (0-2): "))

        # Process the move; if it returns True, someone has won
        if game.make_move(row, col):
            break  # End the game loop
    except (ValueError, IndexError):
        # Handle invalid inputs
        print("Invalid input. Please enter numbers between 0 and 2.")
        
'''

Output:

 | | 
-----
 | | 
-----
 | | 
-----
Player X, enter row (0-2): 1
Player X, enter col (0-2): 1
 | | 
-----
 |X| 
-----
 | | 
-----
Player O, enter row (0-2): 0
Player O, enter col (0-2): 0
O| | 
-----
 |X| 
-----
 | | 
-----
Player X, enter row (0-2): 1
Player X, enter col (0-2): 2
O| | 
-----
 |X|X
-----
 | | 
-----
Player O, enter row (0-2): 1    
Player O, enter col (0-2): 0
O| | 
-----
O|X|X
-----
 | | 
-----
Player X, enter row (0-2): 2
Player X, enter col (0-2): 0
O| | 
-----
O|X|X
-----
X| | 
-----
Player O, enter row (0-2): 0
Player O, enter col (0-2): 2
O| |O
-----
O|X|X
-----
X| | 
-----
Player X, enter row (0-2): 0
Player X, enter col (0-2): 1
O|X|O
-----
O| |X
-----
X| | 
-----
Player O, enter row (0-2): 1
Player O, enter col (0-2): 1
 |X|O
-----
O|O|X
-----
X| | 
-----
Player X, enter row (0-2): 1
Player X, enter col (0-2): 2
Cell already taken!
Player X, enter row (0-2): 2
Player X, enter col (0-2): 2
 |X|O
-----
O|O| 
-----
X| |X
-----
Player O, enter row (0-2): 1
Player O, enter col (0-2): 2
 |X|O
-----
 |O|O
-----
X| |X
-----
Player X, enter row (0-2): 2
Player X, enter col (0-2): 1
 |X|O
-----
 |O|O
-----
 |X|X
-----
Player O, enter row (0-2): 1
Player O, enter col (0-2): 0
 |X| 
-----
O|O|O
-----
 |X|X
-----
Player O wins!


'''