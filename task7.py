"""
Сорт
Дано: массив из 10**6 целых чисел, каждое из которых лежит на отрезке [13, 25].
Задача: отсортировать массив наиболее эффективным способом
"""
from collections import defaultdict
import random

array = [random.randint(13, 25) for i in range(10 ** 4)]


def CountingSort(array, mn, mx):
    count = defaultdict(int)

    for i in array:
        count[i] += 1

    result = []

    for j in range(mn, mx + 1):
        result += [j] * count[j]

    return result