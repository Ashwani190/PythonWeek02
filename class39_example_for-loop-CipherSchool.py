# practice for loop
# ask user a number like 1259
# calculate sum of digits -----> 1 + 2 + 5 + 9

total = 0
num = input()
for i in range(0,len(num)):
    total += int(num[i])
print(total)    

''' num = "1256" , length = 4
   int(num[0]) ----> 1  
   int(num[1]) ----> 2
   int(num[2]) ----> 5
   int(num[3]) ----> 6 '''
    


