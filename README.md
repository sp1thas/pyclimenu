# pyclimenu
![Code Analysis](https://github.com/sp1thas/pyclimenu/workflows/Code%20Analysis/badge.svg) ![Testing](https://github.com/sp1thas/pyclimenu/workflows/Testing/badge.svg) [![codecov](https://codecov.io/gh/sp1thas/pyclimenu/branch/master/graph/badge.svg?token=TGMQOYWT7F)](https://codecov.io/gh/sp1thas/pyclimenu)

This python module creates simple command line menus. Just define the callable and the label of each option and voila!
Foreground, background color numbering and labels are adjustable.

## Install
```bash
pip install pyclimenu
```

## Demo
```python
from pyclimenu.menu import Menu

def a():
    print('''
    Let's Rock!
    ''')
    return 1

mn = Menu(items=[
    {"label": "The easy way", "callback": a},
    {"label": "to create", "callback": a},
    {"label": "command line menus", "callback": a}
])
mn.set_colors(num_fg="cyan", num_bld=True, label_fg="blue", label_bl=True)

results = mn.run(header="pyclimenu")
print(results)
```
![menu](imgs/display.png)
