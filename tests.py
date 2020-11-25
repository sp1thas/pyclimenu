import sys
import unittest
from mock import patch

from pyclimenu import Menu


def a():
    print(
        """
    Let's Rock!
    """
    )


class TestPyCLIMenu(unittest.TestCase):
    def test_menu_with_exit_message(self) -> None:
        menu = Menu(exit_msg="test")
        self.assertEqual(
            menu.exit_item,
            {"args": (), "callback": sys.exit, "kwargs": {}, "label": "test"},
        )

    def test_menu_with_items_list(self) -> None:
        menu = Menu(items=[{"label": "a", "callback": a}])
        self.assertEqual(
            menu.items,
            [
                {"args": (), "callback": a, "kwargs": {}, "label": "a"},
                {"args": (), "callback": sys.exit, "kwargs": {}, "label": "Exit"},
            ],
        )

    def test_menu_run_choice(self) -> None:
        menu = Menu(items=[{"label": "a", "callback": a}])
        self.assertEqual(None, menu.run_choice(0))

    def test_menu_run_exit(self) -> None:
        menu = Menu(items=[{"label": "a", "callback": a}], exit_callback=lambda: None)
        self.assertEqual(None, menu.run_choice(1))

    def test_menu_add_item_kwargs(self) -> None:
        menu = Menu()
        menu.add_item(label="a", callback=a)
        self.assertEqual(
            menu.items,
            [
                {"args": (), "callback": sys.exit, "kwargs": {}, "label": "Exit"},
                {"args": (), "callback": a, "kwargs": {}, "label": "a"},
            ],
        )

    def test_value_callback(self) -> None:
        menu = Menu()
        self.assertEqual(menu._value_callback(1), 1)

    def test_print_row(self) -> None:
        menu = Menu(items=[{"label": "a", "callback": a}])
        menu.print_row(0, "test")

    def test_set_colors(self) -> None:
        menu = Menu(items=[{"label": "a", "callback": a}])
        menu.set_colors(
            num_bold=True,
            num_bg="black",
            num_fg="red",
            label_bold=True,
            label_bg="black",
            label_fg="red",
        )

    def test_menu_add_item_kwargs_no_label(self) -> None:
        menu = Menu()
        menu.add_item(callback=a)
        self.assertEqual(
            menu.items,
            [
                {"args": (), "callback": sys.exit, "kwargs": {}, "label": "Exit"},
                {"args": (), "callback": a, "kwargs": {}, "label": "a"},
            ],
        )

    def test_menu_add_value_item(self) -> None:
        menu = Menu()
        menu.add_value_item(1)
        self.assertEqual(
            menu.items,
            [
                {"args": (), "callback": sys.exit, "kwargs": {}, "label": "Exit"},
                {
                    "args": (1,),
                    "callback": menu._value_callback,
                    "kwargs": {},
                    "label": "1",
                },
            ],
        )

    def test_menu_clear(self) -> None:
        menu = Menu()
        self.assertTrue(menu.clear())

    def test_menu_input_check(self) -> None:
        menu = Menu()
        self.assertEqual(menu._check_input("1"), 1)
        self.assertEqual(menu._check_input("a"), None)
        self.assertEqual(menu._check_input("4"), None)

    def test_menu_print_header(self) -> None:
        menu = Menu()
        self.assertIsNone(menu._print_header("header"))

    def test_menu_print_rows(self) -> None:
        menu = Menu()
        menu._print_rows()

    @patch("builtins.input", lambda *args: "13")
    def test_menu_get_input(self) -> None:
        menu = Menu()
        self.assertEqual(menu._get_input(), "13")

    @patch("builtins.input", lambda *args: "0")
    def test_menu_run(self) -> None:
        menu = Menu(items=[{"label": "a", "callback": a}])
        self.assertEqual(menu.run(choose_msg="test"), None)

    @patch("builtins.input", lambda *args: "15")
    def test_menu_run_out_of_range(self) -> None:
        menu = Menu(items=[{"label": "a", "callback": a}])
        with self.assertRaises(TypeError):
            self.assertEqual(menu.run(choose_msg="test"), None)


if __name__ == "__main__":
    unittest.main()
