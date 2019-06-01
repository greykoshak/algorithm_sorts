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

    def partition(array, start, end):
        pivot = array[(start + end) // 2]
        i = start
        j = end

        while i <= j:
            while array[i] < pivot:
                i += 1
            while array[j] > pivot:
                j -= 1
            if i <= j:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp

                i += 1
                j -= 1

        return i

    @count_time
    def quick_pas(self, array, start, end):
        if start < end:
            temp = partition(array, start, end)

            quick_pas(array, start, temp - 1)
            quick_pas(array, temp, end)

        return self.arr


if __name__ == "__main__":
    # generate some integers
    A = [randint(0, 100_000) for _ in range(100_000)]

    print(A)
    quick = SortQuick(A, 0, len(A)-1)
    print(quick.quick_pas()[::-1])

"""
На сладкое, привожу вам вариант, которому меня научил в университете великий Деон!) Версия избавлена от рекурсии, 
классическим способом - введением стека, в котором хранятся границы наших интервалов.

http://py-algorithm.blogspot.com/2011/11/quicksort.html

def QuickSort(a):
    w = [x for x in xrange(4 + len(a) / 2)]#создаём стек
    k = 0#дно
    w[0] = 0#указатель на позицию левой границы половины
    w[1] = len(a) - 1#-||- правой
    while (k >= 0):
        i = QuickSortPos(a, w[k], w[k + 1])
        if(i != w[k + 1]):RL =i + 1#левая граница правого подъинтервала
        else:RL =w[k + 1]
        RR = w[k + 1]#Правая граница правого подъинтервала
        LL = w[k]#Левая граница левого подъинтервал
        if(i != w[k]):LR =i - 1#Правая граница левого подъинтервал
        else:LR =w[k]
        k -= 2#удалить текущий интервал
        if (RL != RR):k += 2; w[k] = RL; w[k + 1] = RR
        if (LL != LR):k += 2; w[k] = LL; w[k + 1] = LR
    return

def QuickSortPos(a, left, right):
    i = left
    j = right - 1
    while (True):#чтобы поставить разделяющий элемент на свое место
        while (a[i] < a[right]): i+=1
        while (a[j] > a[right] and j > left): j-=1
        if (i >= j): break
        a[i],a[j] = a[j],a[i]
    a[right],a[i]  = a[i],a[right]
    return i

Сразу скажу, что он показывает максимальную производительность из все виденных мной.

"""
