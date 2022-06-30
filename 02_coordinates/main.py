import random

def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x


try:
    with open('coordinates.txt', 'r') as file:
        for line in file:
            nums_list = line.split()
            try:
                res1 = f(int(nums_list[0]), int(nums_list[1]))
                res2 = f2(int(nums_list[0]), int(nums_list[1]))
                number = random.randint(0, 100)
                with open('result.txt', 'a') as file_2:
                    my_list = sorted([res1, res2, number])
                    temp_list = [str(i) for i in my_list]
                    file_2.write(' '.join(temp_list) + '\n')
            except ZeroDivisionError:
                print("Ошибка: В результате вычисление произошло деление на 0")
except FileNotFoundError:
    print("Файл не найден.")
