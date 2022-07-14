class Property:
    __name = 'Имущество'

    def __init__(self, worth):
        self.worth = worth

    def get_name(self):
        return self.__name

    def tax_calculation(self):
        pass


class Apartment(Property):
    __name = 'Апартаменты'

    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        return self.worth / 1000


class Car(Property):
    __name = 'Машина'

    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        return self.worth / 200


class CountryHouse(Property):
    __name = 'Загородный дом'

    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        return self.worth / 500


while True:
    try:
        user_choice = int(input('Рассчитать налог на:\n  1 - Апартаменты\n  2 - Машина\n  3 - Загородный дом\n'
                                '  0 - Выход\n  Выш выбор: '))
        if user_choice not in (1, 2, 3, 0):
            raise ValueError
        if user_choice == 0:
            break

        user_property = Apartment(int(input('Введите стоимость апартаментов: '))) if user_choice == 1 \
            else \
            Car(int(input('Введите стоимость машины: '))) if user_choice == 2 \
                else \
                CountryHouse(int(input('Введите стоимость загородного дома: ')))

        users_money = int(input('Введите наличие денег: '))
        print(f'Налог на {user_property.get_name()}: {user_property.tax_calculation()}')
        if user_property.tax_calculation() > users_money:
            difference = user_property.tax_calculation() - users_money
            print(f'Не хватает {difference} рублей!')
        else:
            print('У вас достаточно средств оплатить налог!')
    except ValueError:
        print('**Неверный ввод! Попробуйте снова!**')
