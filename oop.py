# object --> laptop ->
# name --> props

class Person:
    # constructor
   def __init__(self, name, dob, color, weight, height):
       self.name = name
       self.dob = dob
       self.color = color
       self.weight = weight
       self.height = height
   def display(self):
       print(f"Nmae is {self.name} and DOB is {self.dob}")
# blueprint for creating objects
