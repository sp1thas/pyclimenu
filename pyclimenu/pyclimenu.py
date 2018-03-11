#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import sys, os

class Menu():
  def __init__(self, items=None, exit_msg=None):
    """
    Initialize menu
    
      Usage:
      ------
        >>> mn = Menu(items=[{'label': 'sample 1', 'callback': some_function}]

    :param items: menu items. list of dictionaries
    :type items: list
    :param exit_msg: exit message
    :type exit_msg: str
    :return: Nada
    :rtype: None
    """
    self.items = []
    self.set_exit_item(msg=exit_msg)
    if isinstance(items, list):
      self.items = items
    else: self.items = []

  def display(self, header=None, choose_msg=None):
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
    if choose_msg: self.choose_msq = choose_msg
    else: self.choose_msq = 'Select option: > '
    num_patt = '%' + str(len(str(len(self.items)))) + 'd'
    ln_patt = ' [%s] %s' % (num_patt, '%s')
    while True:
      if header:
        print(' %s' % header)
        print('', '-'*len(header))
      for idx, item in enumerate(self.items):
        print(ln_patt % (idx, item.get('label', 'no label')))
      print(ln_patt % (idx+1, self.exit_item.get('label')))
      choice = self.getChoice()
      if choice is False:
        self.clear()
        continue
      else:
        break

  def runChoice(idx=None):
    """
    Run user's choice
    :param idx: item index
    :type idx: int
    :return: Nada
    :rtype: None
    """
    call_func = self.items[idx].get('callback', sys.exit)
    call_func()

  def set_exit_item(self, msg=None):
    """
    Set exit item
    :param msg: exit message. default: Exit
    :type msg: str
    :return: Nada
    :rtype: None
    """
    self.exit_item = {
      'label': 'Exit',
      'function': sys.exit
    }
    if msg: self.exit_item['label'] = msg

  def getChoice(self):
    """
    Manipulate user's choice
    """
    try:
        choice = input(self.choose_msq)
        return int(choice)
    except KeyboardInterrupt:
      print('Exiting...')
      sys.exit()
    except Exception as e:
      return False

  def clear(self):
    """
    Clear terminal
    """
    os.system('clear')

  def add_item(item=None):
    """
    Add menu item
    :param item: menu item
    :type item: dict
    :return: Nada
    :rtype: None
    """
    self.append(item)