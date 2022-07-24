from typing import List
from collections.abc import Generator

list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56


def find_number(list1: List, list2: List, number_to_find: int) -> Generator:
    for i_numb in list1:
        for j_numb in list2:
            result = i_numb * j_numb
            yield i_numb, j_numb, result
            if result == number_to_find:
                print('Found!!!')
                return


# find = find_number(list1=list_1, list2=list_2, number_to_find=to_find)
# for i in find:
#     print(i)
