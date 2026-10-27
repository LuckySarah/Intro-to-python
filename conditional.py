# if else statements
import sys

name = "Jake"

name = input("What is your name? ")

age = input("Enter your age:") #20 '20'

if not age.isnumeric():
    print("Invalid age")
    #terminate the program
    os._exit(0)
   # sys.exit()

if int(age) > 18:
    print(name + " is an Adult")
else:
    print(name + " is a Child")

# lists, boolean, tuples, dictionary, loops
