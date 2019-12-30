# How to write (mostly) functional programs in Python
Things I did not previously know or forgot about the Python language and that help me to write more functional programs.

## Iterators
Iterators are objects that return a stream of data. To be an iterator a method must implement the `__next__()` method. In case of a finite stream, this method must raise a **StopIteration**. The `iter()` method tries to convert any object into an **iterator**. Iterators can be expanded to support backwards movement, but this feature is not specified. 

### Data Types That Support Iterators
Dicts support iteration. When calling `iter()` on a dict, it returns a iterator, that will loop over the keys. Starting with Python 3.7 the order of iteration will be the same as the insertion order. There is also the possibility to call `values()` and `items()`. Also the `dict()` constructor accepts an iterator of **(key, values)** tuples:
```python
dict([('a', 1), ('b', 2)])
>>> {'a': 1, 'b': 2}
```

## Generator expressions and list comprehensions
It is possible to chain multiple **for x in sequence** expressions together in a single comprehension:
```python
[f'{x}:{y}' for x in [1, 2, 3, 4] for y in ['a', 'b', 'c']]
```
Here it is important to know:
- the for loops are executed sequentially and not in parallel 
- therefore the lengths can be different
- this means that chaining for loops together is the same as nested for loops

## Generators
Generators are special functions that return an **iterator**. They always contain the `yield` statement. The most important difference between `return` and `yield` is the fact, that on reaching a yield statement the generator's **state of execution** is **preserved**. Generators enable more efficient programming. If you have a large list of entries that you computed inside a function, it may be better to use a generator. This way you dont have to store the entire list in memory and only store the current value and the generators state of execution.

## Built-in's
`map()` accepts a function *f* and a sequence *[a, b, c]* and return a iterator: f(a), f(b), f(c).

`filter(predicate, iter)` returns an iterator over all the sequence elements that meet a certain condition. E.g. the **predicate** returns true for some condition.

`enumerate(iter, start)` counts off elements of an iterable return tuples of type (index, element).

`sorted(iterable, key, reverse)` sorts the iterable. Key is used to specify the key to sort the items after:
```python
d = {'a':1, 'c':4, 'b':7}
sorted(d.items(), key=lambda x: x[1])
[('a', 1), ('c', 4), ('b', 7)]
```

## Itertools
[Best explanation](https://docs.python.org/3/howto/functional.html#creating-new-iterators)
