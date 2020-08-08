# Classes are objects

In Python classes do not only define how an instance of a class **looks like**. Classes are also itself **objects**.
Proof?

```py
>>> class SomeUselessCrapClass:
...     def do(self):
...             print("I am useless")
...
>>> SomeUselessCrapClass
<class '__main__.SomeUselessCrapClass'>
>>> useless = SomeUselessCrapClass()
>>> useless.do() # pretty useless
I am useless
>>>
>>> SomeUselessCrapClass.do = lambda self: print("I am soooooo useful") # make it useful
>>> instance = SomeUselessCrapClass()
>>> instance.do() # not so useless anymore
I am soooooo useful
>>>
```

Under the hood all classes inherit from `type`. And all classes can be created `dynamically` using type. Which in turn does nothing other than we did it the above example. Actually I can create the same class using `type`:

```py
>>> def do(self):
...     print("I am sooo usefull")
...
>>> SomeUselessCrapClass = type("SomeUselessCrapClass", (), dict(do=do))
>>> instance = SomeUselessCrapClass()
>>> instance.do()
I am sooo usefull
```

What does that mean?

- I can define a class in order to create instances (objects)
- But classes are objects, too
- This means that I can create a class that creates a class

And these classes actually have a name: **Metaclasses**. Classes that creates classes. 

Metaclasses need to be able to create classes. This is why most metaclasses out there subclass `type`.
Metaclasses are useful if you want to create a class that matches the current context. **WTF-Forms** for example uses it so that all Form classes create the `_unbound_fields` list.

```py
class SomeWeirdMetaClass(type):
  # append _foo to every object
  def __new__(cls, clsname, bases, attrs):
    print("New called")
    attrs = {
      attr if attr.startswith("__") else f"{attr}_foo":v
            for attr, v in attrs.items()
    } 
    return super(SomeWeirdMetaClass, cls).__new__(cls, clsname, bases, attrs)


class FooClass(object, metaclass=SomeWeirdMetaClass):
  def __init__(self):
    print("Init called")

  def do(self):
      print("Do something..")

instance = FooClass()
print(hasattr(instance, 'do'))
print(hasattr(instance, 'do_foo'))
print(instance.do_foo())
```

produces

```
New called
Init called
False
True
Do something..
None
Traceback (most recent call last):
  File "main.py", line 23, in <module>
    print(instance.do())
AttributeError: 'FooClass' object has no attribute 'do'
```