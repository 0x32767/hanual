from __future__ import annotations

from typing import TYPE_CHECKING

from bytecode import BinaryOp, Instr

from hanual.lang.lexer import Token
from hanual.lang.nodes.base_node import BaseNode
from hanual.lang.util.type_objects import GENCODE_RET, PREPARE_RET
from hanual.util import Response

if TYPE_CHECKING:
    from hanual.lang.nodes.f_call import FunctionCall


class ImplicitBinOp[OP: Token, R: (Token, FunctionCall)](BaseNode):
    __slots__ = ("_right", "_op", "_lines", "_line_range")

    def __init__(self, op: OP, right: R) -> None:
        # The left side is implied
        self._right: R = right
        self._op: OP = op

    @property
    def op(self) -> OP:
        return self._op

    @property
    def right(self) -> R:
        return self._right

    def gen_code(self, intents: list[str], **options) -> GENCODE_RET:
        inferred: Token | None = options.get("imply_var")

        if inferred is None:
            raise KeyError("The implied variable for the binary operation needs to be passed")

        yield from inferred.gen_code([self.CAPTURE_RESULT, Token.GET_VARIABLE])
        yield from self._right.gen_code([self.CAPTURE_RESULT, Token.GET_VARIABLE])

        if self._op.value == "+":
            yield Response(Instr("BINARY_OP", BinaryOp.ADD))

        else:
            raise NotImplementedError(f"Have not implemented operator {self._op.value}")

        if self.INPLACE in intents:
            yield from inferred.gen_code([Token.SET_VARIABLE])

        elif self.IGNORE_RESULT in intents:
            yield Response(Instr("POP_TOP"))

        elif self.CAPTURE_RESULT in intents:
            pass

        else:
            raise Exception(
                f"No relevant intents: Inplace, IGNORE_RESULT, CAPTURE_RESULT passed, ( {intents} )"
            )

    def prepare(self) -> PREPARE_RET:
        yield from self._right.prepare()
