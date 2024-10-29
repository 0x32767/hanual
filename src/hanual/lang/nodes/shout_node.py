from __future__ import annotations

from typing import TYPE_CHECKING

from hanual.lang.util.type_objects import GENCODE_RET, PREPARE_RET

from .base_node import BaseNode

if TYPE_CHECKING:
    from hanual.lang.lexer import Token


class ShoutNode(BaseNode):
    __slots__ = (
        "_st",
        "_lines",
        "_line_range",
    )

    def __init__(self, shout_token: Token) -> None:
        self._st = shout_token

    def gen_code(self) -> GENCODE_RET:
        raise NotImplementedError

    def prepare(self) -> PREPARE_RET:
        raise NotImplementedError
