import sys
from PyQt5 import QtWidgets, uic, QtCore, QtGui
 
app = QtWidgets.QApplication(sys.argv)
 
window = uic.loadUi("calc.ui")
window.show()

############ To convert GUI


check = True
answer = None
########3Logic code

def zero():
	global check
	if check:
		window.lineEdit.setText(window.lineEdit.text() + "0")
	if not check:
		window.lineEdit.setText("")
	check = True
		
def one():	
	global check
	if check:
		window.lineEdit.setText(window.lineEdit.text() + "1")
	if not check:
		window.lineEdit.setText("1")
	check = True
	
	
def two():
	global check
	if check:
		window.lineEdit.setText(window.lineEdit.text() + "2")
	if not check:
		window.lineEdit.setText("2")
	check = True	
	
	
def three():
	global check
	if check:
		window.lineEdit.setText(window.lineEdit.text() + "3")
	if not check:
		window.lineEdit.setText("3")
	check = True	
	
	
def four():
	global check
	if check:
		window.lineEdit.setText(window.lineEdit.text() + "4")
	if not check:
		window.lineEdit.setText("4")
	check = True
	
	
def five():	
	global check
	if check:
		window.lineEdit.setText(window.lineEdit.text() + "5")
	if not check:
		window.lineEdit.setText("5")
	check = True
		
	
def six():
	global check
	if check:
		window.lineEdit.setText(window.lineEdit.text() + "6")
	if not check:
		window.lineEdit.setText("6")
	check = True	
	
	
def seven():
	global check
	if check:
		window.lineEdit.setText(window.lineEdit.text() + "7")
	if not check:
		window.lineEdit.setText("7")
	check = True	
	

def eight():
	global check
	if check:
		window.lineEdit.setText(window.lineEdit.text() + "8")
	if not check:
		window.lineEdit.setText("8")
	check = True
	
	
def nine():
	global check
	if check:
		window.lineEdit.setText(window.lineEdit.text() + "9")
	if not check:
		window.lineEdit.setText("9")
	check = True	
		
	
def plus():	
	global check
	window.lineEdit.setText(window.lineEdit.text() + "+")
	check = True
	
def minus():	
	global check
	window.lineEdit.setText(window.lineEdit.text() + "-")
	check = True
	
def mul():
	global check
	window.lineEdit.setText(window.lineEdit.text() + "*")
	check = True
	
def div():	
	global check
	window.lineEdit.setText(window.lineEdit.text() + "/")	
	check = True	
	###### eval fun
def equal():
	global check
	global answer
	try:
		window.lineEdit.setText( str(eval(window.lineEdit.text()) ) )		#eval's input is string, but output is integer	
		answer = window.lineEdit.text()
	except ZeroDivisionError:
		window.lineEdit.setText("Mathematical error")
		
	except SyntaxError:
		window.lineEdit.setText("Invalid operation")
	
	except:
		window.lineEdit.setText("Error")	
	check = False
	
def dot():	
	global check
	if check:
		window.lineEdit.setText(window.lineEdit.text() + ".")	
	if not check:
		window.lineEdit.setText(".")
	check = True	

	
def ans():	
	global answer
	global check
	if answer != None:
	
		if check:
			window.lineEdit.setText(window.lineEdit.text()+ str(answer))	
		if not check:
			window.lineEdit.setText(answer)
	if answer == None:
			window.lineEdit.setText("")	
	check = True



def shift_left():
	global check
	if check:
		window.lineEdit.setText(window.lineEdit.text() + "<<")
	if not check:
		window.lineEdit.setText("<<")
	check = True	

	
def shift_right():	
	global check
	if check:
		window.lineEdit.setText(window.lineEdit.text() + ">>")
	if not check:
		window.lineEdit.setText(">>")
	check = True	
	
def modul():	
	global check
	if check:
		window.lineEdit.setText(window.lineEdit.text() + "%")
	if not check:
		window.lineEdit.setText("%")
	check = True

	
def bracket_1():	
	global check
	if check:
		window.lineEdit.setText(window.lineEdit.text() + "(")	
	if not check:
		window.lineEdit.setText("(")
	check = True


def bracket_2():
	global check
	if check:
		window.lineEdit.setText(window.lineEdit.text() + ")")
	if not check:
		window.lineEdit.setText(")")
	check = True		
		

#clear
def ac():	
	window.lineEdit.setText("")	

def delete():	
	window.lineEdit.setText(window.lineEdit.text()[0:-1])	#delete last element	
	
#connections
window.pushButton_11.clicked.connect(zero)	
window.pushButton_5.clicked.connect(one)
window.pushButton_6.clicked.connect(two)
window.pushButton_9.clicked.connect(three)
window.pushButton_2.clicked.connect(four)
window.pushButton_3.clicked.connect(five)
window.pushButton_8.clicked.connect(six)
window.pushButton.clicked.connect(seven)
window.pushButton_4.clicked.connect(eight)
window.pushButton_7.clicked.connect(nine)


window.pushButton_10.clicked.connect(ans)	
window.pushButton_12.clicked.connect(dot)
window.pushButton_16.clicked.connect(equal)
window.pushButton_14.clicked.connect(plus)
window.pushButton_13.clicked.connect(minus)
window.pushButton_21.clicked.connect(mul)
window.pushButton_15.clicked.connect(div)
window.pushButton_24.clicked.connect(modul)
window.pushButton_20.clicked.connect(bracket_2)
window.pushButton_17.clicked.connect(bracket_1)

window.pushButton_18.clicked.connect(delete)	
window.pushButton_19.clicked.connect(ac)
window.pushButton_23.clicked.connect(shift_left)
window.pushButton_22.clicked.connect(shift_right)






######################### End
sys.exit(app.exec())