"""
4)	Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
my_f = open("file.txt", "r", encoding='utf-8')
numbers_rows = 0
str_list = []

while True:
    content = my_f.readline()
    if content == "":
        break
    else:
        if "One" in content:
            str_list.append(content.replace("One", "Один"))
        elif "Two" in content:
            str_list.append(content.replace("Two", "Два"))
        elif "Three" in content:
            str_list.append(content.replace("Three", "Три"))
        elif "Four" in content:
            str_list.append(content.replace("Four", "Четыре"))
my_f.close()

out_f = open("out_file.txt", "w", encoding='utf-8')
out_f.writelines(str_list)
out_f.close()
