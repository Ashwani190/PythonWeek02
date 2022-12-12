# dictionary intro
# Q  - why we use dictionaries ?
# A  - Because of limitation of lists  , lists are not enough to represent 
# real data

#Example 
user = ["ashwani" , "19" , ["mcv" , "moonknight"],["aawakeneing","white arrow"]]
# this list contains user name , age , fav movies , fav tunes
# you can do this but this is not a good way to do this.
# 


#   Q -> what are dictionaries
#  A  --> unordered collections of data in key : value pair



# how to create dictionary
user = {'name' : 'Ashwani' , 
        'age' : 19}
print(user)

# second method to create dictionaries
user1 = dict(name = "ASHWANI YADAV" ,age  = 19)
print(user1)        

# dictionary mm indexing nhi hoti ,,we take the help of key
print(user1["name"])



## Q -> which type of data can store ?
# ans --> anything
# number ,string ,list , dict

user_info = {
    "name":"ashwani",
    "age" : 19 ,
    "fav_movies": "moonknight"
}
print(user_info["fav_movies"])

### vacant dictionary ..how to store data 
user_info2 = {}
user_info2["name"] = "man-mohan"
user_info2["song"] = "yrr ni miliya"
print(user_info2)