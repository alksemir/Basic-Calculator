number1=int(input("Enter a number1: "))
number2=int(input("Enter a number2: "))
operation=input("'+', '-', '*', '/' ")
def sumup(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multipy(a,b):
    return a*b
def divide(a,b):
    return a/b
def calculate(number1,number2,choose):
    if(operation=='+'):
        return sumup(number1,number2)
    elif(operation=='-'):
        return subtract(number1,number2)
    elif(operation=='*'):
        return multipy(number1,number2)
    elif(operation=='/'):
        return divide(number1,number2)
    else:
         print("Please enter valid arguments")
print(calculate(number1,number2,operation))