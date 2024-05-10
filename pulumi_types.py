from typing import (
    Awaitable,
    Generic,
    TypeVar,
    Union,
)

T = TypeVar("T")

class Output(Generic[T]):
    pass

Input = Union[T, Awaitable[T], Output[T]]
