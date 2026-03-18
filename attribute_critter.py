# Name: 
# Date: 
# Chapter 8 Notes: Object Oriented Programming
# attribute_critter.py
# Description: Demonstrates defining and initializing objects with attributes and the __str__ method

# An ATTRIBUTE is data that is associated with an object, sometimes called an instance variable.  
#   A constructor gives the programmer an opportunity to set up the initial attributes for an object.

class Critter:
    """A virtual pet"""
    
    # The constructor is automatically invoked when a new object is instantiated and can be used to 
    #     initialize the attributes of an object.
    def __init__(self, new_name, new_mood = "happy"): # name is a parameter; still need self
        """Initializes the Critter's attributes"""
        # SELF.ATTRIBUTE is the syntax for attributes
        self.name = new_name #assigning the parameter value as the object's attribute 
        self.mood = new_mood  # self.mood is the object's attribute
        self.age = 0 # every Critter begins life at age 0
        print("\nA new critter",self.name,"has been born and is", self.age, "years old!")

    # A STRING METHOD creates a string representation of your object and returns it; typically the string will contain a description of all the attributes of an object.  
    #     All objects should include a string method and you are required to follow the def __str__(self): method header naming scheme. 
    #     The returned string will now display when the object is printed.
    def __str__(self):
        """String representation of a Critter object"""
        my_string = ""
        my_string += "\nname: " + self.name
        my_string += "\nmood: " + self.mood
        my_string += "\nage: " + str(self.age)
        return my_string 
    
    # CHALLENGE: write a method that prints the object's name, age, and mood
    def talk(self):
        """Critter says its name"""
        print("Hi.  I'm", self.name + ", I'm", self.age, "years old,", "and I'm", self.mood + ".")

def main():
    crit1 = Critter("Poochie", "happy") # only 2 arguments sent!
    crit1.talk()

    crit2 = Critter("Randolph", "sad")
    crit2.talk()
    
    # INSTRUCTOR'S NOTE: demonstrate below code before implementing the string method.
    # use the String method by printing the object's reference variable
    print("\nPrinting crit1:")
    print(crit1)
    print("\nPrinting crit2:")
    print(crit2)
    
    

main()
