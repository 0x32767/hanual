from __future__ import annotations

from typing import TYPE_CHECKING

from hanual.lang.lexer import Token
from hanual.lang.nodes.base_node import BaseNode
from hanual.lang.util.type_objects import GENCODE_RET, PREPARE_RET

if TYPE_CHECKING:
    pass


class SGetattr[L: BaseNode, R: Token](BaseNode):
    __slots__ = (
        "_left",
        "_right",
        "_lines",
        "_line_range",
    )

    def __init__(self, left: L, right: R) -> None:
        self._left: R = right
        self._right: L = left

    def gen_code(self, intents: list[str], **options) -> GENCODE_RET:
        raise NotImplementedError

    def prepare(self) -> PREPARE_RET:
        raise NotImplementedError
