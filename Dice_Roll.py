import random

username=input("Enter your name:")
agreement=input("Do you want play dice roll(yes/no):")
if agreement.lower()!="yes":
    print("oops!! seems like you don't want to play")
    quit()

dice_roll=random.randint(1,7)
print(f"You got {dice_roll}")
