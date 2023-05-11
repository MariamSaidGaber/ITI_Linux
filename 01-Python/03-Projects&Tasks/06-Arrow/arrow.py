###################################################3


def Arrow_Right(lines):
    #Arrow upper side
    list1 =[]
    for i in range(0,lines):
        list1.append( (" "*lines)  + ("*"*i) )
    print("\n".join(list1))      # join fun: to print list element in separate way 

    #######################
    # Middle side
    print(("*"*lines*2))
    # Arrow lower side

    list2 =[]
    for count in range(0,lines):
        list2.append( (" "*lines) + ("*"*(lines-count-1)) )
    print("\n".join(list2))      # join fun: to print list element in separate way 
################################################################3    
def Arrow_Left(lines):
    #Arrow upper side
    list1 =[]
    for i in range(0,lines):
        list1.append( (" "*(lines-i) ) + ("*"*i) )
    print("\n".join(list1))      # join fun: to print list element in separate way 

    #######################
    # Middle side
    print(("*"*lines*2))
    #####################
    # Arrow lower side
    list2 =[]
    for count in range(0,lines):
        list2.append((" "*(count+1)) + ("*"*(lines-count-1)) )
    print("\n".join(list2))      # join fun: to print list element in separate way     
################## 
    
Num_lines = int(input("Enter num of lines: "))
Arrow_Right(Num_lines)   
Arrow_Left(Num_lines)