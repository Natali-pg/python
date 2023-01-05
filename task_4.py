"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо
выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень!
ВНИМАНИЕ: использование встроенной функции = задание не принято
Постараться придумать свой алгоритм без **
"""


def my_func(x_, y_):
    y_ = abs(y_)
    number = 1
    while y_ >= 1:
        number = number * x_
        y_ = y_-1
    return 1/number


x = int(input("Введите положительное число х: "))
y = int(input("Введите отрицательное число y: "))
print(f"{x}^({y}) =  {my_func(x, y)}")
