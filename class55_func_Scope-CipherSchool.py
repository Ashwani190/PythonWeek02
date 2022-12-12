# scope  -- > local and global
x = 99 #Global variable
def funct():
    x = 7 # local variable ---- kyunkyi ye sirf function kk ander work krega
    return x

print(x) ## if directyly run ,then we got "x" is not defined ,because x kiii value to function mm hh , too ye bhrr permission nhi dega ,,we can do print using def or iske liye x kk liye hhh global kaa use krenge
print(funct())
print(x)

