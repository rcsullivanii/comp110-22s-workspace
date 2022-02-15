"""Example of writing a test subject."""


def sum(xs: list[float]) -> float:
    """Compute the sum of the list."""
    sum: float = 0.0
    for x in xs:
        sum += x
    return sum
