#This is the third section from Automate the boring stuff with Python
#The lesson will pertain to importing and modules


#First import random module
import random

#importing multiple modules in one line with commas vs spaces? 

#Notice that randint exist within the random module
test00 = random.randint(1,10)
print(test00)

#Another example below of importing modules
import random, sys, os, math
from random import *

#Now try randint
#Generally better to import and use the . as the code is more readable typicallly
test01 = randint(1,10)
print(test01)

sys.exit()

#Test to make sure code exits - anything after will not be ran
print("should not run")