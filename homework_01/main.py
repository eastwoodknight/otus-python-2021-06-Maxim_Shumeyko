"""
Домашнее задание №1
Функции и структуры данных
"""
from math import sqrt
from itertools import islice, count

def power_numbers(*arg):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return list(map(lambda x: x * x, arg))


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(list_, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    filter_dict = {
        ODD: 
            lambda x: x % 2,
        EVEN: 
            lambda x: not x % 2,
        PRIME: 
            lambda x: (x > 1 and x < 4)
                       or all(x % y for y in islice(count(2), int(sqrt(x)) + 1))
    }

    return list(filter(filter_dict[filter_type], list_))

if __name__ == "__main__":
    pass
