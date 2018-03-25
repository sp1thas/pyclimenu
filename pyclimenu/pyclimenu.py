#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import sys, os
from colors import Colors

class Menu():
  def __init__(self, items=None, exit_msg=None):
    """
    Initialize menu
    
      Usage:
      ------
        >>> mn = Menu(items=[{'label': 'sample 1', 'callback': some_function, 'params': {'param1': 'value', ...}}]

    :param items: menu items. list of dictionaries
    :type items: list
    :param exit_msg: exit message
    :type exit_msg: str
    :return: Nada
    :rtype: None
    """
    self.colors = Colors()
    self.items = []
    self.set_exit_item(msg=exit_msg)
    if isinstance(items, list):
      for item in items:
        self.add_item(item)
    if isinstance(items, dict):
      self.add_item(items)
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
      print(ln_patt % (len(self.items), self.exit_item.get('label')))
      choice = self.getChoice()
      if choice is False:
        self.clear()
        continue
      else:
        break
    self.runChoice(choice)

  def runChoice(self, idx=None):
    """
    Run user's choice
    :param idx: item index
    :type idx: int
    :return: Nada
    :rtype: None
    """
    call_func = self.items[idx].get('callback', sys.exit)
    func_params = self.items[idx].get('params', {})
    call_func(**func_params)

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

  def add_item(self, item=None, label=None, callback=None, params=None):
    """
    Add menu item
    :param item: menu item
    :type item: dict
    :param label: item label
    :type label: str
    :param callback: item callback function
    :type callback: function
    :param params: function parameters
    :type params: dict
    :return: Nada
    :rtype: None
    """
    if item:
      self.items.append(item)
    else:
      self.items.append({
        'label': label,
        'callback': callback,
        'params': params,
      })

  def set_colors(self, **kwargs):
    """
    Set colors for the output
    
    :param num_bold: numbering bold
    :type num_bold: bool
    :param num_fg: numbering foreground color
    :type num_fg: str
    :param num_bg: numbering background color
    :type num_bg: str
    :param label_bold: label bold
    :type label_bold: bool
    :param label_fg: label foregroud color
    :type label_fg: str
    :param label_bg: label background color
    :type label_bg: str
    :return: Nada
    """
    num_bld = kwargs.get('num_bold')
    if num_bld: self.num_bld = self.colors.bold
    num_fg = kwargs.get('num_fg')
    if num_fg: self.num_fg = getattr(self.colors.fg, num_fg)
    num_bg = kwargs.get('num_bg')
    if num_bg: self.num_bg = getattr(self.colors.bg, num_bg)
    
    label_bld = kwargs.get('label_bold')
    if label_bld: self.label_bld = self.colors.bold
    label_fg = kwargs.get('label_fg')
    if label_fg: self.label_fg = getattr(self.colors.fg, label_fg)
    label_bg = kwargs.get('label_bg')
    if label_bg: self.label_bg = getattr(self.colors.bg, label_bg)
