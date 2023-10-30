from ast import main
import os
from sre_constants import SUCCESS
import sys
import math
from math import factorial
from math import tan
from timeit import repeat
zanovo = True
while zanovo:
                print("vvedite pervoe chislo");
                num1 = (input());
                try:
                    num1 = float(num1)
                        
                except ValueError:
                    try:
                        num1 = int(num1)
                        
                        
                    except ValueError:
                        print("This is not a number")
                        break
                        
                        
                        
                        
            
            
                print("vvedite vtoroe chislo");
                num2 = (input());
                try:
                    num2 = float(num2)
                        
                except ValueError:
                    try:
                        num2 = int(num2)
                        
                        
                    except ValueError:
                        print("This is not a number")
                        break
                print("vuberite operaciy:");
                print("+");
                print("-");
                print("*");
                print("**");
                print("/");
                print("sin");
                print("cos");
                print("tan");
                print("factorial");
                operation = input();
                if operation == "+":
                    print(num1 + num2);
                if operation == "-":
                    print(num1 - num2);
                if operation == "/" and num2 != 0:
                    print(num1 / num2);
                if num2 == 0:
                    print("nelzya na nol delit");
                if operation == "*":
                    print(num1 * num2);
                if operation == "**":
                    print(num1 ** num2); 
                if operation == "sqrt":
                    print(math. sqrt (num1),"   ",math. sqrt (num2));
                if operation == "factorial":
                    print(factorial(int(num1)) , " and ", factorial(int(num2)));
                if operation == "sin":
                    print(math.tan (int(num1)), " and ", math.tan (int(num2)));
                if operation == "cos":
                    print(math.cos (int(num1)), " and ", math.cos (int(num2)));
                if operation == "tan":
                    print(math.tan (int(num1)), " and ", math.tan (int(num2)));
                
                if operation != "+" :
                     if operation != "-":
                        if operation != "*" :
                            if operation != "**":
                                 if operation !=  "/" :
                                      if operation != "cos" :   
                                        if operation != "sin" :
                                            if operation != "tan":
                                                if operation != "factorial":
                                                    print("  ")    
                                                    print("nepravilnuy ili ne sushestvuihyi operator")

                print("  ")
                
                
                restart = input("Do you want to CALCULATE again?(no or yes): ")
                if restart == "no":
                
                    zanovo = False
                if restart == "yes":
                    zanovo == True
                else:
                    break



