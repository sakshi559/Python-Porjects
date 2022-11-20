Phrase=input("Enter a phrase : ")
text=Phrase.split()
a=""
for i in text:
    a=a+str(i[0].upper())

print(a)