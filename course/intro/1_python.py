import random
from math import sqrt

def task_1():
    name = input("Enter your name: ")
    print("Hello, %s!" % name)


def task_2():
    a = int(input("Enter first num: "))
    b = int(input("Enter second num: "))
    c = int(input("Enter third num: "))
    print("Sum of 3 num: %s" % str(a + b + c))


def task_3():
    num = input("Enter the number:")
    print("The next number is %s " % str(int(num) + 1))


def task_4():
    square = input("Please enter square: ")
    a = sqrt(int(square))
    print("Side is %s" % str(a))


def task_5():
    print("Enter sides of triangle")
    side1 = int(input("Enter first side : "))
    side2 = int(input("Enter second side : "))
    side3 = int(input("Enter third side : "))

    def get_perimeter():
        return side1 + side2 + side3

    def get_square():
        half_perimeter = get_perimeter() / 2
        return sqrt(half_perimeter * (half_perimeter - side1) * (half_perimeter - side2) - (half_perimeter - side3))

    print("Perimeter: %s" % str(get_perimeter()))
    print("Square: %s" % str(get_square()))


def task_6():
    sum = int(input("Enter credit sum: "))
    percent = int(input("Enter percent: "))
    total = sum / percent + sum
    print("Total : %s" % str(total))


def task_7():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print("a + b = %s" % str(a + b))
    print("a - b = %s" % str(a - b))
    print("a * b = %s" % str(a * b))
    print("a / b = %s" % str(a / b))
    print("a // b = %s" % str(a // b))


def task_8():
    a = int(input("Enter min: "))
    b = int(input("Enter max: "))
    rand = random.uniform(a, b)
    print("Randon for range %s : %s is %s" % (a, b, rand))


def task_9():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    if a < b:
        print("Min for range %s : %s is %s" % (a, b, a))
    elif a > b:
        print("Min for range %s : %s is %s" % (a, b, b))
    else:
        print("Min for range %s : %s is equal" % (a, b))


def task_10():
    a = int(input("Enter a: "))
    if a > 0:
        print("Sign a is %s " % 1)
    elif a < 0:
        print("Sign a is %s " % -1)
    elif a == 0:
        print("Sign a is %s " % -1)


def task_11():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    op = input("Enter operation: ")
    if op in ('+', '-', '*', '/', '//'):
        if op == '+':
            print("a + b = %s" % str(a + b))
        elif op == '-':
            print("a - b = %s" % str(a - b))
        elif op == '*':
            print("a * b = %s" % str(a * b))
        elif op == '/':
            print("a / b = %s" % str(a / b))
        elif op == '//':
            print("a // b = %s" % str(a // b))
    else:
        print("Invalid operation")


def task_12():
    print("Solve ax^2 + bx + c")
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))

    D = b ** 2 - 4 * a * c

    if D > 0:
        x1 = (-b + sqrt(D)) / -b * a
        x2 = (-b - sqrt(D)) / -b * a
        print("x1 = %s, x2 = %s," % (str(x1), str(x2)))

    elif D == 0:
         x = (-b + sqrt(D)) / -b * awe
         print("x = %s" % str(x))

    else:
        print("Have no roots D = %s" % str(D))


def task_13():
    total_minutes = int(input("Enter minutes: "))
    total_sms = int(input("Enter sms: "))
    cost_per_month = 30
    month_minutes = 100
    month_sms = 30
    cost_over_sms = 0.25
    cost_over_minute = 0.3

    if total_sms < total_sms and total_minutes < total_minutes:
        print("Month price: %s" % str(cost_per_month))
    else:
        num_over_sms = total_sms - month_sms
        price_over_sms = num_over_sms * cost_over_sms
        num_over_minutes = total_minutes - month_minutes
        price_over_minutes = num_over_minutes * cost_over_minute
        total_price = cost_per_month + price_over_sms + price_over_minutes
        print("Month price: %s" % str(total_price))


def task_14():
    letter = input("Enter letter: ")
    vowels = 'aeiouyAEIOUY'
    consonants = 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ'
    if letter in vowels:
        print("%s is vowel")
    elif letter in consonants:
        print("%s is consonant")


def task_15():
    a = int(input("Enter first side: "))
    b = int(input("Enter second side: "))
    c = int(input("Enter third side: "))
    if a == b == c:
        print("equilateral triangle a = %s b = %s, c = %s" % (str(a), str(b), str(c)))
    elif a == b or a == c or c == b:
        print("Isosceles triangle a = %s b = %s, c = %s" % (str(a), str(b), str(c)))



def main():
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()
    task_6()
    task_7()
    task_8()
    task_9()
    task_10()
    task_11()
    task_12()
    task_13()
    task_14()
    task_15()


    # task_12()

def authenticate():
    # access_users = [("Ievgen", "123"), ("Anise", "123")]
    # current_user_name = input("Enter your name: ")
    # current_user_password = input("Enter your password: ")
    # if (current_user_name, current_user_password) in access_users:
    #     return True

    return True

if __name__ == "__main__":
    if authenticate():
        main()
    else:
        print("Access denied!")
