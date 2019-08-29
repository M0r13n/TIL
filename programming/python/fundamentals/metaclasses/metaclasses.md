# Metaclasses
- constructed using `__type__`

## Basics about Python and it's objects
- the **class** statement if **only** syntactic sugar and it **NOT** needed 
- that means that classes can be created via **function calls**!!
- classes that create classes are called **metaclasses**

```python
def foo_new(cls):
    print("i will build a instance of ", cls)
    obj = object.__new__(cls)
    print("created a new instance: ", obj)
    return obj


def foo_init(self):
    print("init", self)
    self.value = "some value"


def some_method(self):
    print("I can do stuff!")


Foo = type('Foo',
           (object,),
           {
               '__new__': foo_new,
               '__init__': foo_init,
               'some_method': some_method
           })

foo = Foo()
print(foo.value)
foo.some_method()

```

So one can do things like

```python
class FooMeta(type):

    def __new__(mclass, name, base, ns):
        print("i build a class of", mclass)
        print("with name=", name)
        print("with bases=", base)
        print("with namespace=", ns)

        cls = super().__new__(mclass, name, base, ns)
        print("constructed class ", cls)
        return cls

    def __init__(mclass, name, base, ns):
        super().__init__(mclass)
        print("init")


class Foo(metaclass=FooMeta):
    pass


class Bar(Foo):
    pass

```
