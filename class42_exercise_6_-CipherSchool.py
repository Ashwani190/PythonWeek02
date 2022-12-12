# make a  game in which you input number randomly from 0 to 100 , at last it give the specs of each u enter


winning_number = 43
guess = 1 
num = int(input("guess a number between 0 to 100  : "))
game_over = False

while  not game_over :
    if num == winning_number:
        print(f"you win, and you guessed this number in {guess} times")
    else:
        if num < winning_number :
            print("too low")
            guess += 1
            num = int(input("guess again"))
        else :
            print("too high ") 
            guess += 1
            num = input("guess again")         


