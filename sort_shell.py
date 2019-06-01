import time
from random import randint


def count_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        sort_array = func(*args, **kwargs)
        print("\n--- {} элементов: {:.2f} seconds ---\n".format(len(sort_array), time.time() - start_time))

        return sort_array

    return wrapper


class SortShell:
    """
    Сортировка Шелла (англ. Shell sort) — алгоритм сортировки, являющийся усовершенствованным вариантом сортировки
    вставками. Идея метода Шелла состоит в сравнении элементов, стоящих не только рядом, но и на определённом расстоянии
    друг от друга. Иными словами — это сортировка вставками с предварительными «грубыми» проходами.

    При сортировке Шелла сначала сравниваются и сортируются между собой значения, стоящие один от другого на некотором
    расстоянии d (о выборе значения d см. ниже). После этого процедура повторяется для некоторых
    меньших значений d, а завершается сортировка Шелла упорядочиванием элементов при d=1 (то есть обычной сортировкой
    вставками). Эффективность сортировки Шелла в определённых случаях обеспечивается тем, что элементы «быстрее» встают
    на свои места (в простых методах сортировки, например, пузырьковой, каждая перестановка двух элементов уменьшает
    количество инверсий в списке максимум на 1, а при сортировке Шелла это число может быть больше).
    Лучшая временна́я сложность достигает O(n log^2 n)

    :param arr: Неотсортированный массив
    :return: Отсортированный массив
    """

    def __init__(self, arr: list):
        self.arr = arr

    @count_time
    def shell(self):
        inc = len(self.arr) // 2

        while inc:
            for i, el in enumerate(self.arr):
                while i >= inc and self.arr[i - inc] > el:
                    self.arr[i] = self.arr[i - inc]
                    i -= inc
                self.arr[i] = el

            inc = 1 if inc == 2 else int(inc * 5.0 / 11)

        return self.arr


if __name__ == "__main__":
    # generate some integers
    A = [randint(0, 100_000) for _ in range(100_000)]

    print(A)
    shell = SortShell(A)
    print(shell.shell()[::-1])
