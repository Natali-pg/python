"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
    выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова
    нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
    вместо числа вводится специальный символ, выполнение программы завершается. Если специальный
    символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
    ранее сумме и после этого завершить программу.
"""
sum_num = 0
flag_exit = 1
index_num = -1
index = 0


def sum_numbers(str_numbers):
    global sum_num,  index_num
    for index_, num in enumerate(str_numbers):
        try:
            sum_num += int(num)
        except ValueError:
            flag_exit = 0
            index_num = index_
            return flag_exit


while flag_exit == 1:
    my_str_numbers = input("Введите числа через пробел: ").split()
    flag_exit = sum_numbers(my_str_numbers)
    print(sum_num)
    if flag_exit != 0:
        while index < index_num:
            sum_num += int(my_str_numbers[index])
            index += 1
        flag_exit = int(input("Хотите продолжить? Да/Нет (1/0) "))
