from __future__ import annotations


from dataclasses import dataclass
from typing import Sequence, NoReturn, Literal, TypeGuard, Any


class PositiveInfinity:
    def __gt__(self, other) -> Literal[True]:
        assert isinstance(other, int), f"Can't compare {type(self).__name__} to {type(other).__name__}"
        return True

    def __ge__(self, other) -> Literal[True]:
        assert isinstance(other, int), f"Can't compare {type(self).__name__} to {type(other).__name__}"
        return True

    def __lt__(self, other) -> Literal[False]:
        assert isinstance(other, int), f"Can't compare {type(self).__name__} to {type(other).__name__}"
        return False

    def __le__(self, other) -> Literal[False]:
        assert isinstance(other, int), f"Can't compare {type(self).__name__} to {type(other).__name__}"
        return False


class NegativeInfinity:
    def __gt__(self, other) -> Literal[False]:
        assert isinstance(other, int), f"Can't compare {type(self).__name__} to {type(other).__name__}"
        return False

    def __ge__(self, other) -> Literal[False]:
        assert isinstance(other, int), f"Can't compare {type(self).__name__} to {type(other).__name__}"
        return False

    def __lt__(self, other) -> Literal[True]:
        assert isinstance(other, int), f"Can't compare {type(self).__name__} to {type(other).__name__}"
        return True

    def __le__(self, other) -> Literal[True]:
        assert isinstance(other, int), f"Can't compare {type(self).__name__} to {type(other).__name__}"
        return True


@dataclass()
class LineRange:
    start: int | PositiveInfinity | NegativeInfinity
    end: int | PositiveInfinity | NegativeInfinity

    def to_range(self) -> Sequence[int] | NoReturn:
        if not isinstance(self.start, int):
            raise ValueError("starting value is not a number")

        if not isinstance(self.end, int):
            raise ValueError("ending value is not a number")

        return range(self.start, self.end+1)
