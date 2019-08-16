# Decorator Pattern
- allows to **extend** existing code without **modifying** it
- more common in Java than it is in Python
- define an **ABC** for the components and an **ABC** for the decorators
- each decorator stores it's decorated object in an instance variable
- methods that change the behavior of the decorated object do first call the objects methods and then change the result and finally return the new result


## ABC in Python
- in Python there is no native language support for ABC's
- **BUT** there is the abc module
- `from abc import ABC, abstractmethod`
- a class extending an ABC cannot be **instantiated** as long as there are unimplemented **abstractmethods**


## Python Code

```python
from abc import ABC, abstractmethod


class AbstractCoffee(ABC):
    """ Abstract Base Class for Coffee"""

    @abstractmethod
    def get_cost(self) -> float:
        pass

    @abstractmethod
    def get_ingredients(self) -> []:
        pass


class AbstractCoffeeDecorator(AbstractCoffee):
    """ Abstract Base Class for Decorators"""

    def __init__(self, decorated_coffee: AbstractCoffee):
        self.decorated_coffee = decorated_coffee

    def get_cost(self) -> float:
        return self.decorated_coffee.get_cost()

    def get_ingredients(self) -> []:
        return self.decorated_coffee.get_ingredients()


class BlackCoffee(AbstractCoffee):
    """ Concrete Coffee class"""

    def get_cost(self):
        return 1.0

    def get_ingredients(self):
        return ["Coffee"]


class Sugar(AbstractCoffeeDecorator):
    def get_cost(self):
        return self.decorated_coffee.get_cost() + 0.25

    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients() + ['Sugar']


class Milk(AbstractCoffeeDecorator):
    def get_cost(self):
        return self.decorated_coffee.get_cost() + 0.65

    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients() + ['Milk']

```
