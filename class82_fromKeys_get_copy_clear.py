# from keys
# d = {"name" : "unknown" , "age" :"unknown"}

d = dict.fromkeys(("name","age","HEIGHT"),"unknown")
print(d)


d = dict.fromkeys("Abc" ,"unknown")
print(d)

d = dict.fromkeys(range(1,11),"unknown")
print(d)

#### get method (useful)
d = {"name":"Ashwani" , "age":"19"}
# print(d["name"])
print(d.get("name"))
print(d.get("lover"))


if d.get("name"):
    print("present")
else:
    print("not presnt")


##  clear method
# 
d.clear()
print(d)

# copy method
d1 = d.copy()
# d1 = d
print(d1)