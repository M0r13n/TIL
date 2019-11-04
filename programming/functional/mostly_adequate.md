# Notes for the mostly adequate guide to functional programming

I will use JS and Python to implement some of the examples.

# Chapter 3
I want my functions to be **pure**, which means that they shouldn't have any **side effects**. Such side effects is any interaction with the world outside of a function. Examples could be:

- file system changes
- database changes
- console printing and logging
- making http calls

It is not forbidden to use functions with side effects, but when I do, I should do it in a controlled way(Monads, functors).

Also **pure functions** must always return the same output given the same input.

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

# Chapter 4
Currying is a concept of calling functions. The concept is quite simple:
I can call a function with fewer arguments that it actually expects. It then returns a function that takes the remaining arguments. Currying functions are called **higher order function**, because they take or return a function.

```python


def add(x): return lambda y: x + y


incr = add(1)
add10 = add(10)

print(type(incr), type(add))  # <class 'function'> <class 'function'>
print(add(3))  # returns lambda y: 3 + y
print(incr(2))  # 3
print(add10(90))  # 100

```
When I first read about currying I got confused with **partial functions**. A pattern that I like and that I used often before. Those are two similar, but ** not the same ** concepts.
**Where partial application takes a function and from it builds a function which takes fewer arguments, currying builds functions which take multiple arguments by composition of functions which each take a single argument.**
So partial application transforms a function from *n - ary* to *(x - n) - ary*, where currying from *n-ary* to *n \* 1-ary)*. Partial application just wraps the old function, whereas currying creates **new functions**.

```python
import traceback


# Initial function with 3 arguments
def some_func(a, b, c):
    return f"{a}-{b}-{c}"


# With partial application it could become
def partial(func, a):
    return func(a, 2, 3)


# But when curried becomes:
def curry_func(a):
    return lambda b: lambda c: f"{a}-{b}-{c}"


print(some_func(1, 2, 3))  # 1-2-3, call stack is 1 level deep
print(partial(some_func, 1))  # 1-2-3, call stack is 2 levels deep
print(curry_func(1)(2)(3))  # 1-2-3, call stack is 3 levels deep

```
