

fruits = ["grapes" , "apple"]
fruits.append("orange")
print(fruits)



fruits = []
fruits.append("mango")
fruits.append("straw")
fruits.append("pine")
print(fruits)




# more method to add data in our list
fruits1 = ["mango","orange"]
fruits1.insert(1 , "grapes")
fruits1.insert(3 , "straw")
fruits2 = ["1",2,3,34]
print(fruits1+fruits2)



fruits1 = ["mango" , "orange"]
fruits2 = ["grapes" ,"apple"]
fruits1.extend(fruits2)
print(fruits1)
print(fruits2)

fruits1 = ["mango" , "orange"]
fruits2 = ["grapes" ,"apple"]
fruits1.append(fruits2)
print(fruits1)
print(fruits2)