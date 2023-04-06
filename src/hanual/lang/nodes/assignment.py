from __future__ import annotations

from typing import TypeVar, Generic, Any
from .base_node import BaseNode


T = TypeVar("T", bound=BaseNode)
A = TypeVar("A")
B = TypeVar("B")


class AssighnmentNode(BaseNode, Generic[A, B]):
    __slots__ = ("_target", "_value")

    def __init__(self: BaseNode, target: A, value: B) -> None:
        self._target: A = target
        self._value: B = value

    def compile(self) -> Any:
        return super().compile()

    def eval(self: BaseNode, context) -> Any:
        return super().eval(context)

    @property
    def target(self) -> A:
        return self._target

    @property
    def value(self) -> B:
        return self._value

    def __str__(self, level=0) -> str:
        return f"{type(self).__name__}(\n{' '.rjust(level)}target = {self.target.__str__(level+1) if issubclass(type(self.target), BaseNode) else str(str(self.target))}\n{' '.rjust(level)}value = {self.value.__str__(level+1) if issubclass(type(self.value), BaseNode) else str(str(self.value))}\n{' '.rjust(level)})"