"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""
my_f = open("file.txt", "r", encoding='utf-8')
number_employees = 0
sum_income = 0

while True:
    content = my_f.readline()
    if content == "":
        break
    else:
        number_employees += 1
        content = content.split()
        sum_income += int(content[1])
        if int(content[1]) < 20000:
            print(content[0])

print(f"Средняя величина доходов сотрудников = {sum_income/number_employees}")
my_f.close()
