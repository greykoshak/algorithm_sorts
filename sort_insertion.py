import time
from random import randint


def count_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        sort_array = func(*args, **kwargs)
        print("\n--- {} элементов: {:.2f} seconds ---\n".format(len(sort_array), time.time() - start_time))

        return sort_array

    return wrapper


class SortInsertion:
    """
    Сортировка вставками (англ. Insertion sort) — алгоритм сортировки, в котором элементы входной последовательности
    просматриваются по одному, и каждый новый поступивший элемент размещается в подходящее место среди ранее
    упорядоченных элементов[1]. Вычислительная сложность — O(n^2)
    Общая суть сортировок вставками такова:

    Перебираются элементы в неотсортированной части массива.
    Каждый элемент вставляется в отсортированную часть массива на то место, где он должен находиться.

    То есть, сортировки вставками всегда делят массив на 2 части — отсортированную и неотсортированную. Из
    неотсортированной части извлекается любой элемент. Поскольку другая часть массива отсортирована, то в ней достаточно
    быстро можно найти своё место для этого извлечённого элемента. Элемент вставляется куда нужно, в результате чего
    отсортированная часть массива увеличивается, а неотсортированная уменьшается. Всё. По такому принципу работают все
    сортировки вставками.

    :param arr: Неотсортированный массив
    :return: Отсортированный массив
    """

    def __init__(self, arr: list):
        self.arr = arr

    @count_time
    def insertion(self):
        for i in range(len(self.arr)):
            j = i - 1
            key = self.arr[i]

            while self.arr[j] > key and j >= 0:
                self.arr[j + 1] = self.arr[j]
                j -= 1

            self.arr[j + 1] = key

        return self.arr


if __name__ == "__main__":
    # generate some integers
    A = [randint(0, 25_000) for _ in range(25_000)]

    print(A)
    ins = SortInsertion(A)
    print(ins.insertion()[::-1])
