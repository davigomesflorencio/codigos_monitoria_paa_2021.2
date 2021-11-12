import math

# floor -> PISO
# ceil -> TETO


def pot(b, n):
    if n == 0:
        return 1
    elif n == 1:
        return b
    else:
        # s1 = pot(b, math.floor(n/2))
        # s2 = pot(b, math.ceil(n/2))
        # return s1 * s2
        return pot(b, math.floor(n/2)) * pot(b, math.ceil(n/2))


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


def potG(b, n):
    # if n == 0 and b==0:
    #     return 0
    if n == 1:
        return b
    if n == 0:
        return 1
    else:
        # s1 = potG(b, (n/2))
        if n % 2 == 0:
            return potG(b, (n/2)) * potG(b, (n/2))
        return potG(b, (n/2)) * potG(b, (n/2)) * b


if __name__ == '__main__':
    # print(pot(3, 4))
    print(pot2(2, 1000000))
    # print(pot2(2, 10000000000))

    # print(2**1000000)
