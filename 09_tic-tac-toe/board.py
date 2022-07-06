
for y in range(5):
    if y == 1 or y == 3:
        print('-' * 11)
    else:
        for x in range(11):
            if x == 3 or x == 7:
                print('|', end='')
            else:
                print(' ', end='')
        print()



