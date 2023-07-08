class TicTacToe:
    def __init__(self):
        self.players = ['X', 'O']
        self.current_player = 0
        self.board = [['-', '-', '-'] for _ in range(3)]
        self.winner = None

    def get_current_player(self):
        return self.players[self.current_player]

    def print_title(self):
        print(' TIC TAC TOE '.center(40, '='))

    def print_instructions(self):
        print('Choose a column using [ROW][COLUMN] format, for instace:')
        print('Columns 11, 13, 22, and 33 are valid.')
        print('Columns 00, 14, a2, and 44 are invalid.')

    def print_board(self):
        print()
        print(f'Game Board. Current Player [{self.get_current_player()}]')
        print('----------------------------------------')
        print(f' '.ljust(4), end='')
        print('1'.center(5), end='')
        print('2'.center(5), end='')
        print('3'.center(5), end='')
        print()

        for row in range(len(self.board)):
            print(f'{str(row+1)}'.ljust(4), end='')

            for column in self.board[row]:
                print(f'{column}'.center(5).ljust(5), end='')
            print('')
        
        print()

    def get_input(self):
        choose = input(f'Player [{self.get_current_player()}], choose a column => ')
        
        try:
            chooseOptions = list(choose)
            row = chooseOptions[0]
            column = chooseOptions[1]

            if not row.isnumeric() or not column.isnumeric():
                return None, None

            row = int(row)
            column = int(column)

            if row > 3 or column > 3:
                return None, None
            
            if not self.is_cell_available(row, column):
                return None, None

            return row, column
        except:
            return None, None
    
    def get_player_input(self):
        row, column = self.get_input()

        while not row or not column:
            print('Wrong input, try again.')
            row, column = self.get_input()
        
        return row, column
    
    def change_player(self):
        self.current_player = 1 if self.current_player == 0 else 0

    def is_cell_available(self, row, column):
        return self.board[row-1][column-1] == '-'

    def update_board(self, row, column):
        self.board[row-1][column-1] = f'{self.players[self.current_player]}'

    def get_winner(self):
        for row in self.board:
            if all(cell == self.get_current_player() for cell in row):
                return self.get_current_player()

        for column in range(len(self.board[0])):
            if all(self.board[row][column] == self.get_current_player() for row in range(len(self.board))):
                return self.get_current_player()

        if all(self.board[i][i] == self.get_current_player() for i in range(len(self.board))) or \
            all(self.board[i][len(self.board) - i - 1] == self.get_current_player() for i in range(len(self.board))):
            return self.get_current_player()

    def is_tie(self):
        for row in self.board:
            if '-' in row:
                return False

        return True

    def start_game(self):
        self.print_title()
        self.print_instructions()
        self.print_board()

        while not self.winner:
            row, column = self.get_player_input()

            self.update_board(row, column)
            self.print_board()

            self.winner = self.get_winner()
            if self.winner:
                print()
                print(f'THE WINNER IS: {self.winner}')
                print()
                break

            if self.is_tie():
                print()
                print('IT IS A TIE, NO WINNER')
                print()
                break

            self.change_player()
