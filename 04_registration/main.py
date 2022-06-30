def is_correct(input_list):
    if len(input_list) != 3:
        raise IndexError('Не присутствуют все три поля.')
    elif not input_list[0].isalpha():
        raise NameError('Поле имени содержит НЕ только буквы.')
    elif '@' not in input_list[1] and '.' not in input_list[1]:
        raise SyntaxError('Поле "Имейл" НЕ содержит @ и .(точку).')
    elif not 10 < int(input_list[2]) < 99:
        raise ValueError('Поле "Возраст" НЕ является числом от 10 до 99')


with open('registrations.txt', 'r') as data_file,\
        open('registrations_bad.log', 'a') as file_for_incorrect_mail, \
        open('registrations_good.log', 'a') as file_for_correct_mail:
    for i_line in data_file:
        temp_users_data = i_line.split()
        try:
            is_correct(temp_users_data)
        except (NameError, SyntaxError, ValueError, IndexError) as exc:
            error_message = f'{i_line.rstrip()} - {exc.__class__.__name__} - {exc}\n'
            file_for_incorrect_mail.write(error_message)
        else:
            file_for_correct_mail.write(' '.join(temp_users_data) + '\n')
