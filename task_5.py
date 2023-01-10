"""
5. Реализовать формирование списка, используя функцию range()
и возможности генераторного выражения.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать лямбда-функцию и функцию reduce().
"""
from functools import reduce

list_of_even_numbers = [el for el in range(100, 1001) if el % 2 == 0]

print(list_of_even_numbers)
print(reduce(lambda prev_el, el: prev_el * el, list_of_even_numbers))
