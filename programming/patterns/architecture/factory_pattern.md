# Factory pattern
![class diagram](https://www.tutorialspoint.com/design_pattern/images/factory_pattern_uml_diagram.jpg)

## When to use / Benefits
A cool and simple explanation can be found [here](https://stackoverflow.com/questions/69849/factory-pattern-when-to-use-factory-methods).

> So, to me the factory pattern is like a hiring agency. You've got someone that 
> will need a variable number of workers. This person may know some info they need > in the people they hire, but that's it.

> So, when they need a new employee, they call the hiring agency and tell them 
> what they need. Now, to actually hire someone, you need to know a lot of stuff - 
> benefits, eligibility verification, etc. But the person hiring doesn't need to 
> know any of this - the hiring agency handles all of that.

> In the same way, using a Factory allows the consumer to create new objects 
> without having to know the details of how they're created, or what their 
> dependencies are - they only have to give the information they actually want.


## Code
 
```python
class Shape:
    def draw(self):
        raise NotImplementedError("Implement me!")


class Circle(Shape):
    def draw(self):
        print("I am a Circle")


class Square(Shape):
    def draw(self):
        print("I am a Square")


class ShapeFactory:
    SHAPES = {
        'sq': Square,
        'circ': Circle
    }

    @classmethod
    def get_shape(cls, shape: str) -> Shape:
        assert shape in cls.SHAPES.keys()
        return cls.SHAPES[shape]()


# test driver
c = ShapeFactory.get_shape('circ')
s = ShapeFactory.get_shape('sq')

c.draw()
s.draw()

```