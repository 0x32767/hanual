from __future__ import annotations


class ItemEqualList[T](list[T]):
    def __contains__(self, item):
        for element in self:
            if element == item:
                return True

        return False
