trees: list[int] = [2, 3, 4, 7]


def harvest(trees: list[int]) -> list[int]:
    # for tree in trees:
    #     if (tree > 5):
    #         tree = 1
    # i: int = 0
    # while (i < len(trees)):
    #     if trees[i] > 5:
    #         trees[i] = 1
    #     i += 1
    if 7 in trees:
        return []
    return trees


print(harvest(trees))