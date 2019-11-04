# Notes for the mostly adequate guide to functional programming

I like the style of the book, but I dislike Javascript. Therefore I try to implement all code in Python rather in JS.

# Chapter 3:
I want my functions to be ** pure**, which means that they shouldn't have any ** side effects**. Such side effects is any interaction with the world outside of a function. Examples could be:

- file system changes
- database changes
- console printing and logging
- making http calls

It is not forbidden to use functions with side effects, but when I do, I should do it in a controlled way(Monads, functors).

Also ** pure functions ** must always return the same output given the same input.

# Memoization
This is a caching strategy. Functions that are pure can easily be cached by just memorizing their prior result.

```python
from functools import wraps

# No cache
def square(x): return x * x
a, b, c, d = (square(x) for x in range(4))
same_result = [square(4) for i in range(5)]
print(a, b, c, d, same_result)  # 0 1 4 9 [16, 16, 16, 16, 16]


# Assume that calculating the square of some number is extremely complex and computational expensive.
# Wouldn't it be nice to cache the same result rather than computing it again and again.

def memoize(f):
    cache = {}

    @wraps(f)
    def wrapper(v):
        if v not in cache.keys():
            cache[v] = f(v)
            print("Cache Miss!")
        else:
            print("Cache Hit!")
        return cache[v]

    return wrapper


@memoize
def square(x):
    return x * x


a, b, c, d = (square(x) for x in range(4))
same_result = [square(4) for i in range(5)]
print(a, b, c, d, same_result)  # 0 1 4 9 [16, 16, 16, 16, 16]

```
