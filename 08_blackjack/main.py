import random


class BurnException(Exception):

    def __init__(self, name):
        print(f'Игрок {name} СГОРАЕТ!!!')


class Card:

    def __init__(self, suit, rang):
        self.suit = suit
        self.rang = rang


class Deck:
    suits = ['heart', 'diamond', 'club', 'spade']
    cards_rang = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                  'ace': 11, 'king': 10, 'queen': 10, 'jack': 10
                  }

    def __init__(self):
        self.deck = [Card(suit, rang) for rang in self.cards_rang for suit in self.suits]


class Player:

    def __init__(self, name):
        self.name = name
        self.players_cards = []
        self.ace_one_cards = 0

    def add_and_remove_card(self):
        random_card = random.choice(deck.deck)
        sum_rang = self.calculate_sum_of_rang()
        if sum_rang >= 21 and random_card.rang == 'ace':
            self.ace_one_cards += 1
        else:
            self.players_cards.append(random_card)
            deck.deck.remove(random_card)

    def print_cards_on_hand(self):
        print(f'Карты {self.name}')
        for card in self.players_cards:
            print(f'    {card.rang} of {card.suit}')
        print(f'Количество очков: {self.calculate_sum_of_rang()}')

    def calculate_sum_of_rang(self):
        return sum(Deck.cards_rang[card.rang] for card in self.players_cards) + self.ace_one_cards


def print_all_players_cards(*args):
    for i_player in args:
        print('-' * 30)
        i_player.print_cards_on_hand()
        print('-' * 30)


computer = Player('computer')
user = Player(input('Введите имя игрока: '))
deck = Deck()
print('Игра началась вам выдано по две карты!')
for _ in range(2):
    user.add_and_remove_card()
    computer.add_and_remove_card()

try:
    while True:
        user.print_cards_on_hand()
        print('\n\nВзять еще карту - 1\nОстановиться - 2')
        users_choice = int(input('Выш выбор: '))
        try:
            if users_choice == 1:
                user.add_and_remove_card()
            elif users_choice == 2:
                break
            else:
                raise KeyError
        except KeyError:
            print('Ошибка ввода. Попробуйте еще раз!')
        if computer.calculate_sum_of_rang() < 21:
            computer.add_and_remove_card()
        if user.calculate_sum_of_rang() > 21:
            raise BurnException(user.name)
        if computer.calculate_sum_of_rang() > 21:
            raise BurnException(computer.name)

    print_all_players_cards(user, computer)

    users_rang = user.calculate_sum_of_rang()
    computers_rang = computer.calculate_sum_of_rang()

    if users_rang == computers_rang and users_rang <= 21 >= computers_rang:
        print('Ничья')
    elif 21 >= users_rang > computers_rang:
        print(f'{user.name} Победил! Поздравляем!')
    elif 21 >= computers_rang > users_rang:
        print(f'{computer.name} Победил.')

except BurnException:
    if user.calculate_sum_of_rang() <= 21:
        print_all_players_cards(user, computer)
        print(f'{user.name} Победил! Поздравляем!')
    elif computer.calculate_sum_of_rang() <= 21:
        print_all_players_cards(user, computer)
        print(f'{computer.name} Победил.')
    else:
        print_all_players_cards(user, computer)
        print('Оба сгорели!')

finally:
    print('*' * 10, 'Конец игры!', '*' * 10)
