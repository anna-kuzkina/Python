# coding: utf-8

# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
import sys
from sys import argv


def salary(hours, pay_for_hour, bonus):
    return (hours * pay_for_hour) + bonus


if __name__ == "__main__":
    try:
        h = float(argv[1])
        pay_f_h = float(argv[2])
        b = float(argv[3])
    except ValueError or TypeError():
        print("Ошибка ввода! Вы ввели не число!")
        sys.exit()
    print("Заработная плата сотрудника составила - {}".format(salary(h, pay_f_h, b)))
