# Critter Zoo
# A zoo containing a list of Critter objects.

# CONTAINMENT - one object containing other objects.  In this context, our Zoo
#               objects will contain Critter objects.

class Critter_zoo():
  """A zoo containing virtual Critter pets"""
  def __init__(self, n, crits = None):
    """initializes a zoo with a name and a list of Critters"""
    if crits == None:
      crits = []
    self._name = n
    # the zoo maintains a list of all current critters at the zoo
    self._critters = crits # list containing references to Critter objects

  def get_crits(self):
    """returns the list of references to Critter objects"""
    return self._critters
        
  def get_name(self):
    """returns the name of the zoo"""
    return self._name

  def add_critter(self, crit):
    """adds a Critter object to the zoo"""
    self._critters.append(crit)

  # CHALLENGE: create a del_crit method to remove a Critter from the zoo and a 
  #             find_crit method to return a reference to a Critter at the zoo
  def find_critter(self, name):
    """locates a Critter at the zoo and returns a reference to it"""
    for i in self._critters:
      crit_name = i.get_name()
      if crit_name == name:
        return i
    print("Critter is not at the zoo.")
    
  def del_critter(self, name):
    """deletes a Critter object from the zoo"""
    for i in range(len(critters)):
      crit_name = self._critters[i].get_name()
      if crit_name == name:
        self._critters.pop(i)
    print("Critter " + name + " is not at the zoo.")

  def __str__(self):
    """string representation of a Critter zoo"""
    string = "\nZoo: " + self._name
    string += "\n" + str(len(self._critters)) + " Critters at the zoo..."
    for i in self._critters:
      string += "\n" + i.get_name()
    return string