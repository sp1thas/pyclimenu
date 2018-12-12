pyclimenu
=========

This python module creates simple command line menus. Just define the callable and the label of each option and voila!
Foreground and background color of numbers and labels is adjustable.

Install
-------

.. code:: bash

    $ pip install git+https://github.com/sp1thas/pyclimenu.git

Demo
----

.. code:: python

    >>> from pyclimenu.menu import Menu
    >>> def a():
    ...     print('''
    ...     Let's Rock!
    ...     ''')
    ...     return 1
    >>> mn = Menu()
    >>> mn.add_item(label='The easy way', callback=a, args=())
    >>> mn.add_item(label='to create', callback=a, kwargs={})
    >>> mn.add_item(label='command line menus', callback=a)
    >>> mn.set_colors(num_fg='cyan', num_bld=True, label_fg='blue', label_bld=True)
    >>> results = mn.run(header='pyclimenu')
    >>> results
    1


.. image:: imgs/display.png
   :target: #

Todo
----
