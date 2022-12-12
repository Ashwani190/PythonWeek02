# practice for loop 
# ask user name and count each character 
# "Ashwani Yadav"
# A : 1
# s : 1
# h : 2
# w : 2
# n : 1
# i : 1
#   : 1
# y : 1
# d : 1
# v : 1
name = input("")
temp = ""
for i in range(0,len(name)):
    if name[i] not in temp:
        print(name[i] ,"=",name.count(name[i]))
        temp += name[i]


