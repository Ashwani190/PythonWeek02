# Define is_palindrome function that take one word in string as input 
# and return True if it is palindrome else return False
# 
# palindrome - word that reads same baackwards as forward

# example 
# is_palindrome("madam") -----> True  
# is_palindrome("naman")------> True 
# is_palindrome("horse")-------> False

def is_palindrome(str):
    if str==str[::-1]:   # str[0:] == str[::-1]
        return "Yes, it is palindrome"
    else:
        return "No its not palindrome"
word = input("")
print(is_palindrome(word))          





