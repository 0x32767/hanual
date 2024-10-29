from __future__ import annotations

from bytecode.instr import InstrLocation

from hanual.lang.util.line_range import LineRange
from hanual.lang.util.type_objects import PREPARE_RET


class CompilableObject:
    CAPTURE_RESULT = "CAPTURE_RESULT"  # If the node evaluates to something, keep it on the stack
    IGNORE_RESULT = "IGNORE_RESULT"  # Ignore the result of the operation, pop it off the stack
    INPLACE = "INPLACE"

    def prepare(self) -> PREPARE_RET:
        raise NotImplementedError

    def gen_code(self, intents: list[str], **options):
        raise NotImplementedError

    def get_location(self) -> InstrLocation:
        raise NotImplementedError

    @property
    def lines(self) -> str:
        raise NotImplementedError

    @lines.setter
    def lines(self, new: str) -> None:
        raise NotImplementedError

    @property
    def line_range(self) -> LineRange:
        raise NotImplementedError

    @line_range.setter
    def line_range(self, new: LineRange) -> None:
        raise NotImplementedError

    @property
    def is_token(self):
        raise NotImplementedError

    # This property has been implemented because tokens are also compilable objects
    @property
    def token_type(self):
        raise NotImplementedError

    @property
    def children(self):
        raise NotImplementedError
