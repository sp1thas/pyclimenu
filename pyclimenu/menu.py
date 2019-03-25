from __future__ import print_function
import sys
import os
from .colors import Colors


class Menu:
    def __init__(self, items=None, exit_msg=None):
        """
        Initialize menu

          Usage:
          ------
            >>> def some_function(param1=1, **kwargs):
            ...     pass
            >>> mn = Menu(items=[{'label': 'sample 1', 'callback': some_function, 'args': (), 'kwargs'={}}])

        :param items: menu items. list of dictionaries
        :type items: list
        :param exit_msg: exit message
        :type exit_msg: str
        :return: Nada
        :rtype: None
        """

        self.colors = Colors()
        self.num_bg = ''
        self.num_bld = ''
        self.num_fg = ''
        self.label_bg = ''
        self.label_bld = ''
        self.label_fg = ''
        self.items = []
        self.results = None
        self.set_exit_item()
        self.choose_msq = 'Select option: > '
        self.exit_item = {
            'label': 'Exit',
            'callback': sys.exit
        }
        if isinstance(items, list):
            for item in items:
                self.add_item(item)
        if isinstance(items, dict):
            self.add_item(items)
        else:
            self.items = []

    def run(self, header=None, choose_msg=None):
        """
        Display menu
        :param header: header message
        :type header: str
        :choose_msg: Prompt choose message
        :type choose_msg: str
        :return: Nada
        :rtype: None
        """
        self.clear()
        if choose_msg:
            self.choose_msq = choose_msg
        while True:
            if header:
                max_line_length = max(len(_) for _ in header.split('\n'))
                print(' %s' % header)
                print('', '-' * max_line_length)
            for idx, item in enumerate(self.items):
                self.print_row(idx, item.get('label', 'no label'))
            choice = self.get_choice()
            if choice is False:
                self.clear()
                continue
            else:
                break
        self.run_choice(choice)

    def run_choice(self, idx=None):
        """
        Run user's choice
        :param idx: item index
        :type idx: int
        :return: Nada
        :rtype: None
        """
        if idx == len(self.items):
            call_func = self.exit_item.get('callback')
            args = ()
            kwargs = {}
        else:
            call_func = self.items[idx].get('callback', sys.exit)
            args = self.items[idx].get('args', ())
            kwargs = self.items[idx].get('kwargs', ())
        self.results = call_func(*args, **kwargs)
        return self.results

    def set_exit_item(self, label=None, callable=None, args=None, kwargs=None):
        """
        Set exit item
        :param label: exit item label
        :type label: str
        :param callable: exit callable
        :type callable: callable
        :param args: exit arguments
        :type args: tuple
        :param kwargs; exit keyword argument
        :type kwargs: dictionary
        :return; Nada
        """
        self.add_item({
            'label': label if label else 'Exit',
            'callable': callable if callable else sys.exit,
            'args': args if args else (),
            'kwargs': kwargs if kwargs else {}
        })

    def get_choice(self):
        """
        Manipulate user's choice
        """
        try:
            choice = input(self.choose_msq)
            return int(choice)
        except KeyboardInterrupt:
            print('Exiting...')
            sys.exit()

    @staticmethod
    def clear():
        """
        Clear terminal
        """
        os.system('clear')

    def add_item(self, item=None, label=None, callback=None, args=None, kwargs=None):
        """
        Add menu item
        :param item: menu item
        :type item: dict
        :param label: item label
        :type label: str
        :param callback: item callback function
        :type callback: function
        :param args: function args
        :type args: tuple
        :param kwargs: function kwargs
        :type kwargs: dict
        :return: Nada
        :rtype: None
        """
        if item:
            self.items.append(item)
        else:
            self.items.append({
                'label': label if label else callback.__name__,
                'callback': callback,
                'args': args if args else (),
                'kwargs': kwargs if kwargs else {}
            })

    def print_row(self, idx, label):
        """
        Print Every row (numeric and label)
        :param idx: numeric
        :type idx: str or int
        :param label: Message
        :type label: str
        :return: Nada
        """
        num_st = self.num_bg+self.num_bld+self.num_fg
        labl_st = self.label_bg+self.label_bld+self.label_fg
        num_patt = '%' + str(len(str(len(self.items)))) + 'd'
        ln_patt = '%s [%s] %s %s %s %s' % (num_st, num_patt, self.colors.reset, labl_st, '%s', self.colors.reset)
        print(ln_patt % (idx, label))

    def set_colors(self, **kwargs):
        """
        Set colors for the output
        :param kwargs:
            :num_bold: numbering bold
            :num_fg: numbering foreground color
            :num_bg: numbering background color
            :label_bold: label bold
            :label_fg: label foregroud color
            :label_bg: label background color
        :return: Nada
        """
        num_bld = kwargs.get('num_bold')
        if num_bld:
            self.num_bld = self.colors.bold
        num_fg = kwargs.get('num_fg')
        if num_fg:
            self.num_fg = getattr(self.colors.fg, num_fg)
        num_bg = kwargs.get('num_bg')
        if num_bg:
            self.num_bg = getattr(self.colors.bg, num_bg)

        label_bld = kwargs.get('label_bold')
        if label_bld:
            self.label_bld = self.colors.bold
        label_fg = kwargs.get('label_fg')
        if label_fg:
            self.label_fg = getattr(self.colors.fg, label_fg)
        label_bg = kwargs.get('label_bg')
        if label_bg:
            self.label_bg = getattr(self.colors.bg, label_bg)


if __name__ == '__main__':
    def a():
        print('''
        Let's Rock!
        ''')
    mn = Menu()
    mn.add_item(label=None, callback=a, args=(), kwargs={})
    mn.add_item(label='to create', callback=a, args=(), kwargs={})
    mn.add_item(label='command line menus', callback=a, args=(), kwargs={})
    mn.set_exit_item(label='ooookso re')
    mn.set_colors(num_fg='cyan', num_bld=True, label_fg='blue', label_bld=True)
    mn.run(header='pyclimenu')
