# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
def my_f(name, surname, year, city, email, phone):
    return f'name - {name}, surname - {surname}, year - {year}, city - {city}, email - {email}, phone - {phone}'


print(my_f(name='Джон', surname='Леннон', year=1940, city='Ливерпуль', email='forever_young@gmail.com', phone=83672667))
