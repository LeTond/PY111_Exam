"""
Вычисление сложности
"""

a = len(arr) - 1            # 1 + 1
out = list()                # 1

while a > 0:                # log1.7(n)
    out.append(arr[a])      # 1
    a = a // 1.7            # 1
out.merge_sort()            # log1.7(n)*log(log1.7(n))

O(n) == log1.7(n) + log1.7(n)*log(log1.7(n)) == log1.7(n)*log(log1.7(n))
