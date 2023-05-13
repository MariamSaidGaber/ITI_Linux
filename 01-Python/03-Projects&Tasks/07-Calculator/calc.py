import math

class Calc():
    def __init__(self):
        self.total = 0
        self.res = 0
        
                
    def Add(self,x,y):
        resault = x+y	
        return(x + y)
        
    def Sub(self,x,y):
        resault = x-y
        return(x - y)

    def Mul(self,x,y):
        resault = x*y
        return(x * y)

    def Div(self,x,y):
        
        if y != 0:
            resault = x/y
            return(x / y)
        else:
            print("Not valid")
            
    def Power(self,x,y):
        resault = x**y
        return(x**y) 
      
    def Div_Remen(self,x,y):
        resault = x%y
        return (x%y)
    
    def Sqart(self,x):
        return (math.sqrt(x))
        
    def Log(self,x):
        base = int (input("Please enter base: "))
        return (math.log(x,base))
        
    def Sin(self,x):
        state = int(input("for Degree press 1: "))
        if state == 1:
            return(math.sin(math.radians(x)))
        else:
            return (math.sin(x))
            
        
        
    def Cos(self,x):
        state = int(input("for Degree press 1: "))
        if state == 1:
            return(math.cos(math.radians(x)))
        else:
            return (math.cos(x))
    
    def Tan(self,x):
        state = int(input("for Degree press 1: "))
        if state == 1:
            return(math.tan(math.radians(x)))
        else:
            return (math.tan(x))      
        
    def Shift_Left(self,x,y):
        return(x<<y)
 
    def Shift_Right(self,x,y):
        return(x>>y)
            
    def Clear(self):
        self.total =0
   
		
    def Options(self):
        calculate = "1"
        while calculate != "0":
            num1 = int (input("PLease Enter Num1: "))

            choice = input("Choose the operator: +, -, *, /, %, ^, sqart, log, sin, cos, tan, <<, >> : ")
   
            while choice not in ("+,-,*,/,%,^,sqart,log,sin,cos,tan,<<,>>"):
                choice = input("Please choose +, -, *, /, %, ^, sqart, log, sin, cos, tan, <<, >>")
                    
            if choice == "+":
                    
                num2 = int (input("Please Enter Num2: ")) 
                print(num1 ,"+", num2, "=",Calc.Add(self,num1,num2) ) 
                
            elif choice == "-":
                
                num2 = int (input("Enter Num2: ")) 
                print(num1 ,"-", num2, "=",Calc.Sub(self,num1,num2) ) 
                
            elif choice == "*":
                
                num2 = int (input("Enter Num2: ")) 			
                print(num1 ,"*", num2, "=",Calc.Mul(self,num1,num2) ) 
                
            elif choice == "/":
                num2 = int (input("Enter Num2: "))
                while num2 == 0:
                        num2 = int (input("PLease Enter Valid Num "))
                
                print(num1 ,"/", num2, "=",Calc.Div(self,num1,num2) )
                
            elif choice == "%":
                
                num2 = int (input("Enter Num2: ")) 
                print(num1 ,"%", num2, "=",Calc.Div_Remen(self,num1,num2) ) 
                
            elif choice == "^":
                
                num2 = int (input("Enter Num2: ")) 
                print(num1 ,"^", num2, "=",Calc.Power(self,num1,num2) ) 
                
            elif choice == "sqart":

                print("sqart(",num1 ,") =",Calc.Sqart(self,num1) ) 
                
            elif choice == "log":
 
                print("log(",num1 ,") =",Calc.Log(self,num1) ) 
                
            elif choice == "sin":
   
                print("sin(",num1 ,") =",Calc.Sin(self,num1) ) 
                
            elif choice == "cos":
   
                print("cos(",num1 ,") =",Calc.Cos(self,num1) ) 
                
            elif choice == "tan":
   
                print("tan(",num1 ,") =",Calc.Tan(self,num1) )  
                              
            elif choice == "<<":
                
                num2 = int (input("Enter Num2: ")) 
                print(num1 ,"<<", num2, "=",Calc.Shift_Left(self,num1,num2) )              

            elif choice == ">>":
                
                num2 = int (input("Enter Num2: ")) 
                print(num1 ,">>", num2, "=",Calc.Shift_Right(self,num1,num2) ) 
                                
            calculate = input("If you want to exit press 0: ")
            if calculate == "0":
                print ("Thank you")
                break
                    
          
ope =Calc
ope.Options(0)
    
    
        
        
