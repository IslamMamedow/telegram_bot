from gardener import Gardener


gardener_name = input('Введите имя садовнику: ')
potatoes_amount = int(input('Введите количество картошки для посадки в грядку: '))
user_gardener = Gardener(gardener_name, potatoes_amount)
while True:
    user_gardener.print_gardener_info()
    if len(user_gardener.garden.potatoes) != 0 and user_gardener.garden.are_all_ripe():
        print('\nКартошка созрела, можно собирать!!!\n')
    print('-' * 20)
    print('Ухаживать за грядкой - 1\nСобрать урожай - 2\n')
    users_choice = int(input('Введите цифру: '))
    try:
        if users_choice == 1:
            user_gardener.care_of_the_garden()
        elif users_choice == 2:
            if user_gardener.garden.are_all_ripe():
                harvested_potatoes = user_gardener.harvest()
                user_gardener.garden.potatoes.clear()
                print('Урожай собран')
                print('Хотите посадить еще картошку? 1-да / 2-нет')
                users_choice = int(input('Введите цифру: '))
                if users_choice == 1:
                    potatoes_amount = int(input('Введите количество картошки для посадки в грядку: '))
                    user_gardener.plant_potatoes(potatoes_amount)
            else:
                print('Картошка еще не готова к урожаю!')
        else:
            raise KeyError
    except KeyError:
        print('Ошибка ввода! Попробуйте снова.')
