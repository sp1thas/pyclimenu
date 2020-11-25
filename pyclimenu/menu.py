from __future__ import print_function

import subprocess
import sys
import typing
import types

from pyclimenu.colors import Colors

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


class ExitItemDict(TypedDict):
    label: str
    callback: typing.Callable


class Menu:
    """Menu class

    Usage:
    ------
        >>> from pyclimenu import Menu
        >>> def some_function(param1=1, **kwargs):
        ...     pass
        >>>
        >>> mn = Menu()
        >>> mn.add_item(label='callable label', callback=some_function)
        >>> mn.add_value_item(3, 'value label')
        >>> result = mn.run()
    """

    def __init__(
        self,
        items: typing.List[typing.Dict] = None,
        exit_msg: typing.Optional[str] = None,
        exit_callback: typing.Optional[typing.Callable] = None,
    ) -> None:
        """Initialize menu

        :param items: menu items. list of dictionaries
        :param exit_msg: exit message
        """

        self.colors = Colors()
        self.num_bg = ""
        self.num_bld = ""
        self.num_fg = ""
        self.label_bg = ""
        self.label_bld = ""
        self.label_fg = ""
        self.items: list = []
        self.results = None
        self.choose_msq = "Select option: > "
        self.exit_item: ExitItemDict = {
            "label": exit_msg if exit_msg is not None else "Exit",
            "callback": exit_callback if exit_callback is not None else sys.exit,  # type: ignore
        }
        if isinstance(items, list):
            for item in items:
                self.add_item(item)
        else:
            self.items = []
        self.set_exit_item()

    @staticmethod
    def _print_header(header) -> None:
        if header:
            max_line_length = max(len(_) for _ in header.split("\n"))
            print(" %s" % header)
            print("", "-" * max_line_length)

    def _print_rows(self) -> None:
        for idx, item in enumerate(self.items):
            self.print_row(idx, item.get("label", "no label"))

    def run(self, header: str = None, choose_msg: str = None) -> typing.Any:
        """Display menu

        :param header: header message
        :param choose_msg: Prompt choose message
        """
        self.clear()
        if choose_msg:
            self.choose_msq = choose_msg
        while True:
            self._print_header(header)
            self._print_rows()
            choice = self.get_choice()
            if choice is False:
                self.clear()
                continue
            else:
                break
        return self.run_choice(choice)

    def run_choice(self, idx) -> typing.Any:
        """Run user's choice

        :param idx: item index
        """
        if idx == len(self.items) - 1:
            call_func = self.exit_item["callback"]
            args = ()
            kwargs = {}
        else:
            call_func = self.items[idx].get("callback", sys.exit)
            args = self.items[idx].get("args", ())
            kwargs = self.items[idx].get("kwargs", ())
        self.results = call_func(*args, **kwargs)
        return self.results

    def set_exit_item(self) -> None:
        """Set exit item"""
        self.add_item(self.exit_item)  # type: ignore

    def _get_input(self) -> str:
        """Get input choice"""
        return input(self.choose_msq)

    def _check_input(self, choice: typing.Any) -> typing.Optional[int]:
        """Check input"""
        i = None
        if not choice.isdigit():
            print(
                "{}Please provide an integer as input{}".format(
                    self.colors.Fg.lightred, self.colors.reset
                )
            )
        elif int(choice) > len(self.items) or int(choice) < 0:
            print(
                "{}Provide an integer between 0 and {} {}".format(
                    self.colors.Fg.lightred, len(self.items) - 1, self.colors.reset
                )
            )
        else:
            i = int(choice)
        return i

    def get_choice(self) -> typing.Optional[int]:
        """Manipulate user's choice"""
        while True:
            try:
                choice = self._get_input()
            except KeyboardInterrupt:
                print("Exiting...")
                sys.exit()
            return self._check_input(choice)

    @staticmethod
    def clear() -> bool:
        """Clear terminal"""
        subprocess.call(["clear"])
        return True

    def add_item(
        self,
        item: typing.Dict = None,
        label: typing.AnyStr = None,
        callback: typing.Callable = None,
        args: typing.Tuple = None,
        kwargs: typing.Dict = None,
    ) -> None:
        """Add menu item

        :param item: menu item
        :param label: item label
        :param callback: item callback function
        :param args: function args
        :param kwargs: function kwargs
        :return: Nada
        """

        params = {
            "label": label,
            "callback": callback,
            "args": args if args else (),
            "kwargs": kwargs if kwargs else {},
        }

        if item is None:
            item = {}

        for k, v in params.items():
            if v is not None and k not in item:
                item[k] = v

        if item.get("label") is None:
            item["label"] = item["callback"].__name__
        self.items.append(item)

    @staticmethod
    def _value_callback(value):
        return value

    def add_value_item(self, value: typing.Any, label: str = None) -> None:
        """Add item with specific value

        :param value: item's value
        :param label: item's label
        """
        self.add_item(
            {
                "label": label if label is not None else str(value),
                "callback": self._value_callback,
                "args": (value,),
            }
        )

    def print_row(self, idx: int, label: typing.AnyStr) -> None:
        """Print Every row (numeric and label)

        :param idx: numeric
        :param label: Message
        :return: Nada
        """
        num_st = self.num_bg + self.num_bld + self.num_fg
        label_st = self.label_bg + self.label_bld + self.label_fg
        num_patt = "%" + str(len(str(len(self.items)))) + "d"
        ln_patt = "%s [%s] %s %s %s %s" % (
            num_st,
            num_patt,
            self.colors.reset,
            label_st,
            "%s",
            self.colors.reset,
        )
        print(ln_patt % (idx, label))

    def set_colors(self, **kwargs) -> None:
        """
        Set colors for the output
        :param kwargs:
            :num_bold: numbering bold
            :num_fg: numbering foreground color
            :num_bg: numbering background color
            :label_bold: label bold
            :label_fg: label foreground color
            :label_bg: label background color
        :return: Nada
        """
        num_bld = kwargs.get("num_bold")
        if num_bld:
            self.num_bld = self.colors.bold
        num_fg = kwargs.get("num_fg")
        if num_fg:
            self.num_fg = getattr(self.colors.Fg, num_fg)
        num_bg = kwargs.get("num_bg")
        if num_bg:
            self.num_bg = getattr(self.colors.Bg, num_bg)

        label_bld = kwargs.get("label_bold")
        if label_bld:
            self.label_bld = self.colors.bold
        label_fg = kwargs.get("label_fg")
        if label_fg:
            self.label_fg = getattr(self.colors.Fg, label_fg)
        label_bg = kwargs.get("label_bg")
        if label_bg:
            self.label_bg = getattr(self.colors.Bg, label_bg)
