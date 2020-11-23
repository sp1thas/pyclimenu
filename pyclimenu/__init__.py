import sys
from .menu import Menu
import typing

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__version__ = "0.1.15"


class ExitItemDict(TypedDict):
    label: str
    callback: typing.Callable
