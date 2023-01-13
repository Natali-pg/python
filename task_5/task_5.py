"""
5)	Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
out_f = open("file.txt", "w", encoding='utf-8')
out_f.write("2 4 2 6 7 9 5 13 4")
out_f.close()

my_f = open("file.txt", "r", encoding='utf-8')
number = my_f.read()
number = tuple(map(int, number.split()))
sum_num = sum(number)
print(number)
print(sum_num)
my_f.close()
