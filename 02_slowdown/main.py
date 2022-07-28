from typing import Callable
import time
import functools


def sleep_func(second: (int, float),) -> Callable:
    """Функция принимает в качестве параметра количество секунд для паузы выполнения функции"""
    def sleep_func_decorator(func: Callable) -> Callable:
        """Декоратор, который перед выполнением передаваемой функции ждет несколько секунд"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            time.sleep(second)
            result = func(*args, **kwargs)
            return result
        return wrapper
    return sleep_func_decorator


@sleep_func(0.5)
def test_func(numb: int) -> int:
    return numb * sum([i**2 for i in range(1, numb + 1)])


print(test_func(5))
