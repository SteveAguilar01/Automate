#This is the second section, 6th lesson from Automate the boring stuff with Python
#The lesson will focus on if, else, and elif statements

# 
#Set variable for name
#Compare the name to another name with if

name = "Tony"
if name == "Tony":
    print("Howdy Tony!")
print('Done')

#Notice because name did equal Tony we get Howdy Tony from if statement 


#Lets add to our previous idea with else statement and some user input
#Ask user question then store their input to variable name
print("This Tony or Bob?")
name = input()

#if Tony print Howdy Tony or elif Bob print Howdy Bob and if both fail else statement will print
#Lets try it out!
#Side note - we have not put in a way to capture if a person enters name in lowercase
#Therefore tony will not work and must be entered case sensitive for purpose of demo

if name == "Tony":
    print("Howdy Tony!")
elif name == "Bob":
    print("Howdy Bob!")
else:
    print("If you ain't Tony or Bob - who are you??")

#Important note the order of if and elif statements does matter
#Once one of them comes back as True it will skip the rest of lines going from top to bottom
