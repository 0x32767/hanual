from __future__ import annotations

from typing import Any, TYPE_CHECKING, Dict
from .base_node import BaseNode
from .block import CodeBlock
from abc import ABC


if TYPE_CHECKING:
    from .conditions import Condition
    from .block import CodeBlock


class IfStatement(BaseNode, ABC):
    def __init__(self: IfStatement, condition: Condition, block: CodeBlock) -> None:
        self._condition: Condition = condition
        self._block: CodeBlock = block

    @property
    def condition(self) -> Condition:
        return self._condition

    @property
    def block(self) -> CodeBlock:
        return self._block

    def compile(self) -> None:
        raise NotImplementedError

    def as_dict(self) -> Dict[str, Any]:
        return super().as_dict()
