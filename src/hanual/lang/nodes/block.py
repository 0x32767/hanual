from __future__ import annotations

from typing import List, Union, TypeVar, Any, TYPE_CHECKING
from .base_node import BaseNode
from abc import ABC

if TYPE_CHECKING:
    from hanual.runtime import RuntimeEnvironment, ExecStatus
    from hanual.lang.errors import Error

T = TypeVar("T")


class CodeBlock(BaseNode, ABC):
    __slots__ = ("_children",)

    def __init__(self, children: Union[List[T], T]) -> None:
        self._children: List[BaseNode] = []
        self.add_child(children)

    def add_child(self, child: CodeBlock):
        if isinstance(child, (list, tuple)):
            for child_ in child:
                self.add_child(child_)

        elif isinstance(child, CodeBlock):
            self.children.extend(child.children)

        else:
            self._children.append(child)

        return self

    def execute(self, rte: RuntimeEnvironment) -> ExecStatus[Error, Any]:
        for child in self._children:
            # If we have an error then we raise it, otherwise I just discard the return value and keep going
            err, _ = sts = child.execute(rte)

            if err:
                return sts

    def compile(self, ir) -> Any:
        for child in self.children:
            child.compile(ir)

    @property
    def children(self):
        return self._children

    def as_dict(self) -> List[Any]:
        return [c.as_dict() if hasattr(c, "as_dict") else c for c in self.children]
