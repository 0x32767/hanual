from __future__ import annotations

from abc import ABC
from typing import TYPE_CHECKING

from hanual.lang.util.type_objects import GENCODE_RET, PREPARE_RET

from .base_node import BaseNode

if TYPE_CHECKING:
    from .namespace_acessor import NamespaceAccessor


class UsingStatement(BaseNode, ABC):
    __slots__ = ("_nsa", "_lines", "_line_no")

    def __init__(self, nsa: NamespaceAccessor) -> None:
        self._nsa = nsa

    @property
    def path(self) -> NamespaceAccessor:
        return self._nsa

    def gen_code(self) -> GENCODE_RET:
        raise NotImplementedError

    def prepare(self) -> PREPARE_RET:
        raise NotImplementedError
