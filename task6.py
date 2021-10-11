# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание,
# что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
from itertools import count
from itertools import cycle

# а) итератор, генерирующий целые числа, начиная с указанного,
num_start = int(input("Введите начальное целое число: "))
num_end = int(input("Введите конечное целое число: "))
for num in count(num_start, 1):
    if num > num_end:
        break
    print(num)

# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
с = 0
my_str = input("Введите строку: ")
num_end = int(input("Введите количество элементов строки для печати: "))
for num in cycle(my_str):
    if с >= num_end:
        break
    print(num)
    с += 1
