"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func(number1, number2, number3):
    my_list = [number1, number2, number3]
    my_list.sort()
    return my_list[1] + my_list[2]

def my_func1(number1, number2, number3):
    sum_big_number = 0
    if number1 > number2:
        if number2 > number3:
            sum_big_number = number1 + number2
        else:
            sum_big_number = number1 + number3
    else:
        if number1 > number3:
            sum_big_number = number2 + number1
        else:
            sum_big_number = number2 + number3
    return sum_big_number

sum_number = my_func(1, 2, 9)
sum_number1 = my_func1(1, 2, 9)

print(f"сумма равна: {sum_number}")
print(f"сумма равна: {sum_number1}")
