## write a program in which you have to bring output of number which is greater ?

def greater(a,b):
    if a > b:
        return a
    else :
        return b
num1 = int(input("Enter your first number: "))            
num2 = int(input("Enter the second number : "))
print("The greater numberr is",greater(num1,num2))