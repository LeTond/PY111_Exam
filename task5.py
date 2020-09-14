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

list_ = [
    'ATTAB',
    'ACTAC',
    'AGCAD',
    'ACAAS']

def consensus(list_):
    diction = {}
    answer = []
    start = 0
    current_key = ""
    lenght = len(list_)
    word_len = len(list_[0])

    for j in range(word_len):
        for i in range(lenght):
            if list_[i][j] not in diction:
                diction[list_[i][j]] = 1
            else:
                diction[list_[i][j]] += 1
        for key, values in diction.items():
            if values > start:
                start = values
                current_key = key
        answer.append(current_key)
        diction = {}
        start = 0

    print(f"Консенсус - строка ----- {answer}")


# TODO: убрать встроенную функцию