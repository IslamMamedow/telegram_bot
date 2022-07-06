from random import randint


class Warrior:
    health = 100

    def __init__(self, name):
        self.name = name

    def attack(self, target):
        if not isinstance(target, Warrior):
            print('Цель невозможно атаковать!')
        else:
            target.health -= 20
            print(f'\n{self.name} атаковал {target.name}.\nНанёс 20 урона!\n'
                  f'У {target.name} осталось {target.health} здоровья.')


warrior_1 = Warrior(input('Введите имя первого война: '))
warrior_2 = Warrior(input('Введите имя второго война: '))

while True:
    if warrior_1.health <= 0:
        print('\nКонец игры!\nПобедитель:', warrior_2.name)
        break
    elif warrior_2.health <= 0:
        print('\nКонец игры!\nПобедитель:', warrior_1.name)
        break
    random_number_for_attack = randint(1, 10)
    if random_number_for_attack <= 5:
        warrior_1.attack(warrior_2)
    elif random_number_for_attack > 5:
        warrior_2.attack(warrior_1)








