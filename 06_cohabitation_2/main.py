from husband_wife_child import Husband, Wife, Child, Cat, House


def cats_action(cat):
    print(f'Выберете действие для кошки {cat.name}:')
    user_choice = (int(input('1 - Кушать;\t 2 - Спать;\t 3 - Драть обои\n>>>')))
    if user_choice not in (1, 2, 3):
        raise KeyboardInterrupt
    cat.eating(int(input('Введите количество еды:'))) if user_choice == 1 \
        else cat.sleep() if user_choice == 2 else cat.tear_wallpapers()


husband = Husband(input('Введите имя мужа: '))
wife = Wife(input('Введите имя жены: '))
child = Child(input('Введите имя ребенка: '))
cat1 = Cat(input('Введите имя первого кота: '))
cat2 = Cat(input('Введите имя второго кота: '))
house = House()

for day in range(365):
    print(f'{day + 1}-й день.')
    house.print_info()
    husband.print_info()
    wife.print_info()
    child.print_info()
    cat1.print_info()
    cat2.print_info()
    try:
        print(f'Выберете действие для мужа {husband.name}:')
        user_choice = (int(input('1 - Кушать;\t2 - Играть за компьютером;\t 3 - Пойти на работу.\n'
                                 '>>> ')))
        if user_choice not in (1, 2, 3):
            raise KeyboardInterrupt
        husband.eating(int(input('Введите количество еды: '))) if user_choice == 1 \
            else husband.play_computer() if user_choice == 2 else husband.work()

        print(f'Выберете действие для жены {wife.name}:')
        user_choice = (int(input('1 - Кушать;\t2 - Купить продукты;\t 3 - Купить шубу;\t 4 - Убраться в доме\n'
                                 '>>> ')))
        if user_choice not in (1, 2, 3, 4):
            raise KeyboardInterrupt
        wife.eating(int(input('Введите количество еды: '))) if user_choice == 1 \
            else wife.buy_food(int(input('Введите количество еды: ')),
                               int(input('Введите количество еды для кошек: '))) if user_choice == 2 \
            else wife.buy_fur_coat() if user_choice == 3 \
            else wife.clearing_in_house(int(input('Введите количество грязи, чтобы убрать: ')))

        print(f'Выберете действие для ребёнка {child.name}:')
        user_choice = (int(input('1 - Кушать;\t2 - Играться;\t 3 - Пойти в школу.\n>>> ')))
        if user_choice not in (1, 2, 3):
            raise KeyboardInterrupt
        child.eating(int(input('Введите количество еды: '))) if user_choice == 1\
            else child.play_game() if user_choice == 2 else child.go_to_school()

        cats_action(cat1)
        cats_action(cat2)

    except KeyboardInterrupt:
        print('Ошибка ввода, попробуйте снова!')
