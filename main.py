# task_1_3
def two_max_pow(a,b,c):
    if a > b and b > c:
        return a**2 + b**2

    elif a > b and c > b:
        return a**2 + c**2

    return b ** 2 + c ** 2


# task_1_5 and task_1_6
def sum_of_range(a,b):
    if a > b:
        a, b = b, a

    _sum = 0

    for i in range(a,b + 1,1):
        _sum += i

    return _sum


# task_1_7
def _pow(a, b):
    if b == 0:
        if a == 0:
            return "Undefined"
        return 1

    if b > 0:
        return a ** b

    if b < 0:
        if a == 0:
            return "Can't divide by 0"
        return 1 / a ** (-b)


# task_1_8
def cube_root(n):
    root = 1

    while not enough(root, n):
        root = improve(root, n)
    return root


def enough(value, target):
    if _abs(value ** 3 - target) < 0.00001:
        return True
    else:
        return False


def _abs(n):
    if n > 0:
        return n
    else:
        return -n


def improve(root, target):
    return ((target / (root ** 2)) + (2 * root)) / 3


# task_1_11
def f_rec(n):
    if n < 0 or type(n) != int:
        return 'Wrong input'

    if n < 3:
        return n

    return f_rec(n - 1) + f_rec(n - 2) + f_rec(n - 3)


def f_iter(n):
    if n < 0 or type(n) != int:
        return 'Wrong input'
    f = n
    f1 = 0
    f2 = 1
    f3 = 2

    for i in range(3, n + 1, 1):
        f = f1 + f2 + f3
        f1 = f2
        f2 = f3
        f3 = f

    return f


def f_tail_rec(n, f1=0, f2=1, f3=2):
    if n < 0 or type(n) != int:
        return 'Wrong input'

    if n < 3:
        lst = [f1, f2, f3]
        return lst[n]

    return f_tail_rec(n - 1, f2, f3, f1 + f2 + f3)

