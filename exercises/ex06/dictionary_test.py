"""Dictionary test in ex06 directory."""

__author__ = "730472431"

from dictionary import invert, count, favorite_color
import pytest


"""Tests for the invert function in ex06 dictionary exercise."""


def test_invert_use_case1() -> None:
    """Tests the inverted dictionary of two strings."""
    d: dict[str, str] = {"Robert": "18", "Erin": "22", "Mary": "25"}
    invert(d) == {"18": "Robert", "22": "Erin", "25": "Mary"}


def test_invert_use_case2() -> None:
    """Tests the inverted dictionary of two strings."""
    d: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    invert(d) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_edge_case1() -> None:
    """Tests the inverted dictionary of two empty strings."""
    d: dict[str, str] = {}
    assert invert(d) == {}


def test_invert_edge_case2() -> None:
    """Tests for when an inverted case raises a key error."""
    with pytest.raises(KeyError):
        d = {'kris': 'jordan', 'michael': 'jordan'}
        invert(d)


"""Tests for the favorite colors function in ex06 exercise."""


def test_favorite_color_use_case1() -> None:
    """Tests the favorite color function of a str-str use case dictionary."""
    assert favorite_color({"Rob": "green", "Mark": "red", "Oliver": "red"}) == "red"


def test_favorite_color_use_case2() -> None:
    """Tests the favorite color function of a str-str use case dictionary."""
    assert favorite_color({"Rob": "Yellow", "Sam": "Blue", "Asheley": "Blue"}) == "Blue"


def test_favorite_color_edge1() -> None:
    """Tests the favorite color function when two colors appear the same amount of times."""
    assert favorite_color({"Rob": "Yellow", "Sam": "Blue", "Asheley": "Blue", "Jack": "Yellow", "John": "Blue"}) == "Blue"


def test_favorite_color_use_edge2() -> None:
    """Tests the favorite color function of an empty dictionary."""
    assert favorite_color({}) == ""


"""Tests for the count function in ex06 exercise."""


def test_count_edge_case() -> None:
    """Tests the count funcation for an empty list."""
    l: list[str] = []
    assert count(l) == {}


def test_count_use_case1() -> None:
    """Tests the count function for a use case list."""
    l: list[str] = ["r", "r", "d", "e", "r", "r", "f"]
    assert count(l) == {"r": 4, "d": 1, "e": 1, "f": 1}


def test_count_use_case2() -> None:
    """Tests the count functino for a use case list."""
    l: list[str] = ["d", "J", "J", "e"]
    assert count(l) == {"d": 1, "J": 2, "e": 1}


def test_count_use_case3() -> None:
    """Tests the count function for a use case list."""
    l: list[str] = ["r", "r", "d", "e", "r", "r", "f", "r", "r", "d", "e", "r", "r", "f"]
    assert count(l) == {"r": 8, "d": 2, "e": 2, "f": 2}