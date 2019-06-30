import unittest
from pyclimenu import Menu


def a():
    print('''
    Let's Rock!
    ''')


class TestPyCLIMenu(unittest.TestCase):

    def setUp(self) -> None:
        self.menu = Menu()

    def test_menu_init(self) -> None:
        self.assertTrue(bool(self.menu))

    def test_add_item(self) -> None:
        self.menu.add_item(clb=a, args=(), kwargs={})
        self.assertEqual(len(self.menu.items), 1)


if __name__ == '__main__':
    unittest.main()
