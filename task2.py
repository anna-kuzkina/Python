# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
with open("text2.txt", 'r', encoding="utf-8") as f:
    count_lines = 0
    for line in f:
        f_line = line
        count_lines += 1
        # words = f_line.split()
        print(f"В строке {len(f_line.split())} слов(а)")
print(f"Всего в файле {count_lines} строки")
