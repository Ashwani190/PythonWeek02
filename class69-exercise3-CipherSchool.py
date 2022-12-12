

# filter odd even
# define a function
# input
# list  ---- >  [1,2,3,4,5,6,7]

# output ---> [[1,3,5,7] , [2,4,6]]

def filter(n):
    odd_nums = []
    even_nums = []
    for i in n:
        if i%2==0:
            even_nums.append(i)
        else:
            odd_nums.append(i)
    output = [odd_nums,even_nums]     
    return output   
num = list(range(1,8))                 
print(filter(num))











