# in keyword and iterations in dictionary 

user_info = {
    'name' : 'Ashwani' ,
    'age' : 19 ,
    "fav movies" : "END GAME"
}

# check if key exist in dictionary 
if "name" in user_info:
    print("present")
else:
    print("not present")
   
# check if value exist in dictionary


'''***wrong method**''' 
if "Ashwani" in user_info: 
    print("present")
else:
    print("not present")    


'''correct method'''
if "Ashwani" in user_info.values():
    print("present")
else:
    print("not presnt")    


## loop in dictionaries
user_info = {
    'name' : 'Ashwani' ,
    'age' : 19 ,
    "fav movies" : "END GAME"
}
for i in user_info:
    print(i)



user_info = {
    'name' : 'Ashwani' ,
    'age' : 19 ,
    "fav movies" : "END GAME"
}
for i in user_info.values():
    print(i)
    
'''or another method to print the values of keys '''
user_info = {
    'name' : 'Ashwani' ,
    'age' : 19 ,
    "fav movies" : "END GAME"
}
for i in user_info:
    print(user_info[i])  


# items method
user_items = user_info.info()
print(user_info)
print(type(user_info))




'''why item method is good,for loop'''

user_info = {
    'name' : 'Ashwani' ,
    'age' : 19 ,
    "fav movies" : "END GAME"
}
for key , value in user_info.items():
    print(key,":",value)
    
