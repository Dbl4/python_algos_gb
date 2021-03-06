"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""
from memory_profiler import profile

def rec(count=1, i=32):
    if i == 128:
        return
    elif count == 10:
        count = 1
        print(f'{i} - {chr(i)}', end='\n')
    elif count < 10:
        count += 1
        print(f'{i} - {chr(i)}', end=' ')
    return rec(count, i + 1)

@profile
def func_3():
    return rec()

func_3()

"""
Если применить функцию обертку к рекурсивной функции, можно увидеть расходуемую память.
Без обертки выводятся большое количество таблиц, что неудобно просматривать.
"""