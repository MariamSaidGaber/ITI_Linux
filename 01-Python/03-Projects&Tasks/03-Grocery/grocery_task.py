import sys

class  Grocery():

		def __init__(self):
		
			self.Grocery_List = [('milk',30),('egg',5),('cheese',25),('bread',4),('water',6),('pepsi',20)]
			self.Client_List = []
			self.Cost_List = []
			self.Total_Cost = 0
			print("Hello, Welcome to our grocery shop.")
			print(self.Grocery_List)
			print('\n')



		def Add_Item(self):
				
			item = input("Enter the type of food: ")
			self.Client_List.append(item)
			quantity = int(input("Enter the quantity: "))
			
			for i in range(len(self.Grocery_List)):
				if item == self.Grocery_List[i][0]:
					#print("index is: ",i)
					Cost = (quantity* self.Grocery_List[i][1])
			
			self.Cost_List.append(Cost)
			


		def Remove_Item(self):
			remove_item = input("Enter the type of food that you want to remove: ")
			for counter in range(len(self.Client_List)):
				if remove_item == self.Client_List[counter-1]:
					self.Client_List.pop(counter-1)
					self.Cost_List.pop(counter-1)
					
			print(self.Client_List)
			print(self.Cost_List)
		
		
		def Display(self):
			self.Total_Cost =0
			for i in range(len(self.Client_List)):
				print(self.Client_List[i],':',self.Cost_List[i])
				self.Total_Cost+=self.Cost_List[i-1]
			print("Total cost is: ",self.Total_Cost)
	

		
	
		def Options(self):
		
			while True:
				print('''
						Options: 
						1- Add Item
						2- Display Items
						3- Remove Item
						4- Exit
						''')
				try:
					choice = int(input("Choose from 1 to 4 :"))
				except:
					print("Error choose from 1 to 4")
				#	continue
				else:	
					if choice == 1:
						Grocery.Add_Item(self)
					elif choice == 2:
						Grocery.Display(self)
					elif choice == 3:
						Grocery.Remove_Item(self)
					elif choice == 4:
						Grocery.Display(self)
						print("Thank you")
						sys.exit()	
	
	
client = Grocery()
client.Options()
