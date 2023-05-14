from __future__ import annotations
from hanual.compile import Assembler

from hanual.lang.lexer import Token
from typing import Any, Dict, Union
from .base_node import BaseNode


class AlgebraicExpression(BaseNode):
    __slots__ = "_op", "_left", "_right"

    def __init__(
        self: BaseNode,
        operator: Token,
        left: Union[AlgebraicExpression, Token],
        right: Union[AlgebraicExpression, Token],
    ) -> None:
        self._op = operator
        self._left = left
        self._right = right

    def as_dict(self) -> Dict[str, Any]:
        return {
            "op": self._op,
            "left": self.get_repr(self._left),
            "right": self.get_repr(self._right),
        }

    def compile(self, global_state: Assembler) -> Any:
        return super().compile(global_state)