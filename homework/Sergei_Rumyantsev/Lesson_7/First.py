random_num = 5

while True:
    num = int(input())
    if num != random_num:
        print('попробуйте снова')
    else:
        print('Поздравляю! Вы угадали!')
        break