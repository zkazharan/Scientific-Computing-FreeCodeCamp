class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    classname = self.__class__.__name__
    return classname + '(width=' + str(self.width) + ', height=' + str(self.height) + ')'
  
  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5
  
  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return 'Too big for picture.'

    picture = ''
    for y in range(self.height):
      for x in range(self.width):
        picture += '*'
      picture += '\n'

    return picture

  def get_amount_inside(self, shape):
    self.x_index = self.width // shape.width
    self.y_index = self.height // shape.height
    return self.x_index * self.y_index

class Square(Rectangle):

  def __init__(self, side):
    self.width = side
    self.height = side

  def __str__(self):
    classname = self.__class__.__name__
    return classname + '(side=' + str(self.width) + ')'
  
  def set_side(self, side):
    self.width = side
    self.height = side

  def set_width(self, side):
    self.set_side(side)

  def set_height(self, side):
    self.set_side(side)