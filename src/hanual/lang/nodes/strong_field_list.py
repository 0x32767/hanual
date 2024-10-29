from __future__ import annotations

from typing import TYPE_CHECKING, Self

from hanual.lang.nodes.base_node import BaseNode
from hanual.lang.util.type_objects import GENCODE_RET, PREPARE_RET

if TYPE_CHECKING:
    from .strong_field import StrongField


class StrongFieldList[F: StrongField](BaseNode):
    __slots__ = ("_fields", "_lines", "_line_range")

    def __init__(self) -> None:
        self._fields: list[F] = []

    def add_field(self, field: F) -> Self:
        self._fields.append(field)
        return self

    @property
    def fields(self) -> list[F]:
        return self._fields

    def gen_code(self, intents: list[str], **options) -> GENCODE_RET:
        raise NotImplementedError

    def prepare(self) -> PREPARE_RET:
        raise NotImplementedError
