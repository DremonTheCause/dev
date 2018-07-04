#This script requires python 3.7 which can be downloaded here: https://www.python.org/downloads/release/python-370/
#Import the built-in JSON Library
import json

#Create a new List from the parsed Phones Numbers
directory = list()
#Open the people.json file as variable f
with open('people.json') as f:
	#import f as python dict "data"
	data = json.load(f)

	#iterate through data
	for i in data:
		#Find key "phone"
		currentNumber = i['phone']
		newPhone = ""
		#Set l to the length of the phone number
		l = len(currentNumber)
		#Create a new string x
		x = ""
		#Iterate through all the digits of the Phone Number
		for n in currentNumber:
			#Check if each character is a integer by attemtping to convert it to a int
			
			try:
				int(n)
				#Add that character to x
				x = x + n
				##Store the length of x
				length = len(x)
			#If the character is not a integer, throw an error
			except ValueError:
				#At this point, check if length is greater than of equal to 3
				if length >= 3:
					#If true, concatenate it to the end of variable "newPhone"
					newPhone = newPhone + x
					#print("newPhone is " + newPhone)
				#Reset x to nothing
				x = ""
		#Add the last value of x to newPhone
		#check if "length is greater than of equal to 3. 
		if length >= 3:
					#If true, concatenate it to the end of variable "newPhone"
					newPhone = newPhone + x
		#Add "newPhone" to the end of list "directory"
		directory.append(newPhone)
		#Iterate through each entry in "directory"
		for i in directory:
			#Set n to nothing
			n = ""
			#Add a hyphon after the 3rd and 6th characters in the Phone Number
			n = i[0:3] + "-" + i[3:6] + "-" + i[6:10]
		#Print the Phone Number
		print(n)