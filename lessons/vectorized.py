from __future__ import annotations
from typing import Union


class StrArray:
    items: list[str]

    def __init__(self, items: list[str]):
        self.items = items 

    def __repr__(self) -> str:
        return f"StrArray({self.items})"
    
    def __add__(self, rhs: Union[str, StrArray]) -> StrArray:
        """Vectorized concatenation operator."""
        result: list[str] = []
        if isinstance(rhs, str):
            for item in self.items:
                result.append(item + rhs)
        else:
            i: int = 0
            while (i < len(self.items)):
                result.append(self.items[i] + " " + rhs.items[i])
                i += 1
        return StrArray(result)


first: StrArray = StrArray(["Armando", "Brady", "Caleb"])
last: StrArray = StrArray(["Bacot", "Manek", "Love"])
results: StrArray = first + "!"
print(results)
print(first + last + "!")