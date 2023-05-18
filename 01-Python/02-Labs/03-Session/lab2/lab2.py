#### File handling
user = input("Please Enter Peripheral's name ")



f1 = open(user+"_Interface.h","x") 
f2 = open(user+"_Config.h","x")
f3 = open(user+"_Private.h","x")
f4 = open(user+"_Program.c","x")
	

	
f1 = open(user+"_Interface.h","w")	
f1.write("#ifndef "+user.upper()+"_INTERFACE_H_\n")
f1.write("#define "+user.upper()+"_INTERFACE_H_\n")
f1.write(" \n")
f1.write("#endif\n")
f1.close()	
	
	
f2 = open(user+"_Config.h","w")	
f2.write("#ifndef "+user.upper()+"_CONFIG_H_\n")
f2.write("#define "+user.upper()+"_CONFIG_H_\n")
f2.write(" \n")
f2.write("#endif\n")
f2.close()	
	
	
f3 = open(user+"_Private.h","w")	
f3.write("#ifndef "+user.upper()+"_PRIVATE_H_\n")
f3.write("#define "+user.upper()+"_PRIVATE_H_\n")
f3.write(" \n")
f3.write("#endif\n")
f3.close()		

f4 = open(user+"_Program.c","w")	
f4.write("#include \""+user+"_Interface.h\"\n")

f4.close()
	

