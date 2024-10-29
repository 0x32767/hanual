from __future__ import annotations

from typing import TYPE_CHECKING, Generator

from bytecode import Instr, Label

if TYPE_CHECKING:
    from hanual.util.protocalls import Reply, Request, Response


type REQUEST_TYPE = int

type GENCODE_RET = Generator[
    Response[Instr] | Response[Label],  # yield
    Reply | None,  # send type
    None,  # return type
]
type PREPARE_RET = Generator[
    Request[object], Reply[object] | None, None  # yield  # send type  # return type
]
