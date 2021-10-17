# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
import json

dict_firm = {}
count_firm = 0
sum_profit = 0
with open('text7.txt', 'r', encoding='utf-8') as f:
    for line in f:
        firm, type_firm, money, tax = line.split()
        profit = int(money) - int(tax)
        dict_firm[firm] = profit
        if profit >= 0:
            sum_profit += profit
            count_firm += 1
medium_profit = sum_profit / count_firm
with open('json7.json', 'w', encoding='utf-8') as f:
    json.dump((dict_firm, {"Средняя прибыль": medium_profit}), f, ensure_ascii=False, indent=None)
