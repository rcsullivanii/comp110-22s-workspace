"""An example of Union types."""

from typing import Union


def log(info: Union[int, str]) -> None:
    """Log is a function that can be called with either an int or a str argument."""
    if isinstance(info, str):
        print(f"str: {info}")
    else:
        print(f"int: {info}")


log("Hello, world")
log(110)