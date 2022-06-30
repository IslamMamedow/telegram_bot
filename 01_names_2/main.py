symbol_sum = 0
line_count = 0
try:
    with open('people.txt', 'r') as people_file:
        for i_name in people_file:
            line_count += 1
            length = len(i_name)
            if i_name.endswith('\n'):
                length -= 1
            try:
                if length < 3:
                    raise ValueError
                symbol_sum += length
            except ValueError:
                print('Ошибка: менее трех символов в строке {}.'.format(line_count))
                with open('errors.log', 'a') as errors_file:
                    errors_file.write('Ошибка: менее трех символов в строке {}.\n'.format(line_count))
except FileNotFoundError:
    print('Файл не найден.')
finally:
    print('Общее количество символов:', symbol_sum)
