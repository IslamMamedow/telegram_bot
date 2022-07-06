class WinnerException(Exception):

    def __init__(self, players_name):
        print(f'Выиграл {players_name}')


class Board:
    cell_coordinate_for_interface = {(1, 4): 1, (1, 2): 4, (1, 0): 7,
                                     (5, 4): 2, (5, 2): 5, (5, 0): 8,
                                     (9, 4): 3, (9, 2): 6, (9, 0): 9,
                                     }

    def interface_board(self, player=None, players_numbers=None):
        print('\n', '-' * 18)
        for y in range(5):
            if y == 1 or y == 3:
                print('-' * 18)
            else:
                for x in range(11):
                    if x == 3 or x == 7:
                        print('|', end='')
                    elif (x, y) in self.cell_coordinate_for_interface:
                        if isinstance(player, Player):
                            for key_cell, value_cell in self.cell_coordinate_for_interface.items():
                                if players_numbers == value_cell and (x, y) == key_cell:
                                    print(' ', player.symbol, end='  ')
                                    self.cell_coordinate_for_interface[key_cell] = player.symbol
                                    player.players_cells.append(key_cell)
                                    player = None
                                    break
                            else:
                                print(f'  {self.cell_coordinate_for_interface[(x, y)]}', end='  ')
                        else:
                            print(f'  {self.cell_coordinate_for_interface[(x, y)]}', end='  ')
                print()
        print('-' * 18, '\n')


class Player:
    winners_lines = [[(1, 4), (5, 2), (9, 0)],
                     [(1, 0), (5, 2), (9, 4)],
                     [(1, 4), (1, 2), (1, 0)],
                     [(5, 4), (5, 2), (5, 0)],
                     [(9, 4), (9, 2), (9, 0)],
                     [(1, 4), (5, 4), (9, 4)],
                     [(1, 2), (5, 2), (9, 2)],
                     [(1, 0), (5, 0), (9, 0)]]

    def __init__(self, name, symbol):
        self.name = name
        self.players_cells = []
        self.symbol = symbol

    def player_turn(self, game_board):
        print(f'{self.name} ваш ход!')
        player1_choice = input('Введите число: ')
        game_board.interface_board(self, int(player1_choice))
        if len(self.players_cells) >= 3:
            if self.is_winner():
                raise WinnerException(self.name)

    def is_winner(self):
        count = 0
        for line in self.winners_lines:
            for cell_in_line in line:
                if cell_in_line in self.players_cells:
                    count += 1
                if count == 3:
                    return True
            count = 0
        return False


board = Board()
player1_name = input('Игрок 1: Введите имя: ')
player2_name = input('Игрок 2: Введите имя: ')
player1_symbol_choice = int(input(f'Игрок {player1_name} выберете символ: 1 - "X" / 2 - "O": '))
try:
    if player1_symbol_choice == 1:
        player1 = Player(player1_name, 'X')
        player2 = Player(player2_name, 'O')
    elif player1_symbol_choice == 2:
        player1 = Player(player1_name, 'O')
        player2 = Player(player2_name, 'X')
    else:
        raise KeyError
except KeyError:
    print('Ошибка ввода, попробуйте еще раз!')
print('Игра крестики-нолики!\nПоле 3x3, числа  - это клетка куда вы можете определить '
      'свой символ введя в поле число от 1 до 9.')
board.interface_board()

for _ in range(9):
    try:
        player1.player_turn(board)
        player2.player_turn(board)
    except WinnerException:
        break

print('Конец игры!')


