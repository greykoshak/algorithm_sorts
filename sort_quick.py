import time
from random import randint


def count_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        sort_array = func(*args, **kwargs)
        print("\n--- {} элементов: {:.2f} seconds ---\n".format(len(sort_array), time.time() - start_time))

        return sort_array

    return wrapper


class SortQuick:
    """
    Быстрая сортировка(quicksort, сортировка Хоара): http://aliev.me/runestone/SortSearch/TheQuickSort.html

    Один из быстрых известных универсальных алгоритмов сортировки массивов (в среднем O(n log n) обменов при
    упорядочении n элементов), хотя и имеющий ряд недостатков. Например, в худшем случае (на некоторых входных массивах)
    использует время Ω(n2), что, например, хуже, чем сложность в наихудшем случае алгоритма сортировки слиянием.

    Функция QuickSort сводит сортировку данного ей массива к разделению (partitioning) этого массива на две группы
    элементов и сортировке этих двух групп по отдельности.

    Два дополнительный параметра aL и aR указывают на номер первого и последнего элемента того фрагмента списка, который
    нужно отсортировать (включая эти элементы), то есть элемент сортирует срез A[l:r+1]. Для сортировки всего списка A
    необходимо вызвать QuickSort(A, 0, len(A) – 1).

    :param arr: Неотсортированный массив
    :return: Отсортированный массив
    """

    def __init__(self, arr: list, start: int, end: int):
        self.arr = arr
        self.start = start
        self.end = end

    def partition(self, start, end):
        pivot = self.arr[(start + end) // 2]
        i = start
        j = end

        while i <= j:
            while self.arr[i] < pivot:
                i += 1
            while self.arr[j] > pivot:
                j -= 1
            if i <= j:
                temp = self.arr[i]
                self.arr[i] = self.arr[j]
                self.arr[j] = temp

                i += 1
                j -= 1

        return i

    @count_time
    def quick_pas(self, start, end):
        if start < end:
            temp = self.partition(start, end)

            self.quick_pas(start, temp - 1)
            self.quick_pas(temp, end)

        return self.arr


if __name__ == "__main__":
    # generate some integers
    A = [randint(0, 100_000) for _ in range(100_000)]

    print(A)
    quick = SortQuick(A, 0, len(A)-1)
    print(quick.quick_pas(0, len(A)-1)[::-1])
