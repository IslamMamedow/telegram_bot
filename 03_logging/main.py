import datetime
from typing import Callable
import functools


def logging(func: Callable) -> Callable:
    """Декоратор, логирует функцию и записывает в файл 'function_errors' дату и время возникновения ошибки,
        имя функции и тип ошибки
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception as error:
            with open('function_errors.log', 'a') as file_for_errors:
                file_for_errors.write(f'{datetime.datetime.now()};   '
                                      f'Function name: {func.__name__};   '
                                      f'Error: {error.__class__.__name__} - {error}.\n')
            print(f'В функции {func.__name__} произошла ошибка {error.__class__.__name__}!')
        else:
            print(f'Функция {func.__name__} успешно завершилась. {func.__doc__}')
            return result
    return wrapper


@logging
def test(name, count):
    """Функция приветствует count раз"""
    for _ in range(count):
        print(f'Hello {name}')


@logging
def test2(numb):
    """Функция выводит на экран кубы чисел"""
    for i in range(numb):
        print(i ** 3)


test(name='Ivan', count='r')
test2(5)



