"""
1)	Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
out_f = open("out_file.txt", "w", encoding='utf-8')
while True:
    text = input()
    if text == "":
        break
    else:
        out_f.write(text + "\n")
out_f.close()
