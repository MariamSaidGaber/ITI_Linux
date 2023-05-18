from tkinter import *

def Func():
	print("Mariam Said")


###################
def ButtonPress():
	ButtonPress.counter +1
	print("The button pressed", ButtonPress.counter)

ButtonPress.counter =0	


window_1 = Tk()
window_1.title("Welcome to GUI ")

window_1.geometry('500x500')


label_1 =Label(window_1, text = "Hello")
label_1.pack(side = TOP)		#For position

#b1 = Button(window_1, text = "Print Name", bd ="5", command = Func)
#b1.pack(side = TOP)
b2 = Button(window_1, text = "Mariam Said")
b2.pack(side = LEFT)
b3 = Button(window_1, text = "Mariam Said")
b3.pack(side = RIGHT)
b4 = Button(window_1, text = "Close window", bd ="5", command = window_1.destroy)
b4.pack(side = BOTTOM)



photo_1 =PhotoImage(file = 'sea.png')
photo_1 =photo_1.subsample(2,2)
b1 = Button(window_1, text = "Print Name", background = "white", fg ="red",bd ="5",image =photo_1 ,command = ButtonPress)
#b1.place(x =70, y =50)
b1.place(relx =0.5, rely =0.5, anchor = CENTER)
#b1.pack(side = TOP)


#label_1.pack(side = BOTTOM)


#label_1.pack(side = BOTTOM)

window_1.mainloop()