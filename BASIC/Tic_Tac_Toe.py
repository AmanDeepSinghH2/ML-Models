class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # we will use a single list to represent the 3x3 board, instance variable board

    def print_board(self):
        row1 = '| {} | {} | {} |'.format(self.board[0], self.board[1], self.board[2])
        row2 = '| {} | {} | {} |'.format(self.board[3], self.board[4], self.board[5])
        row3 = '| {} | {} | {} |'.format(self.board[6], self.board[7], self.board[8])
        #in this function, we are formatting board's row and printing them
        print()
        print(row1)
        print(row2)
        print(row3)
        print()

    def player_move(self, icon):
        if icon == 'X':
            number = 1
        elif icon == 'O':
            number = 2

        print("Your turn player {}".format(number))
        #checking the location for icon
        choice = int(input("Enter your move (1-9): ").strip())
        if self.board[choice - 1] == ' ':
            self.board[choice - 1] = icon
        else:
            print()
            print("That space is taken!")
            self.player_move(icon)

    def is_victory(self, icon):
        win_conditions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] == icon:
                return True
        return False


if __name__ == '__main__':
    game = TicTacToe()

    while True:
        game.print_board()
        game.player_move('X')
        game.print_board()
        if game.is_victory('X'):
            print("Player 1 Wins! Congratulations!")
            break
        elif ' ' not in game.board:
            print("It's a tie!")
            break
        game.player_move('O')
        if game.is_victory('O'):
            print("Player 2 Wins! Congratulations!")
            break