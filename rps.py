import random

def result(user, user1):
    if user=='rock' and user1=='scissor':
        print("You  Won!!!!!!!")
    elif user=='paper' and user1=='scissor':
        print(f"{player2} Won!!!!!!!!!")
    elif user=='rock' and user1=='paper':
        print(f"{player2} Won!!!!!!!!!!!")
    elif user=='paper' and user1=='rock':
        print("You Won !!!!!!")
    elif user=='scissor' and user1=='rock':
        print(f"{player2} Won !!!!!")
    elif user=='scissor' and user1=='paper':
        print("You Won!!!!!!")
    else:
        print("Tie!!!!!!")


rps=['rock','paper','scissor']
User_name=input("Enter your name:")
play_mode=input("Whom you want to paly with (AI/FRIEND):")
user=input(f"{User_name} enter your choice(rock/paper/scissor):")
if play_mode.upper()=="AI":
    player2="AI"
    computer=random.choice(rps)
    print("AI choosed : " ,computer)
    result(user,computer)

if play_mode.upper()=="FRIEND":
    player2=input("Enter you name player2:")
    friend=input(f"{player2} enter you choice(rock/paper/scissor):")
    print(f"{player2} choosed",friend)
    result(user,friend)