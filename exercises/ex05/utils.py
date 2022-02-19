"""untils folder in ex05 directory."""

__author__ = "730472431"


def only_evens(xs: list[int]) -> list[int]:
    """Takes a list of ints and returns only the even ints."""
    evens: list[int] = list()
    i: int = 0
    while (i < len(xs)):
        if (xs[i] % 2 == 0):
            evens.append(xs[i])
        i += 1
    return evens


def sub(xs: list[int], a: int, b: int) -> list[int]:
    """Takes a list of ints and returns the list form a, inclusive, to b, non inclusive."""
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
        while (a < (len(xs))):
            short.append(xs[a])
            a += 1
    else:
        while (i < (len(xs))):
            short.append(xs[i])
            i += 1
    return short


def concat(xs: list[int], ys: list[int]) -> list[int]:
    """Takes two lists of ints and returns a list concatenating the elements of the first list with those of the second."""
    concat: list[int] = list()
    i: int = 0
    j: int = 0
    while (i < len(xs)):
        concat.append(xs[i])
        i += 1
    while (j < len(ys)):
        concat.append(ys[j])
        j += 1
    return concat