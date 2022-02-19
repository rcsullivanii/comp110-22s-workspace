"""utils_test folder in ex05 directory."""

__author__ = "730472431"

from exercises.ex05.utils import only_evens, sub, concate

"""Tests for the only_evens function"""


def test_only_evens_empty() -> None:
    """Tests an empty list"""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_multiple_odd() -> None:
    """Tests a list containing only odd numbers"""
    xs: list[int] = [1, 3, 5, 7]
    assert only_evens(xs) == []
    

def test_only_evens_mix1() -> None:
    """Tests a mixed list of odd and even"""
    xs: list[int] = [1, 3, 5, 7, 8]
    assert only_evens(xs) == [8]


def test_only_evens_mix2() -> None:
    """Tests a mixed list of odd and even"""
    xs: list[int] = [1, 2, 3, 6, 16, 222222, 1]
    assert only_evens(xs) == [2, 6, 16, 222222]


"""Tests for the sub function"""


def test_sub_empty() -> None:
    """Tests an empty list with a and b equal to 0"""
    xs: list[int] = []
    assert sub(xs, 0, 0) == []


def test_sub_in_domains() -> None:
    """Tests that the program will repond correctly with a >= 0 and b <= (len(xs) - 1)"""
    xs: list[int] = [1, 2, 3, 4, 5, 6, 12]
    assert sub(xs, 0, 6) == [1, 2, 3, 4, 5, 6]


def test_sub_negative_a() -> None:
    """Tests that the program will repond correctly with a < 0 and b <= (len(xs) - 1)"""
    xs: list[int] = [4, 5, 3, 2, 1, 6, 10]
    assert sub(xs, -3, 2) == [4, 5]


def test_sub_large_b() -> None:
    """Tests that the program will repond correctly with a >= 0 and b > (len(xs) - 1)"""
    xs: list[int] = [4, 5, 6, 7, 8, 9]
    assert sub(xs, 1, 9) == [5, 6, 7, 8, 9]


def test_sub_negative_a_and_large_b() -> None:
    """Tests that the program will repond correctly with a < 0 and b > (len(xs) - 1)"""
    xs: list[int] = [1112, 35, 4, 3, 2, 1]
    assert sub(xs, -5, 30) == [1112, 35, 4, 3, 2, 1]


"""Tests for the concate function"""


def test_concate_empty() -> None:
    """Tests concatenating two empty lists"""
    xs: list[int] = []
    ys: list[int] = []
    assert concate(xs, ys) == []


def test_concate_one_empty() -> None:
    """Tests concatenating one empty list and one list with elements"""
    xs: list[int] = []
    ys: list[int] = [3, 4, 5]
    assert concate(xs, ys) == [3, 4, 5]


def test_concate_with_elements1() -> None:
    """Tests concatenating two lists"""
    xs: list[int] = [5, 6, 8]
    ys: list[int] = [3, 4, 5]
    assert concate(xs, ys) == [5, 6, 8, 3, 4, 5]


def test_concate_with_elements2() -> None:
    """Tests concatenating two lists"""
    xs: list[int] = [123456789]
    ys: list[int] = [2, 3]
    assert concate(xs, ys) == [123456789, 2, 3]