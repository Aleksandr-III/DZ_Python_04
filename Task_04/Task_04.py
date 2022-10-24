# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random


def write_file(st):
    with open('failik.txt', 'w') as file:
        file.write(st)


def create_(k):
    list_ = []
    for i in range(k+1): 
        list_.append(random.randint(0,100))
    return list_
    

def create(sp):
    list_ = sp[::-1]
    v = ''
    if len(list_) < 1:
        v = 'x = 0'
    else:
        for i in range(len(list_)):
            if i != len(list_) - 1 and list_[i] != 0 and i != len(list_) - 2:
                v += f'{list_[i]}x^{len(list_)-i-1}'
                if list_[i+1] != 0:
                    v += ' + '
            elif i == len(list_) - 2 and list_[i] != 0:
                v += f'{list_[i]}x'
                if list_[i+1] != 0:
                    v += ' + '
            elif i == len(list_) - 1 and list_[i] != 0:
                v += f'{list_[i]} = 0'
            elif i == len(list_) - 1 and list_[i] == 0:
                v += ' = 0'
    return v

k = int(input("Введите натуральную степень k = "))
k_ = create_(k)
write_file(create(k_))


