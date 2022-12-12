# define a function which will take list as a argument and this function will return a reversed list 

# examples
#   [1,2,3,4] ----> [4,3,2,1]
# ['word1' , 'word2'] ----> ['word1' , 'word2']

# Note you simply do this with reverse method or  [::1]

# but try to do this with the help of append and  pop method




'''Method 1'''
# def reverse_list(l):
#     l.reverse()
#     return l
# num = [1,2,3,4,5]    
# print(reverse_list(num))


'''Method 2'''
def rev_list(l):
    return l[::-1]
num = list(range(1,7))    
print(rev_list(num))


'''now we use append and pop method'''
def reverse_list(l):
    r_list = []
    for i in range(len(l)):
        popped_item = l.pop()
        r_list.append(popped_item)
    return r_list

num = [1,2,3,4]        
print(reverse_list(num))


