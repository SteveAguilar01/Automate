#This is thirtheenth section from Automate the boring stuff with Python
#The lesson will cover requests module with get/download file and writing in binary to your local machine


#Remeber need to import modules you will be using in script

import requests

# store the URL download into a variable
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

#Status code refers to the http https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
res.status_code
print(res)

#print first 300 lines from text file
print(res.text[:300])

#wb is write binary and is to keep the correct formating - unicode encoding
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(1000):
    playFile.write(chunk)

playFile.close()





