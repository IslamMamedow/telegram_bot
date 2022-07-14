import math


def calc_radian(angle):
    return angle * (math.pi / 180)


class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, distance, angle):
        self.x = round(self.x + distance * math.sin(calc_radian(angle)))
        self.y = round(self.y + distance * math.cos(calc_radian(angle)))


class Bus(Car):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.passengers = 0
        self.income = 0
        self.total_passengers = 0

    def come_in(self, passengers):
        self.passengers += passengers
        self.total_passengers += passengers
        print(f'\nПассажиров в автобусе: {self.passengers}')

    def go_out(self, passengers):
        self.passengers -= passengers
        print(f'\nПассажиров в автобусе: {self.passengers}')

    def move(self, distance, angle):
        super().move(distance, angle)
        earn = self.passengers * distance * 0.5
        print(f'\nАвтобус доехал до точки ({self.x}; {self.y}) c {self.passengers} пассажирами и'
              f' заработал {earn} рублей.')


print('Автобус начинает свой пусть!')
bus = Bus(int(input('Введите координату X: ')),
          int(input('Введите координату Y: ')),
          )
while True:
    try:
        print('\nУкажите действие:\n 1 - Набрать пассажиров\n 2 - Поехать\n'
              ' 3 - Выпустить пассажиров\n 0 - Закончить поездку')
        user_choice = int(input('Введите цифру: '))
        if user_choice not in (1, 2, 3, 0):
            raise SyntaxError
        if user_choice == 0:
            break
        bus.come_in(int(input('Введите количество пассажиров: '))) if user_choice == 1 \
            else bus.move(int(input('Укажите расстояние в км: ')),
                          int(input('Введите направление в градусах: '))) if user_choice == 2 \
            else bus.go_out(int(input('Укажите количество пассажиров: ')))
    except SyntaxError:
        print('Неверный ввод. Попробуйте снова!')

print(f'Поездка завершена.\nОбщее количество пассажиров было: {bus.total_passengers}.\n'
      f'Заработано: {bus.income} рублей.')

