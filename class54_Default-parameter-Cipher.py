# defaut parmeter 

# def user_info(first_name ,last_name , age ):
#     print(f"your first name is {first_name}")
#     print(f"your last name is {last_name}")
#     print(f"your age is {age}")

# user_info('Ashwani' , 'Yadav' , 24)

###############3

def user_info(first_name ,last_name = "Unknown" , age = None ):
    print(f"your first name is {first_name}")
    print(f"dyour last name is {last_name}")
    print(f"your age is {age}")

user_info('Ashwani','Yadav')  ## if we run then our age will come as none 
