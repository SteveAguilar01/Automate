#This is thirtheenth section from Automate the boring stuff with Python
#The lesson will be on web scraping

#Remeber need to import modules you will be using in script
import webbrowser, sys, pyperclip


# quick test - webbrowser.open('https://google.com')

#Check if cmd line args were passed

if len(sys.argv) > 1:
    address = ''.join(sys.argv[1:])

else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
#To make script easier to run lets create batch file or similar on Linux/Mac


