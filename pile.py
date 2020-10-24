# Sion Fandrick
import random

class PileGen:
  """A simple Pile Generator class"""
  def __init__(self):
    self.pile_list = list()
  
  def create(self, pile):
    """Create the pile to then be drawn from"""
    self.pile_list = pile
  
  def read(self):
    """Return the contents of the pile as a list"""
    return list(self.pile_list)

  def update(self, option_old, option_new=""):
    """Change option in pile, if option_new is blank will delete entry"""
    if option_old == option_new:
      return
    self.pile_list.remove(option_old)
    if option_new != "":
      self.pile_list.append(option_new)

  def get(self, keep=None):
    """Get an option from the Pile, optionally choosing to delete"""
    result = random.choice(self.pile_list)
    if keep is None:
      self.update(result)
    return str(result)


if __name__ == '__main__':
  pile = PileGen()
  pile.create(['a', 'b', 'c'])
  assert len(pile.read()) == 3, "Mismatch in size"

  for x in range(len(pile.read())):
    pile.get(keep=True)
  assert len(pile.read()) == 3, "Mismatch in size, after getting with keep set"

  start = len(pile.read())
  pile.get()
  assert len(pile.read()) == 2, "Size not decreasing properly"

  old = pile.read()
  pile.create(['x', 'y', 'z'])
  assert old != pile.read(), "Pile is being created incorrectly"

  old = pile.read()
  old.sort()
  pile.update('x', option_new='1')
  new = pile.read()
  new.sort()
  assert old[0] != new[0], "Update failed with new value %s vs %s" % (old, new)