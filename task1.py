"""
Вычисление сложности
"""


def o_notation(arr=[1, 2, 3, 4]):
    a = len(arr) - 1  # 1 + 1
    out = list()  # 1
    while a > 0:  # log1.7(N)
        out.append(arr[a])  # N
        a = a // 1.7  # 1
    out.merge_sort()  # Nlog(N)


## 2 + 1 + log1.7(N) * (1+N) +NlogN = 3 + Nlog1.7(N) + Nlog(N) = Nlog(N)

