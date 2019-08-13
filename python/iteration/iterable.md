# Iterators

- In order to be *iter***able**, a class needs to implement `__iter__`
- `__iter__` must return an **iterator**
- an **iterator** must implement `__next__`, which must raise a **StopIteration**
- thats why the most common iterators return self in their `__iter__` method
- `__iter__` is only called **once**
- `__next__` is called in **every** iteration

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