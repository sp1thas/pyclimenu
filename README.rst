pyclimenu
=========

Install
-------

.. code:: bash

    $ pip install pyclimenu

Demo
----

.. code:: python

    >>> from pyclimenu import Menu
    >>> def first_function(a=0):
    ...     print(a*2)
    ...
    >>> def second_function(a=0):
    ...     print(a*4)
    ...
    >>> mn = Menu()
    >>> mn.add_item(label='first function', callback=first_function, params={'a': 2})
    >>> mn.add_item(label='second function', callback=second_function, params={'a': 1})
    >>> mn.display()

     [0] first function
     [1] second function
     [2] Exit
    Select option: > 1
    4
    >>>

