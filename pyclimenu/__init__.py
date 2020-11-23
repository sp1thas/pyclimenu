import typing

from .menu import Menu

__version__ = "0.1.15"


class ExitItemDict(typing.TypedDict):
    label: str
    callback: typing.Callable
