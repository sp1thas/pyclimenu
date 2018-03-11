# pyclimenu
The easy way to create command line menus


## Usage
```python
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
```
