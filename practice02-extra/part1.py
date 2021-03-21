import sys
import random

"""
Задание 1.
Преобразовать элементы списка s из строковой в числовую форму.
"""
print("Задание 1")
s = ['235', '1223', '228']
a = [int(i) for i in s]
print(s)
print(a)
print()

"""
Задание 2.
Подсчитать количество различных элементов в последовательности s.
"""
print("Задание 2")
s1 = [1, 1, 2, 3]
print(len(set(s1)))
print()

"""
Задание 3.
Обратить последовательность s без использования функций.
"""
print("Задание 3")
s2 = ['А', 'роза', 'упала', 'на', 'лапу', 'Азора']
print(s2[::-1])
print()

"""
Задание 4.
Выдать список индексов, на которых найден элемент x в последовательности s.
"""
print("Задание 4")
s3 = ['hello', 'world', 'hello', 'hell']
a2 = [i for i, x in enumerate(s3) if x == 'hello']
print(a2)
print()

"""
Задание 5.
Сложить элементы списка s с четными индексами.
"""
print("Задание 5")
s4 = [0, 1, 2, 3, 4]
a3 = sum([j for i, j in enumerate(s4) if not i % 2])
print(a3)
print()

"""
Задание 6.
Найти строку максимальной длины в списке строк s.
"""
print("Задание 6")
s5 = ['1', '22', '33', 'abc', 'abcdefghijklmno']
a4 = max([len(i) for i in s5])
print(a4)


def shorter():
    """
    Сократите код до 19 символов без использования функций.
    return ["much", "code", "wow"][i] # 24 символа
    :return: Первый элемент списка.
    """
    i = 0
    return "muchcodewow"[:i + 4]  # 19 символов


def generate_groups(group_str):
    """
    Напишите генерацию всех названий групп в том виде, в котором используется
    в выпадающем списке на сайте с результатами от робота kispython.
    :param group_str: Название группы.
    :return: Преобразованное название группы.
    """
    return "{}{}".format(group_str[1], int(group_str[5:7]))


def zip_work():
    """
    Изучите, как работает функция zip().
    :return: Список из кортежей, содержащих пары по позициям.
    """
    a = [77, 44, 5]
    b = [3.5, 0.0, -1.0]
    c = ["java", "python", "kotlin"]
    zipped = zip(a, b, c)
    return list(zipped)


def mul_digits(*digits):
    """
    Разберите роль операции * в создании функций с переменным числом
    аргументов, а также для распаковки последовательностей.
    :param digits: Переменное число входных параметров (чисел).
    :return: Произведение чисел.
    """
    res = 1
    for d in digits:
        res *= d
    return res


def transpose(matrix):
    """
    Реализуйте с помощью zip() функцию transpose() для транспонирования матрицы.
    :param matrix: Исходная матриица.
    :return: Транспонированная матрица.
    """
    return list(list(i) for i in zip(*matrix))


economy_data = [
    ["Коллеги,", "В то же время,", "Однако,", "Тем не менее,", "Следовательно,",
     "Соответственно,", "Вместе с тем,", "С другой стороны,"],
    ["парадигма цифровой экономики", "контекст цифровой трансформации",
     "диджитализация бизнес-процессов",
     "прагматичный подход к цифровым платформам",
     "совокупность сквозных технологий", "программа прорывных исследований",
     "ускорение блокчейн-транзакций", "экспоненциальный рост Big Data"],
    ["открывает новые возможности для", "выдвигает новые требования",
     "несёт в себе риски", "расширяет горизонты", "заставляет искать варианты",
     "не оставляет шанса для", "повышает вероятность", "обостряет проблему"],
    ["дальнейшего углубления", "бюджетного финансирования",
     "синергетического эффекта", "компрометации конфиденциальных",
     "универсальной коммодитизации", "несанкционированной кастомизации",
     "нормативного регулирования", "практического применения"],
    ["знаний и компетенций.", "непроверенных гипотез.", "волатильных активов.",
     "опасных экспериментов.", "государственно-частных партнёрств.",
     "цифровых следов граждан.", "нежелательных последствий.",
     "внезапных открытий."]
]


def digital_economy_report_generator():
    """
    Реализуйте генератор докладов по цифровой экономике.
    :return: Сгенерированный доклад
    """
    return " ".join(random.choice(i) for i in economy_data)


def my_print(*args, sep=" ", end="\n"):
    """
    Реализуйте свою версию print(). Постарайтесь использовать максимум
    возможностей настоящей print(). Для вывода используйте функцию
    sys.stdout.write().
    :param args: Аргументы для вывода.
    :param sep: Разделитель данных для вывода.
    :param end: Последний символ строки вывода.
    :return: Ничего не возвращает. Происходит вывод.
    """
    sys.stdout.write(sep.join(str(i) for i in args) + end)


def only_named_args(**args):
    """
    Реализуйте функцию, которая принимает только именованные аргументы. При
    передаче позиционного аргумента Питон должен выдать ошибку.
    :param args: Исходные аргументы
    :return: Словарь из ключей и значений.
    """
    return args


def generate_array(*dim):
    """
    Напишите функцию generate_array(dim1, dim2, dim3, ...) для создания
    многомерного массива с помощью вложенных списков.
    :param dim: Исходная последовательность аргументов.
    :return: Многомерный массив.
    """
    return [*dim]


