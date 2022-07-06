class Parent:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.children = []

    def print_parent_info(self):
        print(f'  Родитель:\n'
              f'     Имя: {self.name}\n'
              f'     Возраст: {self.age}\n'
              f'  Дети:')
        if len(self.children) == 0:
            print('---Список детей пуст---')
        else:
            for child in self.children:
                child.print_child_info()

    def child_feeding(self):
        if len(self.children) == 0:
            print('Пока некого кормить!')
        else:
            for child in self.children:
                print(f'{child.name} {child.states_of_hunger[child.state_of_hunger]}')
                try:
                    user_answer = int(input('Хотите покормить?(да - 1 / нет - 2) '))
                    if user_answer == 1:
                        child.state_of_hunger += 1
                        self.child_feeding()
                    elif user_answer == 2:
                        return
                    else:
                        raise KeyError
                except KeyError:
                    print('Ошибка ввода! Попробуй снова!')
                    self.child_feeding()

    def soothe_the_child(self):
        if len(self.children) == 0:
            print('Пока некого успокаивать!')
        else:
            for child in self.children:
                print(child.name, '-', child.states_of_calm[child.state_of_calm])
                try:
                    user_choice = int(input('Хотите улучшить состояние? (да - 1 / нет - 2) '))
                    if user_choice == 1:
                        child.state_of_calm += 1
                        self.soothe_the_child()
                    elif user_choice == 2:
                        return
                    else:
                        raise KeyError
                except KeyError:
                    print('Ошибка ввода! Попробуй снова!')
                    self.soothe_the_child()


