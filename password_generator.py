import random

length=int(input("Enter the length of password:"))
ss=input("do you want special symbols in your password(yes/no):")
Num=input("Do you want numbers in your password(yes/no):")
ran=int(input("Also enter the range of your number in Password:"))
password=""
i=1

def letters():
    LETTER = ""
    letters=random.randint(65,91)
    Letter=chr(letters)
    LETTER=LETTER+Letter
    return LETTER

def special():
    Special=""
    numbers = [36, 64, 95]
    symbols = random.choice(numbers)
    special = chr(symbols)
    Special=Special+special
    return Special

def numbers():
    numb=random.randint(1,ran)
    return numb


while i<length:
    letter=letters()
    password=password+letter
    if ss.lower()=="yes":
        SPECIAL=special()
        password=password+ str(SPECIAL)
        i+=1
    if Num.lower()=="yes":
        number=numbers()
        password = password + str(number)
        i+=1

    i+=1


print(password)
print(len(password))


