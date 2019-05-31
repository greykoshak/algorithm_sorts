import time
from random import randint


def count_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        sort_array = func(*args, **kwargs)
        print("--- {} элементов: {:.2f} seconds ---".format(len(sort_array), time.time() - start_time))

        return sort_array

    return wrapper


class SortSelection:
    """
    Сортировка выбором (Selection sort) — алгоритм сортировки. Может быть как устойчивый, так и
    неустойчивый. На массиве из n элементов имеет время выполнения в худшем, среднем и лучшем
    случае Θ(n2)
    Проходим по массиву в поисках максимального элемента. Найденный максимум меняем местами с
    последним элементом. Неотсортированная часть массива уменьшилась на один элемент (не включает
    последний элемент, куда мы переставили найденный максимум). К этой неотсортированной части
    применяем те же действия — находим максимум и ставим его на последнее место в неотсортированной
    части массива. И так продолжаем до тех пор, пока неотсортированная часть массива не уменьшится
    до одного элемента.

    :param arr: Неотсортированный массив
    :return: Отсортированный массив
    """

    def __init__(self, arr: list):
        self.arr = arr

    @count_time
    def selection(self):
        for i, e in enumerate(self.arr):
            mn = min(range(i, len(self.arr)), key=self.arr.__getitem__)  # Find position of min element
            # Внутри реализован генератор:
            # По всему дипазону вычисляется позиция минимального элемента

            self.arr[i], self.arr[mn] = self.arr[mn], e

        return self.arr


if __name__ == "__main__":
    # generate some integers
    A = [randint(0, 100) for _ in range(25_000)]

    print(A)
    sel = SortSelection(A)
    print(sel.selection()[::-1])
