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
        print("--- {} элементов: {:.4f} seconds ---".format(len(sort_array), time.time() - start_time))

        return sort_array

    return wrapper


@count_time
def sort_bubble(arr: list) -> list:
    """
    Сортировка пузырьком - это метод сортировки массивов и списков путем последовательного сравнения и обмена соседних
    элементов, если предшествующий оказывается больше последующего. В процессе выполнения данного алгоритма элементы с
    большими значениями оказываются в конце списка, а элементы с меньшими значениями постепенно перемещаются по
    направлению к началу списка. Образно говоря, тяжелые элементы падают на дно, а легкие медленно всплывают подобно
    пузырькам воздуха.
    В сортировке методом пузырька количество итераций внешнего цикла определяется длинной списка минус единица, так как
    когда второй элемент становится на свое место, то первый уже однозначно минимальный и находится на своем месте.
    Количество итераций внутреннего цикла зависит от номера итерации внешнего цикла, так как конец списка уже
    отсортирован, и выполнять проход по этим элементам смысла нет. Сложность алгоритма: n*n

    :param arr: Неотсортированный массив
    :return: Отсортированный массив
    """
    for bypass in range(1, len(arr)):
        for i in range(0, len(arr) - bypass):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


class sort_heapsort():
    """
    Пирамидальная сортировка (англ. Heapsort, «Сортировка кучей») — алгоритм сортировки, работающий
    в худшем, в среднем и в лучшем случае (то есть гарантированно) за Θ(n log n) операций при
    сортировке n элементов. Может рассматриваться как усовершенствованная сортировка пузырьком, в которой элемент
    всплывает (min-heap) / тонет (max-heap) по многим путям.

    Сортировка пирамидой использует бинарное сортирующее дерево. Сортирующее дерево — это такое дерево,
    у которого выполнены условия:
    Каждый лист имеет глубину либо d, либо d-1, d — максимальная глубина дерева.
    Значение в любой вершине не меньше (другой вариант — не больше) значения её потомков.
    Удобная структура данных для сортирующего дерева — такой массив Array, что Array[0] — элемент в
    корне, а потомки элемента Array[i] являются Array[2i+1] и Array[2i+2].

    Алгоритм сортировки будет состоять из двух основных шагов:
    1. Выстраиваем элементы массива в виде сортирующего дерева:
    Array[i]>=Array[2i+1], Array[i]>=Array[2i+2]

    при 0 <= i < n/2
    Этот шаг требует O(n) операций.

    2. Будем удалять элементы из корня по одному за раз и перестраивать дерево. То есть на первом
    шаге обмениваем Array[0] и Array[n-1], преобразовываем Array[0], Array[1], … , Array[n-2] в
    сортирующее дерево. Затем переставляем Array[0] и Array[n-2], преобразовываем Array[0],
    Array[1], … , Array[n-3] в сортирующее дерево. Процесс продолжается до тех пор, пока в
    сортирующем дереве не останется один элемент. Тогда Array[0], Array[1], … , Array[n-1] —
    упорядоченная последовательность.

    Этот шаг требует O(n*log n) операций.

    :param arr: Неотсортированный массив
    :return: Отсортированный массив
    """

    def __init__(self, arr: list):
        self.arr = arr

    def swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def sift_down(self, n, max):
        while True:
            biggest = n
            c1 = 2 * n + 1
            c2 = c1 + 1
            for c in [c1, c2]:
                if c < max and self.arr[c] > self.arr[biggest]:
                    biggest = c
            if biggest == n:
                return
            self.swap(n, biggest)
            n = biggest

    def heapify(self):
        i = int((len(self.arr) - 1) / 2)
        max = len(self.arr)
        while i >= 0:
            self.sift_down(i, max)
            i -= 1

    @count_time
    def heapsort(self):
        self.heapify()  # Create heap
        j = len(self.arr) - 1
        while j > 0:
            self.swap(0, j)  # Move head of heap to next place in sorted list
            self.sift_down(0, j)
            j -= 1
        return self.arr


if __name__ == "__main__":
    # logging.basicConfig(
    #     format='[%(asctime)s][LINE:%(lineno)d][%(name)s][%(levelname)s:] %(message)s',
    #     datefmt='%Y-%m-%d %H:%M:%S',
    #     # filename='log/sorts.log',
    #     level=logging.DEBUG)
    # logger = logging.getLogger(__name__)
    # logging.info("added %s and %s to get %s" % (x, y, x + y))

    # generate some integers
    A = [randint(0, 100) for _ in range(100_000)]

    print(A)
    # print(sort_bubble(A))

    heap = sort_heapsort(A)
    print(heap.heapsort()[::-1])
