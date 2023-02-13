# The game is all about asking the user a bunch of questions, if the right answer for the question is given, we add one to their score. At end of the program, we print out what they have got from the number of questions.

print("Welcome to my computer quiz game")
print("Let's see how well you know your computer abbreviations!  ")
playing = input("Do you want to play? ")
if playing.lower() != "yes":
    print("Thanks for checking up")
    quit()
else:
    print("Okay, Let's play! 💃")
score = 0

question = input("What does API stand for? ")
if question.lower() == "application programming interface":
    print("Correct! 👌")
    score += 2
else:
    print("Incorrect! 😒")

question = input("What does ASCII stand for? ")
if question.lower() == "american standard code for information interchange":
    print("Correct! 👌")
    score += 2
else:
    print("Incorrect! 😒")

question = input("What does BT stand for? ")
if question.lower() == "bittorrent" or question.lower() == "bluetooth":
    print("Correct! 👌")
    score += 1
else:
    print("Incorrect! 😒")

question = input("What does BAL stand for? ")
if question.lower() == "basic assembly language":
    print("Correct! 👌")
    score += 1
else:
    print("Incorrect! 😒")

question = input("What does CLI stand for? ")
if question.lower() == "command line interface":
    print("Correct! 👌")
    score += 1
else:
    print("Incorrect! 😒")

question = input("What does DBMS stand for? ")
if question.lower() == "database management system":
    print("Correct! 👌")
    score += 1
else:
    print("Incorrect! 😒")

question = input("What does DMS stand for? ")
if question.lower() == "direct memory access":
    print("Correct! 👌")
    score += 1
else:
    print("Incorrect! 😒")

question = input("What does EOF stand for? ")
if question.lower() == "end of file":
    print("Correct! 👌")
    score += 1
else:
    print("Incorrect! 😒")

question = input("What does FIFO stand for? ")
if question.lower() == "first in first out":
    print("Correct! 👌")
    score += 1
else:
    print("Incorrect! 😒")

question = input("What does GPRS stand for? ")
if question.lower() == "general packet radio service":
    print("Correct! 👌")
    score += 1
else:
    print("Incorrect! 😒")

print("Thanks for playing!")
print("You got " + str(score) + " questions correctly")
print("You total score = " + str((score / 10) * 100) + "% ")
print("Thanks for playing")




