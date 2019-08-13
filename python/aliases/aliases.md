# Aliases
- Every method is an object
- objects can be assigned to variables
- so methods can be aliased

```python
class Foo:
    def __str__(self):
        return self.__class__.__name__


x = Foo()
string = str
print(str(x))
print(string(x))
``