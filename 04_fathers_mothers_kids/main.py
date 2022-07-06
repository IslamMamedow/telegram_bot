from child import Child
from parent import Parent


def add_parent():
    parents_name = input('Введите имя родителя: ')
    parents_age = int(input('Введите возраст родителя: '))
    parents.append(Parent(parents_name, parents_age))


def add_child():
    child_name = input('Введите имя ребёнка: ')
    child_age = int(input('Введите возраст ребенка: '))
    for i_parent in parents:
        if i_parent.age - child_age < 16:
            print('Возраст ребёнка должен быть меньше возраста родителя хотя бы на 16 лет!')
            child_age = int(input('Введите возраст ребенка: '))
            break
    child = Child(child_name, child_age)
    for j_parent in parents:
        j_parent.children.append(child)


parents = []
while True:
    user_input = int(input('\nСоздать родителя  - 1\nСоздать ребенка - 2\nПосмотреть информацию о родителе - 3\n'
                           'Покормить ребёнка - 4:\nУспокоить ребенка - 5:\nТвой выбор:'))
    try:
        if user_input == 1:
            add_parent()
        elif user_input == 2:
            if len(parents) == 0:
                print('Для создания ребёнка нужен родитель!')
            else:
                add_child()
        elif user_input == 3 and len(parents) != 0:
            for parent in parents:
                parent.print_parent_info()
        elif user_input == 4 and len(parents) != 0:
            parents[0].child_feeding()
        elif user_input == 5 and len(parents) != 0:
            parents[0].soothe_the_child()
        else:
            raise KeyError
    except KeyError:
        print('Неверный ввод, попробуйте снова!')
