'''we will cover below topic in this lecture'''
# looping in tuples
# tuple with one element
# tuple without parenthesis
# tuple unpacking
# list inside tuple
# some functions that you can use with tuples

mixed = (1,2,3,4,5)

# for loop and tuple
for i in mixed:
    print(i)

# while loop
mixed = (1,2,3,4,5)
i = 1
while i<len(mixed):
    print(i)
    i += 1

# tuple with one element
num  = (7,) #if you not put comma , then python wil consider it as a integer
word = ("word",)
print(type(num))
print(type(word))


# tuple without parenthesis
singers = "jazzy B" , "leo gardio" , "Yo yo"
print(type(singers))

# tuple unpacking
singers = ("jazzy B" , "leo gardio" , "Yo yo")
singers1 , singers0 , singers2 = singers
# print(singers0)


mixed2 = (1,2,3,4,5,[6,7,8])
mixed2[5].pop()
print(mixed2) ## so it removes 8







    
