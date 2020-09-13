"""
Задача консенсуса DNA ридов
При чтении DNA последовательностей могут возникать единичные ошибки, выражающиеся в неверной букве в строке.
Для решения данной проблемы требуемое место читается несколько раз, после чего строится консенсус-строка,
в которой на каждом месте будет стоять тот символ, что чаще всего встречался в этом месте суммарно во всех чтениях.
Т.е. для строк
ATTA
ACTA
AGCA
ACAA
консенсус-строка будет ACTA (в первой ячейке чаще всего встречалась A, во второй – C, в третьей – Т,
в четвертой – снова А).
Для входного списка из N строк одинаковой длины построить консенсус-строку.

"""

from collections import Counter

list_ = ['BTTA',
         'AGTD',
         'AGCD',
         'AGAD']


def consensus(list_):
    dot = []
    answer = ""
    counter = 0
    len_cons = len(list_[0])
    enter = ""
    while len(answer) < len_cons:
        for i in range(len(list_)):
            enter += list_[i]
            print(enter)
        for j in range(counter, len(enter), 4):
            dot.append(enter[j])
        counter += 1
        answer += Counter(dot).most_common(1)[0][0]
    print(f"Консенсус - строка: {answer}")

