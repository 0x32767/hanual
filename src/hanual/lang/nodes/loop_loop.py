from __future__ import annotations

from typing import TYPE_CHECKING

from hanual.lang.util.type_objects import PREPARE_RET

from .base_node import BaseNode
from .block import CodeBlock

if TYPE_CHECKING:
    pass


class LoopLoop(BaseNode):
    __slots__ = ("_inner", "_lines", "_line_range")

    def __init__(self, inner: CodeBlock) -> None:
        self._inner: CodeBlock = inner

    @property
    def inner(self) -> CodeBlock:
        return self._inner

    def gen_code(self, intents: list[str], **options):
        raise NotImplementedError

    def prepare(self) -> PREPARE_RET:
        yield from self._inner.prepare()
