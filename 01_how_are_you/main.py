from typing import Callable
import functools


def how_are_you(func: Callable) -> Callable:

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        answer = input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию!')
        result = func(*args, **kwargs)
        return result
    return wrapper


@how_are_you
def test_func(numb: int) -> int:
    return numb * sum([i**2 for i in range(1, numb + 1)])


print(test_func(6))
