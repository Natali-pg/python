"""
Задание 4.

Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и только арифметические операции.
Не используйте взятие по индексу.

Пример:
Ведите целое положительное число: 123456789
Самая большая цифра в числе: 9
"""

number = int(input("Введите целое положительное число - "))
max_number = number % 10

while True:
    number = number // 10
    current_number = number % 10
    if current_number > max_number:
        max_number = current_number
    elif number > 9:
        continue
    print(f"Самая большая цифра в числе - {max_number}")
    break




