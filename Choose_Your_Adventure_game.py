name = input("Enter you name: ")
print("Welcome", name, "to the game of adventure!")

answer = input("You are on a cross road, you can chose to go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You've come to a river, "
                     "you can walk around it or swim across. Type walk to walk around or swim to swim across: ").lower()
    if answer == "swim":
        answer = input("You are getting drown as the river is too deep for you to swim across. "
                         "Do you want to ask for help or not? "
                         "Type help to ask for help or No to continue swimming: ") .lower()
        if answer == "help":
            print("You've been rescued, you lose! ")
        elif answer == "no":
            print("You got drawn and lost the game")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game")
    else:
        print("Not a valid option. You lose")

elif answer == 'right':
    answer = input("You've come to a bridge, it looks wobbly, do you want to cross it or head back? (cross/back) ")
    if answer == "back":
        print("You went back and lost the game")
    elif answer == "cross":
        answer = input("You crossed the bridge and met a stranger trapped on the bridge."
                             " Do you help him or not? (yes/no): ")
        if answer == "yes":
            answer = input("You got trapped also while trying to help the stranger. "
                               "Would you call for help or keep struggling? (help/no) ")
            if answer == "help":
                print("You asked for help and was rescued! You lose")
            elif answer == "no":
                print("You were able to free yourself and the stranger, You win!")

        elif answer == "no":
            print("You ignored the stranger and loose")
        else:
            print("Not a valid option. You lose")
else:
    print("Not a valid option. You lose")

print('Thank you for playing', name + "!")
