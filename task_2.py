"""
Задание 2.

Создайте собственный!!! класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class ExceptionDivisionByZero(Exception):
    def __init__(self, txt):
        self.txt = txt


def division_by_zero(one_number, two_number):
    try:
        if two_number == 0:
            raise ExceptionDivisionByZero("Деление на ноль запрещено!")
        print(one_number / two_number)
    except ExceptionDivisionByZero as err:
        print(err)


division_by_zero(4, 2)
division_by_zero(5, 0)

