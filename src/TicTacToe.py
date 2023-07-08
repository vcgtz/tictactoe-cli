class TicTacToe:
    def __init__(self):
        self.players = ['X', 'O']
        self.current_player = 0
        self.board = [['-'.center(5), '-'.center(5), '-'.center(5)] for _ in range(3)]
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
                print(f'{column}'.ljust(5), end='')
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
        return self.board[row-1][column-1] == '-'.center(5)

    def update_board(self, row, column):
        self.board[row-1][column-1] = f'{self.players[self.current_player]}'.center(5)

    def start_game(self):
        self.print_title()
        self.print_instructions()
        self.print_board()

        while not self.winner:
            row, column = self.get_player_input()

            self.update_board(row, column)
            self.print_board()
            self.change_player()
