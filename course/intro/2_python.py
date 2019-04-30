import math
from functools import reduce

import numpy


def task_1():
    number_of_int = int(input("Enter number of integers: "))
    numbers = []

    for i in range(number_of_int):
        i_number =  input("Enter %s of integers: " % str(i))
        numbers.append(i_number)
    min_of_list = min(numbers)
    print("Minimum is %s" % str(min_of_list))


def task_2():
    print("Enter number while input negative int: ")

    while True:
        number = float(input("Enter integer: "))
        if number < 0:
            break
        sqrt_of_num = math.sqrt(number)
        print("Sqrt of %s is %s" % (number, sqrt_of_num))


def task_3():
    number_of_int = int(input("Enter number of integers: "))
    operation = input("Enter operation (+ or *): ")
    numbers = []

    for i in range(number_of_int):
        i_number = float(input("Enter %s of integers: " % str(i)))
        numbers.append(i_number)

    if operation == "+":
        result = reduce((lambda x, y: x + y), numbers)
        print("Result is:", result)

    elif operation == "*":
        result = reduce((lambda x, y: x * y), numbers)
        print("Result is:", result)


def task_4():
    number_of_int = int(input("Enter number of Fibonacci : "))
    first = 1
    fibo_list = []

    for i in range(1, number_of_int):
        if not fibo_list:
            fibo_list.append(first)
            fibo_list.append(first + first)
        else:
            fibo_list.append(fibo_list[-2] + fibo_list[-1])

    print("Fibonacci list: ", fibo_list)


def task_5():
    fibo_limit = int(input("Enter limit of Fibonacci : "))
    first = 1
    fibo_list = []
    fibo_i = first

    while fibo_limit > fibo_i:
        if not fibo_list:
            fibo_i = first + first
            fibo_list.append(first)
            fibo_list.append(fibo_i)
        else:
            fibo_i = fibo_list[-2] + fibo_list[-1]
            fibo_list.append(fibo_i)

    print("Fibonacci list: ", fibo_list)


def task_6():
    startind_value = float(input("Enter starting value : "))
    endind_value = float(input("Enter ending value : "))
    step = float(input("Enter ending value : "))

    c_list = [round(c, 2) for c in numpy.arange(startind_value, endind_value, step)]
    f_list = list(map(lambda x: round(x * 9 / 5 + 32, 2), c_list))
    print("C :", c_list)
    print("F :", f_list)


def task_7():
    pass


def main_flow():
    # task_1()
    # task_2()
    # task_3()
    # task_4()
    # task_5()
    # task_6()
    task_7()


if __name__ == "__main__":
    main_flow()