import sys


while True:
	choice = int(input('''Please enter 
	1- for info about capitalize
	2- for info about casefold 
	3- for Exit
	'''))


	if choice == 1:
			print('''
	Definition and Usage:
	The capitalize() method returns a string where the first character is upper case, and the rest is lower case.
			
		Example:
		txt = "hello, and welcome to my world."

		x = txt.capitalize()

		print (x)
			
			''')
		
			
	elif choice == 2:
			print('''
	Definition and Usage:
	The casefold() method returns a string where all the characters are lower case.
	This method is similar to the lower() method, but the casefold() method is stronger, more aggressive, meaning that it will convert more characters into lower case, and will find more matches when comparing two strings and both are converted using the casefold() method.
		
		Example:
		txt = "Hello, And Welcome To My World!"

		x = txt.casefold()

		print(x)	
				
			''')
		
	elif choice == 3:
			print("Thank you")
			sys.exit()
			