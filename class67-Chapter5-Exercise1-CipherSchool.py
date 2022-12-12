# define a function which will take list containing numbers as input  and return list containing square of every elements 

# example
# numbers = [1,2,3,4]                                                                                                        
# square_list(numbers) ----- > return ---->[1,2,9,16]

def square_list(l):
    square = []
    for i in l:
        square.append(i**2)
    return square
number = list(range(1,5))    
print(square_list(number))




def list_sqrt(l):
    sqrt = []
    for i in l:
        sqrt.append(i**2)
    return sqrt 
num = list(range(1,8))
print(list_sqrt(num))       















 
