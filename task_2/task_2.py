"""
2)	Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
my_f = open("file.txt", "r", encoding='utf-8')
numbers_rows = 0

while True:
    content = my_f.readline()
    if content == "":
        break
    else:
        numbers_rows += 1
        numbers_words = len(content.split())
        print(f"Строка номер {numbers_rows} содержит {numbers_words} слов")
print(f"Всего строк - {numbers_rows}")
my_f.close()
