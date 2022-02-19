"""untils folder in ex05 directory."""

__author__ = "730472431"


def only_evens(xs: list[int]) -> list[int]:
    evens: list[int] = list()
    i: int = 0
    while (i < len(xs)):
        if (xs[i] % 2 == 0):
            evens.append(xs[i])
        i += 1
    return evens


def sub(xs: list[int], a: int, b: int) -> list[int]:
    short: list[int] = list()
    i: int = 0
    if (a >= 0 and b <= (len(xs) - 1)):
        while (a < b):
            short.append(xs[a])
            a += 1
    elif (a < 0 and b <= (len(xs) - 1)):
        while (i < b):
            short.append(xs[i])
            i += 1
    elif (a >= 0 and b > (len(xs) - 1)):
        while (a < (len(xs) - 1)):
            short.append(xs[a])
            a += 1
    else:
        while (i < (len(xs) - 1)):
            short.append(xs[i])
            i += 1
    return short


def concate(xs: list[int], ys: list[int]) -> list[int]:
    concate: list[int] = list()
    i: int = 0
    j: int = 0
    while (i < len(xs)):
        concate.append(xs[i])
        i += 1
    while (j < len(ys)):
        concate.append(ys[j])
        j += 1
    return concate