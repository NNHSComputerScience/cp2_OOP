# Private Critter
# Demonstrates private attributes and private methods
#   To encourage encapsulation, you can declare attributes or methods as 'private',
#   meaning only other methods of the object should access or invoke it.
#   However, privacy is only a convention in Python; there is no true privacy
#   as in other languages. 

class Critter:
    """A virtual pet"""
    def __init__(self, name, mood = "indifferent"): 
        """constructor to set Critter attributes"""
        print ("A new critter has been born!")
        self.name = name                    # public attribute
        # PRIVATE ATTRIBUTE - DO NOT access outside class definition. 
        #   Uses a single underscore prefix to indicate the privacy.
        self._mood = mood                  # private attribute
        # double underscore can simulate privacy, but it's not really meant for it
        self.__age = 0                  # attribute hidden (but not really)
    
    # PRIVATE METHOD - DO NOT access outside the class definition.
    def _private_method(self):             # private method
        """private method example for class Critter"""
        print ("This is a private method.")

    def get_mood(self):                     # public method
        """Return's the Critter's mood"""
        self._private_method() # accessing private method through public method
        return self._mood

def main():
    crit = Critter("Poochie","happy") 
    
    print("\nAccessing private attributes:")
    print(crit.name) #  access public attributes directly
    print(crit._mood) # access not prevented, but NEVER DO IT!
    print(crit.__age) # access prevented, but there's a hack...
    print(crit._Criter__age) # still directly accessible!
    print(crit.get_mood()) # OK to access a private attribute with a public method
    
    print("\nCalling private methods:")
    crit._private_method() # not prevented, but NEVER DO IT!
    crit.public_method()   # OK to access a private method through a public method
    
main()
input("\n\nPress the enter key to exit.")
Displaying private_critter_finished.py.
