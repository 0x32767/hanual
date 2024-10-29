from __future__ import annotations

from typing import TYPE_CHECKING

from hanual.lang.nodes.base_node import BaseNode
from hanual.lang.util.type_objects import GENCODE_RET, PREPARE_RET

if TYPE_CHECKING:
    from hanual.lang.lexer import Token


class StrongField[T](BaseNode):
    __slots__ = (
        "_name",
        "_type",
        "_lines",
        "_line_range",
    )

    def __init__(self, name: Token, type_: T) -> None:
        self._name: Token = name
        self._type: T = type_

    @property
    def name(self) -> Token:
        return self._name

    @property
    def type(self) -> T:
        return self._type

    def gen_code(self, intents: list[str], **options) -> GENCODE_RET:
        raise NotImplementedError

    def prepare(self) -> PREPARE_RET:
        raise NotImplementedError
