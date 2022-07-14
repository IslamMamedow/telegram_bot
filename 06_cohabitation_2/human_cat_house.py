class Human:
    def __init__(self, name):
        self.name = name
        self.satiety = 30
        self.happiness = 100

    def eating(self, food_amt):
        self.satiety += food_amt if food_amt <= 30 else 30
        if House.food_in_refrigerator >= food_amt:
            House.food_in_refrigerator -= food_amt
            print(f'{self.name} кушает\n   Сытость + {food_amt} = {self.satiety}\n'
                  f'Eда в холодильнике -(минус) {food_amt} = {House.food_in_refrigerator}')
        else:
            print('Еды в холодильнике не достаточно, сходите в магазин!!!')

    def pet_the_cat(self):
        self.happiness += 5
        self.satiety -= 10

    def print_info(self):
        print(f'{self.__class__.__name__}\t{self.name}:\n   Степень сытости: {self.satiety};\n'
              f'   Степень счастья: {self.happiness}.')


class Cat:
    def __init__(self, name):
        self.name = name
        self.cat_satiety = 30

    def eating(self, food_amt):
        self.cat_satiety += food_amt
        House.food_for_cat -= food_amt
        print(f'Кошка {self.name} покушала:\n   Сытость + {food_amt} = {self.cat_satiety}\n '
              f'   Количество еды для кошки в доме -(минус) {food_amt} = {House.food_for_cat}')

    def sleep(self):
        self.cat_satiety -= 10
        print(f'Кошка {self.name} спит:\n   Сытость -(минус) 10 = {self.cat_satiety}')

    def tear_wallpapers(self):
        self.cat_satiety -= 10
        House.dirt_amount += 5
        print(f'Кошка {self.name} сдирает обои и мусорит + 5 = {House.dirt_amount}\n'
              f'Сытость -(минус) 10 = {self.cat_satiety}')

    def print_info(self):
        print(f'{self.__class__.__name__}\t{self.name}:\n   Степень сытости: {self.cat_satiety}.')


class House:
    money_in_safe = 100
    food_in_refrigerator = 150
    food_for_cat = 30
    dirt_amount = 0

    def print_info(self):
        print(f'В доме:\nКоличество денег: {self.money_in_safe}; \t'
              f'Количество еды в холодильнике: {self.food_in_refrigerator}; \t'
              f'Количество еды для кота: {self.food_for_cat}; \t'
              f'Уровень грязи: {self.dirt_amount}.')
