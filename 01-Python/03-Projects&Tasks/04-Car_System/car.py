
############### Car sysyem ###########
import sys

class Car():
	
	def __init__(self, air=0, volume=0,speed =0):
	
		self.speed = speed
		self.air = air
		self.volume = volume
		self.system ={"Speed":self.speed,"Air_condi":self.air,"Volume":self.volume,
		"Window_FrontRight":"closed", "Window_FrontLeft":"closed", "Window_BackRight":"closed", "Window_BackLeft":"closed"}
	
	def Speed(self):
		self.system["Speed"] = int(input("Please enter the speed: "))
		
	def Air_Cond(self):
		self.system["Air_condi"] = int(input("Please enter the degree: "))
	
	def Volume(self):
		self.system["Volume"]  = int(input("Please enter the volume degree: "))

################   Windows ###########
	def Front_Right(self,state1):
		self.system["Window_FrontRight"] = state1
		
	def Front_Left(self,state2):
		self.system["Window_FrontLeft"] = state2
		
	def Back_Right(self,state3):
		self.system["Window_BackRight"] = state3
		
	def Back_Left(self,state4):
		self.system["Window_BackLeft"] = state4
#####################################	
	def Open(self):
		
			print('''
	1- Front_Right Window
	2- Front_Left Window
	3- Back_Right Window
	4- Back_Left Window	
	5- All windows
			''')
			window = "open"
			try:
				wind = int(input("Choose: "))
			except:
				print("Please choose from 1:5 ")
			else:
				if wind == 1:
					Car.Front_Right(self,window)
				
				elif wind == 2:
					Car.Front_Left(self,window)
					
				elif wind == 3:
					Car.Back_Right(self,window)
					
				elif wind == 4:
					Car.Back_Left(self,window)	
					
				elif wind == 5:
					Car.Front_Right(self,window)
					Car.Front_Left(self,window)
					Car.Back_Right(self,window)
					Car.Back_Left(self,window)
					
	def Close(self):
		
			print('''
	1- Front_Right Window
	2- Front_Left Window
	3- Back_Right Window
	4- Back_Left Window	
	5- All windows
			''')
			window = "closed"
			try:
				wind = int(input("Choose: "))
			except:
				print("Please choose from 1:5 ")
			else:
				if wind == 1:
					Car.Front_Right(self,window)
				elif wind == 2:
					Car.Front_Left(self,window)
				elif wind == 3:
					Car.Back_Right(self,window)
				elif wind == 4:
					Car.Back_Left(self,window)
				elif wind == 5:
				
					Car.Front_Right(self,window)
					Car.Front_Left(self,window)
					Car.Back_Right(self,window)
					Car.Back_Left(self,window)
	def Windows(self):
		print('''
1- Open
2- Close		
		''')
		try:
			window_state = int(input("Choose: "))
		except:
			print("choose 1 or 2")
		else:
			if window_state == 1:
				Car.Open(self)
			elif window_state == 2:
				Car.Close(self)
	
	
	def Display(self):
	
		print("Speed is: ",(self.system["Speed"]))
		print("Air degree is: ",(self.system["Air_condi"]))
		print("Volume degree is: ",(self.system["Volume"]))	
		print("Window Front Right is: ",(self.system["Window_FrontRight"]))	
		print("Window Front Left is: ",(self.system["Window_FrontLeft"]))	
		print("Window Back Right is: ",(self.system["Window_BackRight"]))
		print("Window Back Left is: ",(self.system["Window_BackLeft"]))		

	def Options(self):
		
		print('''
1- Speed control
2- Air condithioning
3- Volume
4- Windows
5- Display all 
6- Exit		
		''')
		
		try:
			choice = int(input("Please choose from 1 to 6: "))
		except:
			print("Please choose from 1 to 6 only")
		else:
			if choice == 1:
				Car.Speed(self)
			elif choice == 2:
				Car.Air_Cond(self)
			elif choice == 3:
				Car.Volume(self)
			elif choice == 4:
				Car.Windows(self)				
			elif choice == 5:
				Car.Display(self)
			elif choice == 6:
				print("Thank you")
				sys.exit()
		
toyota = Car(0) 
while True:
	toyota.Options()

