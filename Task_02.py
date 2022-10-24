# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# *Пример*
# - при N=236     ->        [2, 2, 59]


z = int(input("Введите число: "))
i = 2 
v = []
o = z
while i <= z:
    if z % i == 0:
        v.append(i)
        z //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {o} -> {v}")