# generate lists with range functions
# something more about pop method
# index method
# pass Lists to a function

num = list(range(1,11))
# print(num) 
# num.pop(8) 
num.pop()
print(num)

# 1,2,3,4,5,6,7,8,9,10
num = list(range(1,11))
print(num.index(1))


# we can pass a list in function too
num = [1,2,3,4,5,6,7,8,9,10]
def neg_list(l):
    neg = []
    for i in l :
        neg.append(-i)
    return neg    
print(neg_list(num))        










