class MySteck:
    def __init__(self):
        self.__steck = []

    def add_element(self, obj):
        self.__steck.append(obj)

    def get_element(self):
        if len(self.__steck) != 0:
            end_element = self.__steck[len(self.__steck) - 1]
            self.__steck.remove(end_element)
            return end_element
        else:
            return None

    def print_steck(self):
        print(self.__steck)


class TaskManager:
    def __init__(self):
        self.__steck = dict()

    def new_task(self, task: str, task_queue: int):
        if task_queue in self.__steck:
            self.__steck[task_queue].append(task)
        else:
            for value_task in self.__steck.values():
                if task in value_task:
                    print(f'Задача "{task}" уже в списке!')
                    return
            self.__steck[task_queue] = [task]

    def remove_task(self, task: str):
        delete_key = None
        for key, value in self.__steck.items():
            if task in value:
                value.remove(task)
            if len(value) == 0:
                delete_key = key
        if delete_key is not None:
            self.__steck.pop(delete_key)

    def __str__(self):
        display_steck = ''
        max_numb_in_steck = max([key for key in self.__steck])
        for element in range(max_numb_in_steck + 1):
            if element in self.__steck:
                display_steck += str(element) + ' '
                for task in self.__steck[element]:
                    display_steck += task + '; '
                display_steck += '\n'

        return display_steck

manager = TaskManager()
manager.new_task('Сделать уборку', 4)
manager.new_task('помыть посуду', 4)
manager.new_task('отдохнуть', 1)
manager.new_task('поесть', 2)
manager.new_task('сдать дз', 2)
manager.new_task('поесть', 5)
print(manager)

manager.remove_task('помыть посуду')
print(manager)








