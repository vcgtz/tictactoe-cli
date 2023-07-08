class Board:
    def __init__(self):
        self.board = [['-'.center(5), '-'.center(5), '-'.center(5)] for _ in range(3)]
    
    def print(self):
        print('BOARD')
        print(f' '.ljust(4), end='')
        print('0'.center(5), end='')
        print('1'.center(5), end='')
        print('2'.center(5), end='')
        print()

        for row in range(len(self.board)):
            print(f'{row}'.ljust(4), end='')

            for column in self.board[row]:
                print(f'{column}'.ljust(5), end='')
            print('')

    def start_game(self):
        pass
