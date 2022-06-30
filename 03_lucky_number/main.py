import random


exceptions_tpl = (SyntaxError, BaseException, NameError, IndexError, SystemError, NotADirectoryError, MemoryError)
numb_sum = 0
try:
    while 777 != numb_sum < 777:
        numb = int(input('Введите число: '))
        if random.randint(1, 13) == 13:
            rand_exception = random.choice(exceptions_tpl)
            raise rand_exception
        with open('out_file.txt', 'a') as output_file:
            output_file.write(str(numb) + '\n')
        numb_sum += numb
except rand_exception:
    print('Вас достигла неудача!')
else:
    print('Вы успешно выполнили условия для выхода из порочного цикла!')
