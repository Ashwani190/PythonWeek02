# define a function that takes list of words as argument and return list with reverse of every element in that list

# example
# ['abc' , 'suv' , ,xyx]   -----------> ['cba' , 'vus' , 'zyx']

def rev_list(l):
    elements = []
    for i in l:
        elements.append(i[::-1])
    return elements
words =  ['abc' , 'suv' ,'xyz']     
print(rev_list(words))        



        
   





