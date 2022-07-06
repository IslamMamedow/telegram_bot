from random import randint


class HumanDie:
    pass


class Human:

    def __init__(self, name, house):
        self.name = name
        self.satiety = 50
        self.house = house

    def eat(self):
        self.satiety += 10
        self.house.refrigerator_with_food -= 10
        print(f'{self.name} кушает.\nСытость: {self.satiety}'
              f'\nКоличество еды в холодильнике: {self.house.refrigerator_with_food}')

    def work(self):
        self.satiety -= 10
        self.house.safe += 10
        print(f'{self.name} работает.\nСытость: {self.satiety}'
              f'\nКоличество денег в тумбе: {self.house.safe}')

    def play(self):
        self.satiety -= 10
        print(f'{self.name} играет.\nСытость: {self.satiety}')

    def go_to_the_grocery_store(self):
        self.house.refrigerator_with_food += 50
        self.house.safe -= 20
        print(f'{self.name} пошёл в магазин.\nКоличество еды в холодильнике: {self.house.refrigerator_with_food}'
              f'\nКоличество денег в тумбе: {self.house.safe}')

    def print_info(self):
        print(f'{self.name}:\nСтепень сытости: {self.satiety}')
        print(' ' * 4, f'В доме:\nУровень количества еды в холодильнике: {self.house.refrigerator_with_food}'
                       f'\nКоличество денег: {self.house.safe}\n')


class House:
    refrigerator_with_food = 50
    safe = 0


def action(human):
    print(f'Ход {human.name}')
    random_number = randint(1, 6)
    print('Сгенерированное число кубика:', random_number)
    if human.satiety < 20:
        human.eat()
    elif human.house.refrigerator_with_food < 10:
        human.go_to_the_grocery_store()
    elif human.house.safe < 50:
        human.work()
    elif random_number == 1:
        human.work()
    elif random_number == 2:
        human.eat()
    elif human.satiety < 0:
        print(f'{human.name} умер!\n')
        raise HumanDie
    else:
        action(human)


house = House()
human_1 = Human(input('Введите имя второго жильца: '), house)
human_2 = Human(input('Введите имя первого жильца: '), house)
for _ in range(365):
    try:
        action(human_1)
        action(human_2)
        print('-' * 40)

    except HumanDie:
        break

print('-' * 40)
print('Состояние жильцов дома: ')
for human in human_1, human_2:
    human.print_info()







