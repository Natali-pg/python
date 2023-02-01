"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class OnlyNumbersInList(Exception):
    def __init__(self, txt):
        self.txt = txt


num_lst = []
while True:
    try:
        elem = input("Введите число или ! для завершения: ")
        if elem == '!':
            break
        elif elem.isdigit():
            num_lst.append(int(elem))
        else:
            raise OnlyNumbersInList("Введено не число!!! Попробуйте ещё раз")
    except OnlyNumbersInList as error:
        print(error.txt)

print(num_lst)
