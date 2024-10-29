from __future__ import annotations

from typing import TYPE_CHECKING

from hanual.lang.nodes.base_node import BaseNode
from hanual.lang.util.type_objects import GENCODE_RET, PREPARE_RET

if TYPE_CHECKING:
    from .arguments import Arguments


class HanualList(BaseNode):
    __slots__ = "_elements", "_lines", "_line_range"

    def __init__(self, args: Arguments) -> None:
        self._elements = args

    @property
    def elements(self) -> list:
        return self._elements.children

    def gen_code(self, intents: list[str], **options) -> GENCODE_RET:
        raise NotImplementedError

    def prepare(self) -> PREPARE_RET:
        raise NotImplementedError
