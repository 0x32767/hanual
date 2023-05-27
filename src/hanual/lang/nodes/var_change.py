from __future__ import annotations


from typing import Any, Dict, TypeVar, TYPE_CHECKING
from hanual.lang.lexer import Token
from .base_node import BaseNode


if TYPE_CHECKING:
    from hanual.compile import Assembler

T = TypeVar("T", bound=BaseNode)


class VarChange(BaseNode):
    def __init__(self: BaseNode, name: Token, value) -> None:
        self._name: Token = name
        self._value: T = value

    @property
    def name(self) -> Token:
        return self._name

    @property
    def value(self) -> T:
        return self._value

    def as_dict(self) -> Dict[str, Any]:
        return super().as_dict()

    def compile(self) -> None:
        raise NotImplementedError