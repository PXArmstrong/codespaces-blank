i=1
print("Welcome to the food order service menu")
name=input("What is your name? ")
Birthday=int(input("Please enter your birthyear: "))
#Gathers information from the user
age=2025-Birthday
#Calculates the Age based off of birthday
options=["placeholder1","placeholder2","placeholder3","exit"]
for word in options:
    print(str(i)+"."+word)
    i+=1
userinp= input("Please enter the number of your choice ")
if userinp==4:
    exit()
#List Printer and Exit selection