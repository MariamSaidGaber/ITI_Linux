###################################################3
import time

def Arrow_Right(lines):
    #Arrow upper side
    list1 =[]
    for i in range(0,lines):
        list1.append( (" "*(lines*2)) + (" "*lines)  + ("*"*i) )
    print("\n".join(list1))      

    #######################
    # Middle side
    print((" "*(lines*2)) +("*"*lines*2))
    # Arrow lower side

    list2 =[]
    for count in range(0,lines):
        list2.append((" "*(lines*2)) + (" "*lines) + ("*"*(lines-count-1)) )
    print("\n".join(list2))       
################################################################
 
def Arrow_Left(lines):
    #Arrow upper side
    list1 =[]
    for i in range(0,lines):
        list1.append( (" "*(lines-i) ) + ("*"*i) )
    print("\n".join(list1))     

    #######################
    # Middle side
    print(("*"*lines*2))
    #####################
    # Arrow lower side
    list2 =[]
    for count in range(0,lines):
        list2.append((" "*(count+1)) + ("*"*(lines-count-1)) )
    print("\n".join(list2))        
################## 

def Arrow_Up(lines):
    
    list1 =[]
    for i in range(0,(lines+1)):
        list1.append((" "*lines) + (" "*(lines-i) ) + ("*"*(2*i-1)) )
    print("\n".join(list1))      
    for i in range(0,lines):
        print((" "*lines) + (" "*(lines-1)) + ("*")) 

#################################
   
def Arrow_Down(lines):
    
    for i in range(0,lines):
        print((" "*lines) + (" "*(lines-1)) + ("*") )
    
    list2 =[]
    for count in range(0,lines):
        list2.append((" "*lines) + (" "*(count+1)) + ("*" *((lines-count-1)*2-1)) )
    print("\n".join(list2))      \
    


def Display(Num_lines):
    
	Arrow_Right(Num_lines)
	time.sleep(1)	
	Arrow_Down(Num_lines)
	time.sleep(1)
	Arrow_Left(Num_lines)
	time.sleep(1)
	Arrow_Up(Num_lines)
	time.sleep(1)

        
		


Num_lines = int(input("Enter num of lines: "))
#while True:
Display(Num_lines)
	