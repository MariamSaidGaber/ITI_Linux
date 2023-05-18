
#### File handling

#f1 = open("file1.txt","x") 
f1 = open("file1.txt","a+")
#f1 = open("file1.txt","w")

f1.write("Hello user\n")

f1 = open("file1.txt","r")

print(f1.read())
f1.close()		#Must to close file before reading again 

##############################################
f1 = open("file1.txt","r")
print(f1.readlines(10))
f1.close()