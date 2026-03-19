# Property Critter
# Demonstrates a PROPERTY in Python, which is a special kind of attribute that 
# computes its value when accessed.  A property is defined using the 
# @property decorator and a method that calculates the value of the property.

class Critter(object):
    """A virtual pet"""

    def __init__(self, name):
        """Initializes the Critter's attributes"""
        self.name = name
        self.age = 0
        self.mood = "happy"
        print("\nA new critter",self.name,"has been born and is", self.age, "years old!")

    # A property is defined using the @property decorator 
    #   and a method that calculates the value of the property.
    @property
    def mood_description(self): 
        """Returns a description of the Critter's mood"""
        if self.mood == "happy":
            return f"{self.name} is feeling happy and content."
        elif self.mood == "sad":
            return f"{self.name} is feeling sad and down."
        elif self.mood == "sleepy":
            return f"{self.name} is feeling sleepy and ready for a nap."
        else:
            return f"{self.name} is feeling {self.mood}."

    @property
    def description(self):
        """Returns a description of the Critter"""
        return f"{self.name} is {self.age} years old and is feeling {self.mood}."


def main():
    crit = Critter("Poochie")
    print(crit.description)

main()