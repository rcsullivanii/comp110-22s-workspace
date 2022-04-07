"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730472431"


class Simpy:
    """Create a Simpy object with a list[float]."""
    values: list[float]

    def __init__(self, values: list[float] = []):
        """Initialize the values attribute with argument."""
        self.values = values
    
    def __str__(self) -> str:
        """Return str in the format of Simply(...} where elipses are repaced with list[str] literal."""
        return f"Simpy({self.values})"

    def fill(self, num: float, total: int) -> None:
        """Create a total-length list[float] where each float is mutated to num."""
        self.values = []
        i: int = 0
        while (i < total):
            self.values.append(num)
            i += 1
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in the values attribute with range of values, like the range built-in function, but in terms of floats."""
        assert step != 0.0
        total: int = int(abs((stop - start) // step))
        i: int = 0
        value: float = start
        while (i < total):
            self.values.append(value)
            value += step
            i += 1

    def sum(self) -> float:
        """Compute and return sum of all items in the values attribute."""
        return sum(self.values)

    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
        """The left-hand side either a Simpy object or a float value, returns a new Simpy object."""
        total: list[float] = []
        if isinstance(rhs, Simpy):
            assert(len(self.values) == len(rhs.values))
            i: int = 0
            while (i < len(self.values)):
                total.append(self.values[i] + rhs.values[i])
                i += 1
        else:
            i: int = 0
            while (i < len(self.values)):
                total.append(self.values[i] + rhs)
                i += 1
        return Simpy(total)

    def __pow__(self, rhs: Union[Simpy, float]) -> Simpy:
        """The left-hand side either a Simpy object or a float value, returns a new Simpy object."""
        total: list[float] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while (i < len(self.values)):
                total.append(self.values[i] ** rhs.values[i])
                i += 1
        else:
            i: int = 0
            while (i < len(self.values)):
                total.append(self.values[i] ** rhs)
                i += 1
        return Simpy(total)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """A mask list[bools] based on equality of each item in the values attribute."""
        result: list[bool] = []
        if isinstance(rhs, Simpy):
            assert(len(self.values) == len(rhs.values))
            i: int = 0
            while(i < len(self.values)):
                result.append(self.values[i] == rhs.values[i])
                i += 1
        else:
            i: int = 0
            while(i < len(self.values)):
                result.append(self.values[i] == rhs)
                i += 1
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """A mask list[bools] based on equality of each item in the values attribute."""
        result: list[bool] = []
        if isinstance(rhs, Simpy):
            assert(len(self.values) == len(rhs.values))
            i: int = 0
            while(i < len(self.values)):
                result.append(self.values[i] > rhs.values[i])
                i += 1
        else:
            i: int = 0
            while(i < len(self.values)):
                result.append(self.values[i] > rhs)
                i += 1
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Subscription operator to reach specific indexes in list[float]."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            result: list[float] = []
            i: int = 0
            while(i < len(rhs)):
                if (rhs[i]):
                    result.append(self.values[i])
                i += 1
            return Simpy(result)