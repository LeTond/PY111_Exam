"""
Вычисление сложности
"""

a = len(arr) - 1            # 1 + 1
out = list()                # 1
while a > 0:                # log1.7(N)
    out.append(arr[a])      # 1
    a = a // 1.7            # 1
out.merge_sort()            # N*log(N)

# O == 2 + 1 + log1.7(N)*1*1 + N*log(N) == log1.7(N) + N*log(N)

print(928029384902384//1.7)


# TODO: Неврно