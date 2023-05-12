import sys

class Calc():
    def __init__(self,total =0,res =0):
        self.total = total
        self.res = res
        
                
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
    
    def Clear(self):
        self.total =0
   
		
    def Options(self):
        calculate = "1"
        while calculate != "0":
            num1 = int (input("PLease Enter Num1: "))
            try:
                choice = input("Choose the operator: +,-,*,/,%,^: ")
                
            except:
                print("Please choose +,-,*,/,%,^")
            else:  
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
                    print(num1 ,"/", num2, "=",Calc.Div(self,num1,num2) )
                    
                elif choice == "%":
                  
                    num2 = int (input("Enter Num2: ")) 
                    print(num1 ,"%", num2, "=",Calc.Div_Remen(self,num1,num2) ) 
                    
                elif choice == "^":
                    
                    num2 = int (input("Enter Num2: ")) 
                    print(num1 ,"^", num2, "=",Calc.Power(self,num1,num2) ) 
                    
                calculate = input("If you want to exit press 0: ")
                if calculate == "0":
                    break
                    

              
ope =Calc
ope.Options(0)
    
    
        
        
