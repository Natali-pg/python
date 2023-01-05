"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).

Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!

Process finished with exit code 0

Пример:
Введите первое число: 10
Введите второе число: 10
1.0

Process finished with exit code 0
"""


def division(number1, number2):
    try:
        return number1/number2
    except ZeroDivisionError:
        print("Делить на 0 НЕЛЬЗЯ!")


num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
print(f"{num1}/{num2} = {division(num1, num2)}")
