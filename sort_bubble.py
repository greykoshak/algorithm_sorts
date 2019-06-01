# import logging
import time
from random import randint


# logging.basicConfig(
#     format='[%(asctime)s][LINE:%(lineno)d][%(name)s][%(levelname)s:] %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S',
#     # filename='log/sorts.log',
#     level=logging.DEBUG)
# logger = logging.getLogger(__name__)
# logging.info("added %s and %s to get %s" % (x, y, x + y))


def count_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        sort_array = func(*args, **kwargs)
        print("\n--- {} элементов: {:.2f} seconds ---\n".format(len(sort_array), time.time() - start_time))

        return sort_array

    return wrapper


class SortBubble:
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

    def __init__(self, arr: list):
        self.arr = arr

    @count_time
    def sort_bubble(self):
        for bypass in range(1, len(self.arr)):
            for i in range(0, len(self.arr) - bypass):
                if self.arr[i] > self.arr[i + 1]:
                    self.arr[i], self.arr[i + 1] = self.arr[i + 1], self.arr[i]
        return self.arr


if __name__ == "__main__":
    # generate some integers
    A = [randint(0, 25_000) for _ in range(25_000)]

    print(A)
    bubble = SortBubble(A)
    print(bubble.sort_bubble())
