"""Dictionary exercise in ex06 directory."""

__author__ = "730472431"


def invert(d: dict[str, str]) -> dict[str, str]:
    inverted_d: dict[str, str] = {}
    for keys in d:
        if (d[keys] in inverted_d):
            raise KeyError("Error")
        inverted_d[d[keys]] = keys
    return inverted_d


def favorite_color(d: dict[str, str]) -> str:
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
    count_dict: dict[str, int] = {}
    i: int = 0
    count: int = 1
    while (i < len(count_list)):
        if (count_list[i] in count_dict):
            count += 1
            count_dict[count_list[i]] = count
        else:
            count_dict[count_list[i]] = 1
        i += 1
    return count_dict


def index(colors: list[str]) -> int:
    i: int = 0
    count: int = 0
    highest: int = 0
    index: int = 0
    while (colors[i] in colors.pop(i) and len(colors) > 1):
        count += 1
        if (count > highest):
            index = i
            highest = count
    return index


print(favorite_color({"Rob": "Yellow", "Sam": "Blue", "Asheley": "Blue"}))