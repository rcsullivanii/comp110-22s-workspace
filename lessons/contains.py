"""Example of a function that searches through a list."""


def main() -> None:
    print(contains("Kevin Bacon", ["Kanye West", "Kevin Bacon"]))


# Define a function named contains
# Two parameters 
# 1. needle - the string we're searching for
# 2. haystack - the list we're searching through
# Algorithm:
# For each item in the haystack
#   Test if it is equal to the need
#       If so, return True
#   After testing all items, return False, because not found
# Returns true if needle in haystack, false otherwise


def contains(needle: str, haystack: list[str]) -> bool:
    for hay in haystack:
        if (hay == needle):
            return True
    return False


if __name__ == "__main__":
    main()
    print(__name__)
else:
    print(__name__)