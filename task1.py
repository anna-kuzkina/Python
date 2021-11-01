# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.
import numbers


class Matrix(object):
    def __init__(self, lists):
        Matrix.check_matrix(lists)
        self.__lists = lists
        self.__dim = (len(lists), len(lists[0]))

    @staticmethod
    def check_matrix(lists):
        if type(lists) != list:
            raise ValueError('Expected type list, got {}'.format(type(lists)))
        if len(lists) == 0:
            raise ValueError('Matrix should not be empty')
        prev_len = len(lists[0])
        for i, sublist in enumerate(lists):
            if type(sublist) != list:
                raise ValueError('Expected list of lists, got {} on {} position'.format(type(lists), i))
            if len(sublist) != prev_len:
                raise ValueError('Length of rows are not equal: row 0 has {} elements, row {} has {}'
                                 .format(prev_len, i, len(sublist)))
            for el in sublist:
                if not isinstance(el, numbers.Number):
                    raise ValueError('Expected all elements to be numbers, found {} of type {} at row {}'
                                     .format(el, type(el), i))

    def __str__(self):
        res = []
        for el in self.__lists:
            for i in el:
                res.append(str(i))
                res.append(" ")
            res.append("\n")
        return ''.join(res)

    def __add__(self, other):
        if self.__dim != other.__dim:
            raise ValueError('Expected equal dims, got {}, {}'.format(str(self.__dim), str(other.__dim)))
        matrix_result = []
        for i in range(len(self.__lists)):
            matrix_result.append([])
            for j in range(len(self.__lists[i])):
                matrix_result[i].append(self.__lists[i][j] + other.__lists[i][j])
        return Matrix(matrix_result)


m_1 = Matrix([[1, 2, 3, 4], [4, 3, 2, 1]])
m_2 = Matrix([[4, 3, 2, 1], [5, 6, 7, 8]])
m_3 = Matrix([[1, 1, 1, 1], [1, 1, 1, 1]])
print(f"Matrix 1:\n{m_1}")
print(f"Matrix 1:\n{m_2}")
print(f"Sum of matrices \n{m_1 + m_2}")
print(f"Sum of matrices:\n{m_1 + m_2 + m_3}")
m_4 = Matrix([[1, 1, 1], [1, 1, 1]])
print(f"Sum of matrices:\n{m_1 + m_2 + m_3 + m_4}")
