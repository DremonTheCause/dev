import json
from pprint import pprint
directory = list()
#open the people.json file as variable f
with open('people.json') as f:
	#import f as python dict "data"
	data = json.load(f)

	#iterate through data
	for i in data:
		#print(i)
		#find keys with named "phone"
		currentNumber = i['phone']
		newPhone = ""

		#print('current phone # is ' + currentNumber)

		l = len(currentNumber)
		x = ""
		for n in currentNumber:
			#print('n is currently ' + n)
			try:
				int(n)	
				x = x + n
				length = len(x)

			#	print('x is currently ' + x)
				
				#print(newPhone)
			except ValueError:
			#print(n + " is not an int")
				#print('the length of x is ' + len(x))
				#print( "The length of x is " + str(length))
				if length >= 3:
					newPhone = newPhone + x
				#	print(newPhone)
				x = ""

		else:
			if length >= 3:
				newPhone = newPhone + x

		directory.append(newPhone)
		#print(directory)
		for i in directory:
			n = ""
			n = i[0:3] + "-" + i[3:6] + "-" + i[6:10]
		print(n)

				

		#json.dump(output, f)