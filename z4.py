from random import randint
LOWER_LIMIT = 0
UPPER_LIMIT = 1000
num = randint(LOWER_LIMIT, UPPER_LIMIT)
count = 1
while count < 11:
    print('Попытка', count)
    count += 1

    print('отгадай число в диапазоне от ', LOWER_LIMIT, 'до', UPPER_LIMIT)
    num1 = float(input())
    if num1 == num:
        print('УРА. Отгадали с ', count, 'попытки')
    elif num1 > num :
        print('загаданное число меньше')
    else:
        print('загаданное число больше')
        continue
else:
    print('попытки исчерпаны', 'ответ', num)
    quit()


