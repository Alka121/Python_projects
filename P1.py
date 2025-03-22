import random
target = random.randint(1, 100)

while True:
    userChoice = input("Guess the target Or Quit(Q):")
    if(userChoice == "Q"):
        break
    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success : Coreect Guess!!")
        break
    elif(userChoice < target):
        print("Your number was too small,Take a Bigger Guess!!")
    else:
        print("Your number was too big,Take a Lesser Guess!!")
print("----------------Game is over!!---------")
    
