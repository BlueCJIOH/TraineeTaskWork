from enum import Enum, unique
from functools import lru_cache
from operator import attrgetter


@unique
class BaseEnum(Enum):
    @classmethod
    @lru_cache(None)
    def values(cls):
        return tuple(map(attrgetter("value"), cls))

    @classmethod
    @lru_cache(None)
    def names(cls):
        return tuple(map(attrgetter("name"), cls))

    @classmethod
    @lru_cache(None)
    def items(cls):
        return tuple(zip(cls.values(), cls.names()))


class CreatorType(BaseEnum):
    AUTHOR = "Author"
    TEACHER = "Teacher"
