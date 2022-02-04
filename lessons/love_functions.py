def love(name: str) -> str:
    """Given a name as a parameter, returns a loving string."""
    return f"I love you, {name}"


def spread_love(to: str, n: int) -> str:
    """Generates a string that repeats a loving message n times."""
    love_note: str = ""
    i: int = 0
    while (n > i):
        love_note += f"I love you, {to}\n"
    return love_note