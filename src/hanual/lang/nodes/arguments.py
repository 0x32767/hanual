from __future__ import annotations

from collections.abc import Iterable
from typing import Generator
from typing import Self

from bytecode import Instr
from hanual.lang.lexer import Token
from hanual.lang.nodes.base_node import BaseNode
from hanual.util import Reply
from hanual.util import Request
from hanual.util import Response


class Arguments[T: (BaseNode, Token)](BaseNode):
    __slots__ = (
        "_children",
        "_lines",
        "_line_range",
    )

    def __init__(
        self,
        children: T | Iterable[T],
    ) -> None:
        self._children: list[T] = []
        self.add_child(children)

    def add_child(self, child) -> Self:
        if isinstance(child, Arguments):
            self._children.extend(child.children)

        elif isinstance(child, Iterable):
            self._children.extend(child)

        else:
            self._children.append(child)

        return self

    @property
    def children(self) -> list[T]:
        return self._children

    def gen_code(self) -> Generator[Response | Request, Reply, None]:
        for arg in self._children:
            if isinstance(arg, Token) and arg.type == "STR":
                yield Response(Instr("LOAD_CONST", arg.value))

            else:
                raise NotImplementedError(f"{arg}")

    def prepare(self) -> Generator[Response | Request, Reply, None]:
        for arg in self._children:
            if isinstance(arg, Token) and arg.type == "STR":
                yield Request(Request.ADD_CONSTANT, arg.value).make_lazy()

            elif isinstance(arg, Token) and arg.type == "NUM":
                yield Request(Request.ADD_CONSTANT, arg.value).make_lazy()

            else:
                raise NotImplementedError
