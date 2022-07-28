from typing import Callable
import functools


def debug(func: Callable) -> Callable:

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(repr(func.__name__), 'вернула значение', repr(result))
        return result
    return wrapper


@debug
def greeting(name, age=None):
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


print(greeting("Том"))
print(greeting("Миша", age=100))
print(greeting(name="Катя", age=16))
