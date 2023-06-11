from __future__ import annotations


from typing import Any, Dict, Optional, TYPE_CHECKING
from .base_node import BaseNode


if TYPE_CHECKING:
    from hanual.lang.lexer import Token


class RangeNode(BaseNode):
    def __init__(
        self: Self,
        from_: Optional[Token] = None,
        to_: Optional[Token] = None,
    ) -> None:
        self._from = from_
        self._to = to_

    def compile(self) -> None:
        raise NotImplementedError

    def as_dict(self) -> Dict[str, Any]:
        return {
            "from": self._from,
            "to": self._to,
        }
