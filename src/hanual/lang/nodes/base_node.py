from __future__ import annotations

from abc import abstractmethod
from bytecode.instr import InstrLocation
from hanual.lang.nodes.base_node_meta import _BaseNodeMeta
from hanual.lang.util.compileable_object import CompilableObject
from hanual.lang.util.line_range import LineRange
from hanual.lang.util.type_objects import GENCODE_RET, PREPARE_RET


class BaseNode(CompilableObject, metaclass=_BaseNodeMeta):
    """A node that all language nodes inherit from.

    Typical usage example:
        class MyNode(BaseNode):
            # logic for the node.

    """
    __slots__ = (
        "_lines",
        "_line_range",
    )

    @abstractmethod
    def __init__(self, *args, **kwargs) -> None:
        """The initializer for a node should be overriden.

        Raises:
            NotImplementedError: This method should be overriden with no super call.
        """
        self._line_range: LineRange | None = None
        self._lines: str | None = None

        raise NotImplementedError

    @abstractmethod
    def prepare(self) -> PREPARE_RET:
        """Called before any code is or should be generated.

        Raises:
            NotImplementedError: This method should be overriden with no super call.

        Returns:
            PREPARE_RET: The function should be lazy and yield information to the compiler.
        """
        raise NotImplementedError

    @abstractmethod
    def gen_code(self, *intents, **options):
        """Yields the byte code instructions to the compiler.

        The function takes options and a list of intents. The intents represent what the parent
        node intends to do. This is for information that should be propogated up the AST during
        compilation. The options should be information more specific towards the child node.

        Raises:
            NotImplementedError: This method should be overriden with no super call.

        Returns:
            GENCODE_RET: This method is a generator that should yield the instructions to the compiler.
        """
        raise NotImplementedError

    def get_location(self) -> InstrLocation:
        """Generates the location of the instructions as an InstrLocation for the bytecode module.

        Raises:
            Exception: When the `_line_range` attr is None.
            Exception: This occurs if the line range has never been set.

        Returns:
            InstrLocation: The location of the instruction.
        """
        if self._line_range is None:

            raise ValueError("self._line_range is None (was never set)")

        if self._line_range.start < 1 or self._line_range.end < 1:
            raise ValueError(f"LineRange has a range of -1 {self._line_range}")

        # TODO add column offsets and change second `self._line_range.start` to the `self._line_range.end`
        return InstrLocation(
            lineno=int(self._line_range.start),
            end_lineno=int(self._line_range.start),
            col_offset=None,
            end_col_offset=None,
        )

    @property
    def lines(self) -> str:
        """The lines that the node is in as a str.

        Raises:
            Exception: The line attr was None, was never set.

        Returns:
            str: The lines that contain the node.
        """
        if self._lines is None:
            # TODO make the exception a value error
            raise Exception("self._lines is None (was never set)")

        return self._lines

    @lines.setter
    def lines(self, new: str) -> None:
        """Sets the lines for the attr.

        This method should not be used in the code base.
        """
        # TODO make the exception a value error
        assert isinstance(new, str), "new value for lines must be a str"
        self._lines = new

    @property
    def line_range(self) -> LineRange:
        """Gets the location of the code as a line range.

        Raises:
            Exception: When the attribute has not yet been set.

        Returns:
            LineRange: The location of the code as a line range.
        """
        if self._line_range is None:
            # TODO make the exception a value error
            raise Exception("self._line_range is none (was never set)")

        return self._line_range

    @line_range.setter
    def line_range(self, new: LineRange) -> None:
        """Sets the line range for the attr.

        This method should not be used in the code base.
        """
        assert isinstance(new, LineRange), "new value must be a line_range"
        self._line_range = new

    @property
    def is_token(self):
        """Returns if the node is a token or not.

        Tokens also implements this logic and always return True. This reduces the requirement to
        run isinstance checks.

        Returns:
            bool: False
        """
        return False
