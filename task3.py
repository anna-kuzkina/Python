# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
from command import enter_num


def my_func(num_1, num_2, num_3):
    numbers_list = [num_1, num_2, num_3]
    numbers_list.sort()
    return numbers_list[-1] + numbers_list[-2]


a = enter_num("Введите 1-ое число: ")
b = enter_num("Введите 2-ое число: ")
c = enter_num("Введите 3-ье число: ")
print(my_func(a, b, c))
