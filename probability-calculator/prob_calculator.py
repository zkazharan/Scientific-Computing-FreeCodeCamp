import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **kwargs):
    self.contents = list()

    for key, value in kwargs.items():
      for i in range(value):
        self.contents.append(key)

  def draw(self, number):
    taken = list()

    if number > len(self.contents):
      return self.contents
    
    for i in range(number):
      taken.append(self.contents.pop(random.randrange(len(self.contents))))
    return taken

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  
  count = 0
  
  for i in range(num_experiments):
    expected_copy = copy.deepcopy(expected_balls)
    hat_copy = copy.deepcopy(hat)

    obtained = hat_copy.draw(num_balls_drawn)

    for color in obtained:
      if color in expected_copy:
        expected_copy[color] -= 1

    if all(x <= 0 for x in expected_copy.values()):
      count += 1

  return count / num_experiments