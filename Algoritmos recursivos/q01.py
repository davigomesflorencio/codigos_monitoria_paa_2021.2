import math


def pot(b, n):
    if n == 0:
        return 1
    elif n == 1:
        return b
    else:
        s1 = pot(b, math.floor(n/2))
        s2 = pot(b, math.ceil(n/2))
        return s1 * s2


def pot2(b, n):
    if n == 0:
        return 1
    elif n == 1:
        return b
    else:
        s1 = pot2(b, math.floor(n/2))
        if n % 2 == 0:
            return s1 * s1
        return s1 * s1 * b


if __name__ == '__main__':
    # print(pot(3, 4))
    print(pot2(2, 1000000))
    # print(2**1000000)
