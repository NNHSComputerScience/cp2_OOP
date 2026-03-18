# Unit 3 Notes: Object Oriented Programming
# simple_critter.py
# Description: Demonstrates a basic class and objects. Introduces the constructor method.

# Defining a Class
#   A user-defined class must be defined using the class keyword before it is used.  
#   Class definitions should include a docstring as the first line of the class definition.  
#   The scope of a class is defined using indentation, much like functions.

#   INSTRUCTOR NOTE: 'vocab.txt' defines the OOP terminology used in this unit so as to not clutter this file.
#       You will want to refer to it as you write the code below.

class Critter:  # class header; class names capitalized by convention
    """A virtual pet""" # docstring to describe class

    # Constructor; must have 'self' parameter; may have other parameters as well
    def __init__(self, name = "Default"): 
        """Constructor of the Critter class"""
        print("A new critter has been born!")
        # Attribute list:
        self.age = 0        
        self.name = name 
        self.mood = "happy" # default mood for all Critters

    # Defining a Method
    def talk(self): # must have 'self' parameter as a reference to the object.  
        """Makes the Critter talk"""
        print("\nHi.  I'm an instance of class Critter named", self.name, "and I'm", self.age, "years old.")

    # INSTRUCTOR NOTE: ask students to come up with other attributes and methods to add to the class.  
    # #     For example, a mood attribute and a sleep method.
    def sleep(self):
        """Makes the Critter sleep"""
        print("\nzzzzzz...ZZZZZZZ...zzzzzzz")
        self.mood = "sleepy" # change the mood attribute to sleepy when the critter sleeps


    def __str__(self):
        """Returns a String representation of a Critter object"""
        my_string = "Critter:"
        my_string += "\nname: " + self.name
        my_string += "\nmood: " + self.mood
        my_string += "\nage: " + str(self.age)
        return my_string 

def main():
    # creating instances of class Critter
    crit1 = Critter() # crit1 is variable reference to a Critter object
    crit2 = Critter("Randolph") # a second Critter object is created and referenced
    
    # Now it's easy to create many objects!
    #for i in range(500):
    #    Critter()

    # accessing the methods of our new objects
    crit1.talk()
    crit2.talk()
    crit1.sleep()
    crit2.sleep()

    # INSTRUCTOR'S NOTE: demonstrate below code before implementing the string method.
    # Use the String method by printing the object's reference variable
    print("\nPrinting crit1:")
    print(crit1)
    print("\nPrinting crit2:")
    print(crit2)

    # show in http://pythontutor.com/

main()
