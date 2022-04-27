#This is the first section from Automate the boring stuff with Python
#For now it will start simple and we will slowly build upon this while pushing to the github repo

#Create a variable
#Notice output that pickle is actually 42 and saying pickle are different!
pickle = 42
print('pickle? or ' + str(pickle))

#Following Section 1 we will now add input
#Now I decided to have little fun with it
print('What is name the of your pickle?')
rempickle = input()
print('That is good you remember!' + rempickle)
print('Your pickle name is quite long, it is:')
print(len(rempickle))
print('How many years you owned that pickle??')

#Notice that we can take multiple inputs and save them each into
#their own variables!
agepickle = input()
print('Your pickle age will be ' + str(int(agepickle)+ 1) + ' in a year.')