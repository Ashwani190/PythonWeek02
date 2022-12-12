## fibonacci series
# 0 1 1 2 3 5 8 13 21 34

# 1 ---> 0
# 2 ----> 0 1 
# 3 ----> 0 1 1

# for i in range(1,11):
#     print(i , end=" ")  ## end se..ye hoga kii jo numbers print honge vo ek line mm hee honge ,,mtlb row me

    # print(i)   /  print(i , end="\n") 
    
def fibonacci(n):
    a = 0 # first number 
    b = 1 # second number
    if n == 1 :
        print(a)
    elif n == 2:
        print(a,b)  # a b  , 0 1

        for n in range(n-2):
            c = a+b     # c = 1  , 2 , 3
            a = b       # a = 1 , 1 ,2
            b = print(b , end=" ")  # b = 1 , 2 , 3
            print(c , end = " ")    
fibonacci(13)            
fibonacci(20)
        

