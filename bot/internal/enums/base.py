from enum import Enum
from typing import Self


class ExtendedEnum(Enum):

    @classmethod
    def list(cls) -> list[Self]:
        return list(map(lambda c: c.value, cls))
