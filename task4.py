# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **. Второй — более сложная реализация без оператора **,
# предусматривающая использование цикла.
def my_func(x, y):
    return x ** y


def enter_x(tip):
    """
    проверка вводимого числа х: действительное положительное число
    """
    input_num = None
    while input_num is None:
        input_num = input(tip)
        try:
            input_num = float(input_num)
        except ValueError:
            print('Ошибка ввода x!')
            input_num = None
            continue
        if input_num > 0:
            return input_num
        else:
            print('Ошибка ввода x!')
            input_num = None
    return input_num


def enter_y(tip):
    """
    проверка вводимого числа y: целое отрицательное число
    """
    input_num = None
    while input_num is None:
        input_num = input(tip)
        try:
            input_num = int(input_num)
        except ValueError:
            print('Ошибка ввода y!')
            input_num = None
            continue
        if input_num < 0:
            return input_num
        else:
            print('Ошибка ввода x!')
            input_num = None
    return input_num


x = enter_x("Введите действительное положительное число x: ")
y = enter_y("Введите целое отрицательное число y: ")
print(my_func(x, y))
