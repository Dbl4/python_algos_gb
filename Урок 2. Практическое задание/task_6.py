"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

import random
random_number = random.randint(1, 100)

#print(random_number)


def rec(number, i=1):
    if i == 10:
        return f'Вы проиграли!Загаданное число - {random_number}'
    elif number == random_number:
        return 'Вы победили!'
    elif number < random_number:
        print('Вы ввели число меньше заданного!')
    elif number > random_number:
        print('Вы ввели число больше заданного!')
    return rec(number - number + int(input('Введите число: ')), i + 1)


print(rec(int(input('Введите число: '))))