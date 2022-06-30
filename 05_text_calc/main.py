def calc_string(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b
    elif operation == '**':
        return a ** b
    elif operation == '//':
        return a // b
    elif operation == '%':
        return a % b

    return None


result = 0

try:
    with open('calc.txt', 'r') as calc_file:
        for i_line in calc_file:
            temp_list = i_line.split()
            try:
                func_result = calc_string(int(temp_list[0]), int(temp_list[2]), temp_list[1])
                if not func_result:
                    raise SyntaxError
                result += func_result
            except SyntaxError:
                print('Ошибка в строке:', ' '.join(temp_list), end=' ')
                print('Хотите исправить?', end=' ')
                user_answer = input()
                if user_answer == 'да':
                    corrected_string = input('Введите исправленную строку: ').split()
                    func_result = calc_string(int(corrected_string[0]), int(corrected_string[2]), corrected_string[1])
                    result += func_result
                continue
            except IndexError:
                print('Строка "{}" не состоит из операции и двух операндов'.format(' '.join(temp_list)))

except FileNotFoundError:
    print('Файл не обнаружен.')
finally:
    print('Сумма результатов:', result)
