# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position
# (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
# (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f'Полное имя сотрудника - {self.surname} {self.name}'

    def get_total_income(self):
        return f"Доход сотрудника с учетом премии - {(self._income['wage'] + self._income['bonus'])}"


position_1 = Position(input("Введите имя работника: "), input("Введите фамилию работника: "),
                      input("Введите должность работника: "), int(input("Введите оклад работника: ")),
                      int(input("Введите премию работника: ")))
print(position_1.get_full_name())
print(position_1.get_total_income())
print(position_1.position)
print(position_1._income["bonus"])
