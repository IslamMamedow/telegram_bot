import random


class Karma:
    __karma_value_constant = 500

    def __init__(self):
        self.current_karma = 0

    def get_karma_value_constant(self):
        return self.__karma_value_constant


class KillError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


def one_day():
    if random.randint(1, 10) == 5:
        raise random.choice([DrunkError, CarCrashError, GluttonyError, DepressionError])
    else:
        return random.randint(1, 7)


my_karma = Karma()
day = 0
with open('karma.log', 'a') as karma_file:
    while True:
        day += 1
        try:
            if my_karma.current_karma >= my_karma.get_karma_value_constant():
                break
            else:
                daily_karma = one_day()
                print(f'{day} день прошел хорошо + к карме {daily_karma}')
                my_karma.current_karma += daily_karma
        except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as error:
            error_message = f'День {day}. Ошибка {error.__class__.__name__}'
            print(error_message)
            karma_file.write(error_message + '\n')





