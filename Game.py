class Board(object):
    def __init__(self):
        self.boardCells = [" "] * 9
    
    def display(self):
        print(" | " + self.boardCells[0] + " | " + self.boardCells[1] + " | " + self.boardCells[2] + " | ")
        print("  --- --- ---")
        print(" | " + self.boardCells[3] + " | " + self.boardCells[4] + " | " + self.boardCells[5] + " | ")
        print("  --- --- ---")
        print(" | " + self.boardCells[6] + " | " + self.boardCells[7] + " | " + self.boardCells[8] + " | ")
        print("  --- --- ---")
    
    def mark_cell(self, position, mark):
        self.boardCells[position] = mark
    
    def is_cell_empty(self, position):
        return self.boardCells[position] == " "
    
    def check_winner(self, mark):
        for i in range(0, 3):
            if ((self.boardCells[i * 3] == self.boardCells[i * 3 + 1]) and (self.boardCells[i*3] == self.boardCells[i * 3 + 2]) and (self.boardCells[i*3] == mark)):
                return True
            if ((self.boardCells[i] == self.boardCells[i + 3]) and (self.boardCells[i] == self.boardCells[i + 6]) and (self.boardCells[i] == mark)):
                return True
             
            # Check diagonals
            if ((self.boardCells[0] == self.boardCells[4]) and (self.boardCells[0]==self.boardCells[8]) and (self.boardCells[0]==mark)):
                return True
            if ((self.boardCells[2] == self.boardCells[4]) and (self.boardCells[2] == self.boardCells[6]) and (self.boardCells[2] == mark)):
                return True
        return False    

class Player(object):
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def make_move(self, board):
        # Ask player to make the move
        while True:
            player_input = int(input(f"{self.name}, enter position (1-9): "))
            position = player_input - 1
            
            if (0 <= position <= 8 and board.is_cell_empty(position)):
                board.mark_cell(position, self.mark)
                break
            else:
                print("Invalid position. Try again!")

def playGame():
    board = Board()
    player1 = input('Enter player1 Name : ')       
    player2 = input('Enter player2 Name : ')  
    
    p1 = Player(player1, 'X')
    p2 = Player(player2, 'O')
    current_player = p1
    
    while True:
        board.display()
        current_player.make_move(board)
        if board.check_winner(current_player.mark):
            board.display()
            print(f"{current_player.name} wins!!")
            break
        if " " not in board.boardCells:
            print("It is a tie")
            break
        current_player = p2 if current_player == p1 else p1

playGame()
