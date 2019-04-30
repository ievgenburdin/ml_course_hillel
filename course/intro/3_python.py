from functools import reduce
from pprint import pprint

import numpy


def task_1():
    n = int(input("Enter num row :"))
    m = int(input("Enter num cols :"))
    ll = [[i for i in range(m)] for _ in range(n)]

    pprint(ll)

    ranges = input("Enter three nums; (sep: ,)")
    a, b, c = int(ranges[0]), int(ranges[1]), int(ranges[2])
    pprint(ll[a][b:c])


def task_2():
    n = int(input("Enter num row :"))
    m = int(input("Enter num cols :"))
    ll = [[i for i in range(m)] for _ in range(n)]
    pprint(ll)
    numpy.array(ll)
    s = numpy.sum(ll, axis=0)
    pprint(s)
    # pprint(lr)


def task_3():
    n = int(input("Enter num row cols :"))
    new = numpy.zeros((n, n), int)
    numpy.fill_diagonal(new, 1)
    pprint(new)


def task_4():
    pass


if __name__ == "__main__":
    # task_1()
    # task_2()
    # task_3()
    task_4()
