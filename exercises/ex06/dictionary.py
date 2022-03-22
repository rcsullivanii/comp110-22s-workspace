"""Dictionary exercise in ex06 directory."""

__author__ = "730472431"


def invert(d: dict[str, str]) -> dict[str, str]:
    """Inverts dictionary."""
    inverted_d: dict[str, str] = {}
    for keys in d:
        if (d[keys] in inverted_d):
            raise KeyError("Error")
        inverted_d[d[keys]] = keys
    return inverted_d


def favorite_color(d: dict[str, str]) -> str:
    """Returns most appeared color of str values."""
    colors_list: list[str] = []
    for colors in d:
        colors_list.append(d[colors])
    colors_dict: dict[str, int] = count(colors_list)
    highest: int = 0
    fav: str = ""
    for colors in colors_dict:
        if (colors_dict[colors] > highest):
            highest = colors_dict[colors]
            fav = colors
    return fav


def count(count_list: list[str]) -> dict[str, int]:
    """Counts the number of times a str value has appeared."""
    count_dict: dict[str, int] = {}
    i: int = 0
    while (i < len(count_list)):
        if (count_list[i] in count_dict):
            count_dict[count_list[i]] += 1
        else:
            count_dict[count_list[i]] = 1
        i += 1
    return count_dict