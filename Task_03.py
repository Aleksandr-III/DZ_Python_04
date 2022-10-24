# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# *Пример*
# - при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]

from random import randint


def o(list_: list):
    result = []
    for i in list_:
        if i in result:
            continue
        elif list_.count(i) == 1:
            result.append(i)
    return result


z = int(input('Введите количество элементов в списке: '))
v = []
for i in range(z):
    v.append(randint(1, 9))
print(f'Список {v}')
print(f'Список не повторяющихся элементов {o(v)}')
