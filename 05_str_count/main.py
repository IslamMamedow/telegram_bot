
from functools import wraps
from typing import Callable, Any, Optional


def counter(func: Callable) -> Callable:
    """
    Декоратор для подсчета количества вызовов функции

    :param func:
    :return:
    """
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        """
        Функция - обертка для вывода числа вызова функций
        Мы используем глобальный параметр для хранения числа вызовов.

        :param args:
        :param kwargs:
        :return:
        """
        wrapper.count += 1
        result = func(*args, **kwargs)
        print(f"Функцию '{func.__name__}' вызвали {wrapper.count} раз")
        return result
    wrapper.count = 0
    return wrapper


@counter
def greeting(name: str, age: Optional[int] = None) -> str:
    """
    Приветствие с возрастом и имененем.

    :param name:
    :param age:
    :return:
    """
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растешь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


@counter
def greeting2(name: str) -> None:
    """
    Приветствие с имененем. Вывод в консоль.

    :param name:
    :return:
    """
    print(f'Привет, {name}!')


def main() -> None:
    """
    Основная функция для запуска.

    :return:
    """
    greeting("Том")
    greeting("Миша", age=100)
    greeting2("Маша")
    greeting(name="Катя", age=16)


main()

