# import logging

import time
from random import randint


# def log(func):
#     def wrapper(*args, **kwargs):
#         func_str = func.__name__
#         args_str = ', '.join(args)
#         kwargs_str = ', '.join([':'.join([str(j) for j in i]) for i in kwargs.iteritems()])
#         with open('log.txt', 'w') as f:
#             f.write(func_str)
#             f.write(args_str)
#             f.write(kwargs_str)
#         return func(*args, **kwargs)
#     return wrapper

def count_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        sort_array = func(*args, **kwargs)
        print("--- %.2f seconds ---" % (time.time() - start_time))

        return sort_array

    return wrapper


@count_time
def sort_bubble(A: list) -> list:
    '''
    Сортировка пузырьком - это метод сортировки массивов и списков путем последовательного сравнения и обмена соседних
    элементов, если предшествующий оказывается больше последующего. В процессе выполнения данного алгоритма элементы с
    большими значениями оказываются в конце списка, а элементы с меньшими значениями постепенно перемещаются по
    направлению к началу списка. Образно говоря, тяжелые элементы падают на дно, а легкие медленно всплывают подобно
    пузырькам воздуха.
    В сортировке методом пузырька количество итераций внешнего цикла определяется длинной списка минус единица, так как
    когда второй элемент становится на свое место, то первый уже однозначно минимальный и находится на своем месте.
    Количество итераций внутреннего цикла зависит от номера итерации внешнего цикла, так как конец списка уже
    отсортирован, и выполнять проход по этим элементам смысла нет.
    '''
    for bypass in range(1, len(A)):
        for i in range(0, len(A) - bypass):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
    return A


if __name__ == "__main__":
    # logging.basicConfig(
    #     format='[%(asctime)s][LINE:%(lineno)d][%(name)s][%(levelname)s:] %(message)s',
    #     datefmt='%Y-%m-%d %H:%M:%S',
    #     # filename='log/sorts.log',
    #     level=logging.DEBUG)
    # logger = logging.getLogger(__name__)
    # logging.info("added %s and %s to get %s" % (x, y, x + y))

    # generate some integers
    A = [randint(0, 100) for _ in range(5_000)]

    print(A)
    print(sort_bubble(A))
