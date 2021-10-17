# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint
with open('text5.txt', 'w', encoding='utf-8') as f:
    f.write(" ".join([str(randint(1, 100)) for _ in range(100)]))
with open('text5.txt', 'r', encoding='utf-8') as f:
    sum_num = 0
    for i in f.read().split():
        sum_num += int(i)
print(f"Сумма всех чисел в файле = {sum_num}")
