# pyclimenu
![build](https://travis-ci.org/sp1thas/pyclimenu.svg?branch=master) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/ecdea75af44541ef91e3ec465592cc32)](https://www.codacy.com/app/sp1thas/pyclimenu?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=sp1thas/pyclimenu&amp;utm_campaign=Badge_Grade)

This python module creates simple command line menus. Just define the callable and the label of each option and voila!
Foreground, background color numbering and labels are adjustable.

## Install
```bash
pip install git+https://github.com/sp1thas/pyclimenu.git
```

## Demo
```python
from pyclimenu.menu import Menu
def a():
    print('''
    Let's Rock!
    ''')
    return 1
mn = Menu()
mn.add_item(label='The easy way', callback=a, args=())
mn.add_item(label='to create', callback=a, kwargs={})
mn.add_item(label='command line menus', callback=a)
mn.set_colors(num_fg='cyan', num_bld=True, label_fg='blue', label_bld=True)
results = mn.run(header='pyclimenu')
results
1
```
![menu](imgs/display.png)

## Todo
