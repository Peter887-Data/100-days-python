from typing import Protocol


class Shape(Protocol):
  def area(self):
    ...
  def double(self):
    ...


class Rectangle(Shape):
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def area(self):
    return self.x * self.y
  def double(self):
    return Rectangle(2 * self.x, 2 * self.y)
  def __str__(self) -> str:
    return f"Rectangle({self.x}, {self.y})"


class Square(Rectangle):
  def __init__(self, x):
    super().__init__(x, x)
  def double(self):
    return Square(2 * self.x)
  def __str__(self) -> str:
    return f"Square({self.x})"


def fancy_shape(shape: Shape):
  print(shape.area())


if __name__ == "__main__":
  fancy_shape(Rectangle(1, 2))
  fancy_shape(Square(2))

  print(Rectangle(1, 2))
  print(Square(2))

  print(Square(2).double())
