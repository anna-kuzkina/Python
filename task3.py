# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
def my_func(num_1, num_2, num_3):
    numbers_list = [num_1, num_2, num_3]
    numbers_list.sort()
    return numbers_list[-1] + numbers_list[-2]


print(my_func(int(input("Введите 1-е число: ")), int(input("Введите 2-е число: ")),int(input("Введите 3-е число: "))))
