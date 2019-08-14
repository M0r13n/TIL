# Observer Pattern
The **Observer Pattern** defines a one-to-many dependency between objects, to that when one object changes state, all of it's dependents are notified and updated.

- subjects and observers are loosely coupled: they know very little about each other
- in Java there is the `java.util.Observable` implementation that might be handy
- the default Java version may lead to errors, if the order of notification is important

## Subject
- the **subject** is the object that is **monitored**
- needs some kind of **notify mechanism** to notify it's observers
- needs to keep track of it's observers (register, unregister, etc)

## Observer
- the **object** that want to be notified when the **subject** changes it's state
- only needs to provide a mechanism to handle a **state change**

## Concrete Python implementation

```python
class Observable(object):
    """ Make a subject observable"""

    def __init__(self):
        # list of callback functions for that extra bit of customizability
        self.callbacks = []

    def subscribe(self, callback):
        # just append the function to callbacks
        self.callbacks.append(callback)

    def notify(self, **kwargs):
        # transfer data as a dict
        data = dict(kwargs)
        for f in self.callbacks:
            f(data)


class Subject(Observable):
    pass


class Observer(object):
    def notify_callback(self, data: {}):
        for k, v in data.items():
            print(k, v)
            # or update the data attributes of this class
            setattr(self, k, v)


s = Subject()
o = Observer()
oo = Observer()
s.subscribe(o.notify_callback)
s.subscribe(oo.notify_callback)
s.notify(data_1="some value", data_2="some other value")
print(getattr(o, "data_1"), o.data_1)
```
