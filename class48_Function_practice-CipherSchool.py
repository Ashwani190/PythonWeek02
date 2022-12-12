### example 1
# def last_char(name):
#     print(name[-1])
# name=input("Enter your name : ")    
# last_char(name)

### another method /// pure method

# a= input("Enter your name : ")
# def last_chr(a):
#     return a[-1]
# print(last_chr(a))    

## 
# name= input("Enter your name : ")
# def last_chr(a):
#     return name[-1]
# print(last_chr(name))  


### example 2nd
# def odd_even(num):
#     if num%2==0 :
#         return "even"
#     else:
#         return "odd"
# print(odd_even(12))        
# print(odd_even(21))
# print(odd_even(18))

'''we can define this function in small way'''
# def odd_even(num):
#     if num%2==0 :
#         return "even"
#     return "odd"    
# print(odd_even(10))


'''another very small way method'''
def odd_even(num):
    return num%2 == 0 # true 
num = int(input("Enter the number : "))
print(odd_even(num))    

## "if we not give input in the function ,then also we can get the right output,that we want"
def song():
    return "Happy bday song"
print(song()) 


