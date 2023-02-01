"""
Задание 1.

Реализовать класс «Дата», на уровне класса определить атрибут day_month_year,
присвоить ему значение

В рамках класса реализовать два метода.

Первый, с декоратором @classmethod, должен извлекать число, месяц,
год, преобразовывать их тип к типу «Число» и делать атрибутами класса.

Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:
    day_month_year = "1 - 2 - 2023"

    @classmethod
    def get_day_month_year(cls):
        date = [int(el) for el in cls.day_month_year.split() if el != '-']
        cls.day, cls.month, cls.year = date

    @staticmethod
    def val_date():
        if Date.day < 1 or Date.day > 31:
            return "Такая дата не существует!"
        elif 1 > Date.month or Date.month > 12:
            return "Такой месяц не существует!"
        elif 2023 > Date.year or Date.year < 1000:
            return f"Неправильно введён год"
        else:
            return "Дата введена верно"


Date.get_day_month_year()
print(Date.val_date())
