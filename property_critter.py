# Property Critter
# Demonstrates a PROPERTY, an object with methods that allow indirect access
#   to attributes and often impose some sort of restriction on that access.
#

class Critter(object):
    """A virtual pet"""
    def __init__(self, name):
        print("A new critter has been born!")
        self.__name = name

    @property  # property decorator controls access to private attribute __name
    def name(self):  # method (name) has same name as property (name)
        """Returns a private attribute (and gives indirect access to it)"""
        return self.__name
    
    @name.setter  # decorator accesses the setter attribute of 'name' property
    def name(self, new_name):
        """Method called when attempting to set a new value for 'name' property"""
        if new_name == "": # handles attempting to rename to an empty string
            print("A critter's name can't be an empty string.")
        else:
            self.__name = new_name  # changes private attribute to new value
            print("Name change successful.")

    def talk(self):
        """Makes Critter say its name"""
        print("\nHi, I'm", self.name)

def main():
    crit = Critter("Poochie")
    crit.talk()

    print("\nMy critter's name is:", end= " ")
    print(crit.name)

    print("\nAttempting to change my critter's name to Randolph...")
    crit.name = "Randolph" # successfully changing the name property
    print("My critter's name is:", end= " ")
    print(crit.name)

    print("\nAttempting to change my critter's name to the empty string...")
    crit.name = "" # unsuccessfully changing the name property
    print("My critter's name is:", end= " ")
    print(crit.name)
main()

input("\n\nPress the enter key to exit.")
