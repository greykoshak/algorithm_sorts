# import logging

import time
from random import randint


def count_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        sort_array = func(*args, **kwargs)
        print("--- {} элементов: {:.4f} seconds ---".format(len(sort_array), time.time() - start_time))

        return sort_array

    return wrapper


class SortHeapsort:
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
    # generate some integers
    A = [randint(0, 100) for _ in range(100_000)]

    print(A)
    heap = SortHeapsort(A)
    print(heap.heapsort()[::-1])
