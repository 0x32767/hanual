from .handeler.reference_handeler import ReferenceHandeler
from .handeler.const_handeler import ConstantHandeler
from .handeler.file_deps import ExternDepsHandeler
from .handeler.labels import LabelHandeler


class GlobalState:
    __instance = None

    def __init__(self) -> None:
        self.__instance = self

        self._const_pool = []
        self._label_pool = []
        self._functions = {}
        self._file_deps = []
        self._refs = []

    @property
    def refs(self):
        return self._refs

    @property
    def const_pool(self):
        return self._const_pool

    @property
    def get_instacne(self):
        return self.__instance

    @property
    def labels(self):
        return LabelHandeler(self)

    @property
    def constants(self):
        return ConstantHandeler(self)

    @property
    def references(self):
        return ReferenceHandeler(self)

    @property
    def external_deps(self):
        return ExternDepsHandeler(self)

    def add_function(self, name: str, entery):
        self._functions[name] = entery
