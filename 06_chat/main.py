def print_text():
    print()
    with open('chat_text.txt', 'r') as text_file:
        for i_line in text_file:
            print(' '.join(i_line.split()))
            print('*' * 20)


def write_message(name):
    with open('chat_text.txt', 'a') as text_file:
        message = input('Введите сообщение: ')
        text_file.write(name + ': ' + message + '\n')


while True:
    users_name = input('Введите имя: ')
    print('1 - Посмотреть текущий текст чата.')
    print('2 - Отправить сообщение.')
    user_answer = input('Выберете действие:')
    if user_answer == '1':
        print_text()
    elif user_answer == '2':
        write_message(users_name)
    else:
        print('Ошибка ввода, попробуйте снова.')


