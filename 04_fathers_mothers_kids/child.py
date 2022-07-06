class Child:
    states_of_calm = {0: 'Плачет', 1: 'Счастлив', 2: 'Расстроен'}
    states_of_hunger = {0: 'Очень голодный', 1: 'Сытый', 2: 'Переел'}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.state_of_calm = 0
        self.state_of_hunger = 0

    def print_child_info(self):
        print(f'\n     Имя: {self.name}'
              f'\n     Возраст: {self.age}'
              f'\n     Состояние спокойствия: {self.states_of_calm[self.state_of_calm]}'
              f'\n     Состояние голода: {self.states_of_hunger[self.state_of_hunger]}')

