pyclimenu
=========

This python module creates simple command line menus. Just define the callable and the label of each option and voila!
Foreground, background color numbering and labels are adjustable.

Install
-------

.. code:: bash

    $ pip install git+https://github.com/sp1thas/pyclimenu.git

Demo
----

.. code:: python

    >>> from pyclimenu import Menu
    >>> def a():                                                                                                     
    ...     print('''
    ...     Let's Rock!
    ...     ''')
    >>> mn = Menu()
    >>> mn.add_item(label='The easy way', callback=a, params={})
    >>> mn.add_item(label='to create', callback=a, params={})
    >>> mn.add_item(label='command line menus', callback=a, params{})
    >>> mn.set_colors(num_fg='cyan', num_bld=True, label_fg='blue', label_bld=True)
    >>> mn.display(header='pyclimenu')


.. image:: imgs/display.png
   :target: #

Todo
----
