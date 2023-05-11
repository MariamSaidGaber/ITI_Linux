###################################################3
# pyramid upper side
Num_lines = int(input("Enter num of lines: "))

list1 =[]
for i in range(0,Num_lines):
    list1.append( (" "*Num_lines)  + ("*"*i) )
print("\n".join(list1))      # join fun: to print list element in separate way 


#######################
# Pyramid middle
print(("*"*Num_lines*2))

# Pyramid lower side

list2 =[]
for count in range(0,Num_lines):
    list2.append( (" "*Num_lines) + ("*"*(Num_lines-count-1)) )
print("\n".join(list2))      # join fun: to print list element in separate way 
##################################################  