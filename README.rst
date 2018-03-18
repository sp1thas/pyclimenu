pyclimenu
=========

The easy way to create command line menus

Demo
----

.. code:: python

    >>> from pyclimenu.pyclimenu import Menu
    >>> def first_function(a=0):
    ...     print(a*2)
    ...
    >>> def second_function(a=0):
    ...     print(a*4)
    ...
    >>> mn = pyclimenu.Menu()
    >>> mn.add_item(label='first function', callback=first_function, params={'a': 2})
    >>> mn.add_item(label='second function', callback=second_function, params={'a': 1})
    >>> menu.display()

     [0] first function
     [1] second function
     [2] Exit
    Select option: > 1
    4
    >>>

