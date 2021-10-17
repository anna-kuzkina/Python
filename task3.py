# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
with open("text3.txt", 'r', encoding="utf-8") as f:
    count_names_20, count_names, count_salary = 0, 0, 0
    f_name = []
    for line in f:
        line = line.split()
        name = line[0]
        salary = float(line[1])
        count_salary += salary
        count_names += 1
        if salary < 20000:
            count_names_20 += 1
            f_name.append(name)
print(f'{count_names_20} сотрудников имеет оклад менее 20 тыс.: {f_name}')
print(f'Cредняя величина дохода сотрудников = {count_salary/count_names}')
