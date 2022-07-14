from human_cat_house import Human, Cat, House


class Husband(Human):
    def __init__(self, name):
        super().__init__(name)

    def work(self):
        self.satiety -= 10
        House.money_in_safe += 150
        print(f'{self.name} работал:\n   Сытость -(минус) 10 = {self.satiety}\n'
              f'   Деньги в дом + 150 = {House.money_in_safe}')

    def play_computer(self):
        self.happiness += 20
        self.satiety -= 10
        print(f'{self.name} играл:\n   Сытость -(минус) 10 = {self.satiety}\n'
              f'   Счастье + 20 = {self.happiness}')


class Wife(Human):
    def __init__(self, name):
        super().__init__(name)
        self.fur_coat = 0

    def buy_food(self, food_for_human, food_for_cat):
        if House.money_in_safe >= food_for_human + food_for_cat:
            House.food_in_refrigerator += food_for_human
            House.food_for_cat += food_for_cat
            House.money_in_safe -= food_for_human + food_for_cat
        else:
            print(f'{food_for_human + food_for_cat - House.money_in_safe} не хватает на '
                  f'продукты!')

        self.satiety -= 10
        print(f'{self.name} ходила за продуктами:\n   Еда в холодильник + {food_for_human}\n'
              f'   Еда для кота + {food_for_cat}\n'
              f'   Деньги в доме -(минус) {food_for_human + food_for_cat} = {House.money_in_safe}\n'
              f'   Сытость -(минус) 10 = {self.satiety}')

    def clearing_in_house(self, dirt_amt):
        House.dirt_amount -= dirt_amt if dirt_amt <= 100 else 100
        self.satiety -= 10
        print(f'{self.name} произвела уборку в доме:\n   Количество грязи -(минус) {dirt_amt}\n'
              f'   Сытость -(минус) 10 = {self.satiety}')

    def buy_fur_coat(self):
        self.fur_coat += 1
        House.money_in_safe -= 350
        self.happiness += 60
        print(f'{self.name} купила шубу:\n   Количество денег в доме -(минус) 350 = {House.money_in_safe}\n'
              f'   Счастье + 60 = {self.happiness}')


class Child(Human):
    def __init__(self, name):
        super().__init__(name)

    def eating(self, food_amt):
        self.satiety += food_amt if food_amt <= 10 else 10
        House.food_in_refrigerator -= food_amt
        print(f'{self.name} кушает\n   Сытость + {food_amt} = {self.satiety}\n'
              f'   Eда в холодильнике -(минус) {food_amt} = {House.food_in_refrigerator}')

    def play_game(self):
        self.satiety -= 10
        self.happiness += 30
        House.dirt_amount += 10
        print(f'{self.name} поиграл:\n   Сытость -(минус) 10 = {self.satiety}\n'
              f'   Счастье + 30 = {self.happiness}\n'
              f'   Грязь в доме + 10 = {House.dirt_amount}')

    def go_to_school(self):
        self.satiety -= 10
        print(f'{self.name} сходил в школу:\n   Сытость -(минус) 10 = {self.satiety}\n')
