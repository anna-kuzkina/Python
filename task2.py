# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
# соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class Clothes(ABC):

    total_material = 0

    def __init__(self):
        Clothes.total_material += self.counting_material

    @abstractmethod
    def counting_material(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size
        super().__init__()

    @property
    def counting_material(self):
        return self.size / 6.5 + 0.5

    def __str__(self):
        return f'The size of a Coat is {self.size} with fabric consumption = {self.counting_material}'


class Suit(Clothes):
    def __init__(self, height):
        self.height = height
        super().__init__()

    @property
    def counting_material(self):
        return 2 * self.height + 0.3

    def __str__(self):
        return f'The height of a Suit is {self.height} with fabric consumption = {self.counting_material}'


c_1 = Coat(10)
s_1 = Suit(160)
c_2 = Coat(14)
print(c_1)
print(s_1)
# два варианта вывода общего расхода ткани
print(f'Total fabric consumption for clothing (Coats and Suits) = {sum([x.counting_material for x in [c_1, c_2, s_1]])}')
print(f'Total fabric consumption for clothing (Coats and Suits) = {Clothes.total_material}')
