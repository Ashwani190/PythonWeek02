
# string are immutable 
# Lists are mutable
 
s = "string"  # string is never changed , we have to store it somewhere first then we can get changed
t = s.title()
print(t)

l = ["l1" , "l2" , "l3"]
l.pop()
print(l)  # list are mutable