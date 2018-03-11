pyclimenu
=========

The easy way to create command line menus

Demo
----

.. code:: python

    >>> from pyclimenu.pyclimenu import Menu
    >>> def first_func():
    ...     return 'first item'
    ... 
    >>> def second_func():
    ...     return 'second item'
    ...
    >>> import pyclimenu
    >>> items = [
    ...     {'label': 'First item',
    ...      'callback': first_func
    ...     },
    ...     {'label': 'Second item',
    ...      'callback': second_func,
    ...     }
    ... ]
    >>> menu = pyclimenu.Menu(items=items)
    >>> menu.display()

Demo Output
-----------

.. code:: bash

     [0] First item
     [1] Second item
     [2] Exit
    Select option: > 
