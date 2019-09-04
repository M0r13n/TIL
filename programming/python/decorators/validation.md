# Validation of various kinds (e.g user input)
Instead of checking for errors or validity inside a function, it's way cleaner to use a decorator.
The following snippets demonstrates basically the whole concept:

```python
def repeat_on_error(*exceptions):
    def checking(function):
        def checked(*args, **kwargs):
            while True:
                try:
                    result = function(*args, **kwargs)
                except exceptions as problem:
                    print(f"The following error occured: {type(problem).__name__} ")
                else:
                    return result

        return checked

    return checking


@repeat_on_error(ValueError)
def getNumberOfIterations():
    return int(input("Please enter the number of iterations: "))
```