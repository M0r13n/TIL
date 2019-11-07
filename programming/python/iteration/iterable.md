# Iterators

- In order to be *iter***able**, a class needs to implement `__iter__`
- `__iter__` must return an **iterator**
- an **iterator** must implement `__next__`, which must raise a **StopIteration**
- thats why the most common iterators return self in their `__iter__` method
- `__iter__` is only called **once**
- `__next__` is called in **every** iteration
- The big difference between yield and a return statement is that on reaching a yield the generator’s state of execution is suspended and local variables are preserved.

## Code

```python
class IterableThing:
    def __init__(self):
        self.current = 0
        self.values = range(1, 6)

    def __getitem__(self, index):
        return self.values[index]

    def __len__(self):
        return len(self.values)

    def __iter__(self):
        return self # possible because __next__ is implemented

    def __next__(self):
        while self.current < len(self):
            v = self[self.current]
            self.current += 1
            return v # may also check for conditions
        # required!
        raise StopIteration
```

# Generators
- is also an iterator
- does not know about the past and only knows what happens next
- use this if it's unimportant what state we are in

```python
class GeneratorThing:
    def __init__(self):
        self.values = range(1, 6)

    def __getitem__(self, index):
        return self.values[index]

    def __iter__(self):
        for i in self.values:
            if not i % 2: # yield only even values
                yield i

``
