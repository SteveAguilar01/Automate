#This is the third section from Automate the boring stuff with Python
#The lesson will pertain to def or AKA define functions


#Create first function as a test
def hello():
    print("test1")
    print("test2")
    print("test3")

#This code within the function is not ran until it is called
#Having a function helps save time by not having to hard code this section code multiple times
#Instead you can call the function


#On this function we are adding a parameter from the argument that is passed
def hello(name): #parameter
    print("test1 " + name)

#Below are arguements being passed into the hello function
hello("Bill") # argument
hello("Jill")

# Argument = value passed in the function call
# Parameter = variable inside the function

#Example run
# str(len('hello')) becomes str(5)
# str(5) becomes '5'
# now you can print out the entire because everything is a string
print ('Hello has ' + str(len('hello')) + ' letters in it.')

print('test1', 'test2', 'test3', sep='||||||')