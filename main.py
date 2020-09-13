from task2 import funct
from task3 import componenti_svyaznosti, counter
from task4 import calculate_paths, chess_board_
from task5 import consensus, list_
from task6 import rocket_money
from task7 import CountingSort, array
from Enter_Task import *


if __name__ == '__main__':
    print("-------------------Task 2-------------------")
    funct()                                     # Task 2
    print("-------------------Task 3-------------------")
    componenti_svyaznosti(counter)              # Task 3
    print("-------------------Task 4-------------------")
    print(calculate_paths(chess_board_))        # Task 4
    print("-------------------Task 5-------------------")
    consensus(list_)                            # Task 5
    print("-------------------Task 6-------------------")
    rocket_money()                              # Task 6
    print("-------------------Task 7-------------------")
    print(CountingSort(array, 13, 25))          # Task 7
    print("-------------------Library-------------------")
    work_with_library(json_file)                # Library

