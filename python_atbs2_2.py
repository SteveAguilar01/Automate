#This is the second section, 6th and 7th lesson from Automate the boring stuff with Python
#The lesson will focus on while and for loops


#Set variable for spam
spam = 0
while spam < 5:
    print('I am spam')
    spam = spam + 1

#While spam is less than 5 add 1 - this will loop when the condition is true
#Once spam is no longer less than 5 it is false and then stop
#Spam variable is being added to from 0 - this is call an iteration 



#Lets try this as a joke loop - we ask the user literally for 'your name'
#Also lets give the user a little hint with an if statement they still put in the wrong answer

name = ''
while name != 'your name':
    print ('Please type "your name"')
    name = input()
    
    if name != 'your name':
        print('Think about what I am really asking :-)')
print ("Hehe good job!")
