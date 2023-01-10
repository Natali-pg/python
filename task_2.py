"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

Реализуйте вариант без и с генераторным выражением
"""
source_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result_list = []

for index, el in enumerate(source_list):
    if (index > 0) & (el > source_list[index-1]):
        result_list.append(el)
print(result_list)

result_list_2 = [el for index, el in enumerate(source_list) if  (index > 0) & (el > source_list[index-1])]
print(result_list_2)
