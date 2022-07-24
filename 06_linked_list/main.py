from typing import Any


class Node:
    def __init__(self, data: Any = None) -> None:
        self.__data = data
        self.__next_node = None

    def get_data(self) -> Any:
        return self.__data

    def get_next_node(self) -> Any:
        return self.__next_node

    def set_next_node(self, elem: Any) -> None:
        self.__next_node = elem


class LinkedList:
    def __init__(self) -> None:
        self.__head = None
        self.__previous_elem = None
        self.__length_of_list = 0
        self.__count_for_interation = 0
        self.__elem_for_iteration = None

    def append(self, elem: Any) -> None:
        if not self.__head:
            temp_elem = Node(elem)
            self.__head = temp_elem
            self.__previous_elem = temp_elem
            self.__length_of_list += 1
        else:
            temp_elem = Node(elem)
            self.__previous_elem.set_next_node(temp_elem)
            self.__previous_elem = temp_elem
            self.__length_of_list += 1

    def get(self, index: int) -> Any:
        if index > self.__length_of_list:
            raise IndexError
        else:
            if index == 0:
                return self.__head
            else:
                elem_to_return = None
                elem = self.__head.get_next_node()
                for _ in range(index):
                    elem_to_return = elem
                    elem = elem_to_return.get_next_node()

                return elem_to_return.get_data()

    def remove(self, index: int) -> None:
        if index > self.__length_of_list:
            raise IndexError
        else:
            if index == 0:
                elem_to_remove = self.__head
                self.__head = elem_to_remove.get_next_node()
                del elem_to_remove
                self.__length_of_list -= 1
            else:
                elem_to_remove = None
                previous_elem = self.__head
                elem = self.__head.get_next_node()
                for _ in range(index):
                    elem_to_remove = elem
                    elem = elem_to_remove.get_next_node()
                    previous_elem.set_next_node(elem)
                    previous_elem = elem_to_remove

                del elem_to_remove
                self.__length_of_list -= 1

    def __str__(self) -> str:
        string_for_print = '[' + str(self.__head.get_data())
        elem = self.__head.get_next_node()
        for _ in range(self.__length_of_list - 1):
            string_for_print += ' ' + str(elem.get_data())
            elem = elem.get_next_node()

        return string_for_print + ']'

    def __iter__(self):
        self.__count_for_interation = 0
        self.__elem_for_iteration = self.__head
        return self

    def __next__(self) -> Any:
        if self.__length_of_list > self.__count_for_interation:
            self.__count_for_interation += 1
            elem = self.__elem_for_iteration
            self.__elem_for_iteration = elem.get_next_node()
            return elem.get_data()
        else:
            raise StopIteration


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список: ', my_list)
print('Получение третьего элемента: ', my_list.get(2))
print('Удаление второго элемента:')
my_list.remove(1)
print('Новый список:', my_list)
for i in my_list:
    print(i)
