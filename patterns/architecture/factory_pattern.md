# Factory pattern
![class diagram](https://www.tutorialspoint.com/design_pattern/images/factory_pattern_uml_diagram.jpg)

# Code
 
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