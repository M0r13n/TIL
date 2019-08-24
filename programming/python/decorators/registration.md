# Registration of functions or classes
One of the most convenient features of Flask is definitely their mechanism to register view functions. One can decorate a function with '@app.route('/url', ...)'
and the Flask app knows about that new endpoint. It always felt a bit like magic and so I played around with it and finally understood the mechanism and how it works. 

## Problem
Let's say I want to register a function that is called, when a special keyword is entered. Basically all I need to do is something like this:
```python

commands = {}

def respond_to(match):
    def wrapper(func):
        commands[re.compile(match)] = func
        return func

    return wrapper
```

and then I can decorate that function with that decorator.


```python
@respond_to(r'some regex')
def do_something(*args, **kwargs):
	pass
```

The only problem that is left, is the fact that the decorator is only executed once that function gets called. In fact it is enough to import the function to trigger that decorator. A simple way to import all functions from all Python files could be something like this:

```python
import os
from importlib import import_module
from glob import glob

path_name = os.path.dirname(os.path.abspath(__file__))
module_list = glob('{}/[!_]*.py'.format(path_name))
module_list = ['.'.join(('<<SOME_MODULE>>', os.path.split(f)[-1][:-3])) for f in module_list]
[import_module(module) for module in module_list]
```

That's it. The functions are registered now. :-)
