# Metaclasses
- constructed using `__type__`

## Basics about Python and it's objects
- the **class** statement if **only** syntactic sugar and it **NOT** needed

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