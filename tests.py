import unittest
from pyclimenu import Menu
import typing


def a():
    print('''
    Let's Rock!
    ''')


class TestPyCLIMenu(unittest.TestCase):

    def setUp(self) -> typing.NoReturn:
        self.menu = Menu()

    def test_menu_init(self) -> typing.NoReturn:
        self.assertTrue(bool(self.menu))

    def test_add_item(self) -> typing.NoReturn:
        self.menu.add_item(clb=a, args=(), kwargs={})
        self.menu.add_value_item(3, 'value label')
        self.assertEqual(len(self.menu.items), 2)


if __name__ == '__main__':
    unittest.main()
