import sys

class atm():
	def __init__(self,Name,AccountNum,Balance = 0):
		self.Name = Name
		self.AccountNum = AccountNum
		self.Balance = Balance
		
	def Account_Info(self):
		
		print("\nAccount Information:")
		print("Account Name: "+(self.Name))
		print("Account Number: ",(self.AccountNum))
		print("Account Balance: ",(self.Balance))
		print('')
		
	def Deposite(self,Amount):
		self.Amount = Amount
		self.Balance = self.Balance + self.Amount
		print ("Balance now is: ",(self.Balance))
		print('')
	
	def Withdraw(self,Amount):
		if Amount > self.Balance:
			print("Your balance is not enough")
			print ("Your balance is: ",(self.Balance))
			print('')	
		else: 
			self.Amount = Amount
			self.Balance = self.Balance - self.Amount
			print ("Balance now is: ",(self.Balance))
			print('')
	def Balance_Info(self):
		print("Account Balance: ",(self.Balance))
		print('')
		
	def Options(self):
		print('''
				Options: 
				1- Account Information
				2- Deposite
				3- Withdraw
				4- Balance_Info
				5- Exit
				''')
		try:
			choice = int(input("Choose from 1:5 :"))
		except:
			print("Error choose from 1 to 5")
		#	continue
		else:	
			if choice == 1:
				atm.Account_Info(self)
			elif choice == 2:
				amount = int(input("How much do you want to deposite? "))
				atm.Deposite(self,amount)
			elif choice == 3:
				amount = int(input("How much do you want to withdraw? "))
				atm.Withdraw(self,amount)
			elif choice == 4:
				atm.Balance_Info(self)
			elif choice == 5:
				print("Thank you")
				sys.exit()		
			
	
	
name = input("Enter your Name: ")
num = int(input("Enter your Number: "))	
account_one = atm(name,num)

while True:
	account_one.Options()
