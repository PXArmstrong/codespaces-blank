#This code assumes user has an already pre-existing account with bank, having this chatbot for existing members.
i=1
commonIssue=["Account Issues","Fund Transfering","Card Issues","Other"]
print("Welcome to the First National Bank Banking System")
name=input("What is your name? ")
account_id=str(input("Please enter your Account ID: "))
#Gathers information from the user
if(len(account_id)>7 or len(account_id)<7):
    print("This is not a viable Account ID, please try again");
    exit()
else:
#sees if id is viable
    options=["Open a new Account","Report an Issue","Contact a Human Representative","Exit"]
    for word in options:
        print(str(i)+"."+word)
        i+=1
    userinp= input("Please enter the number of your choice ")
    if userinp=="1" or userinp=="Open Account":
       print("Alright "+name+"! Lets get started, would you like to open a Checking or a Savings Account?")
       accOpen=str(input(""))  
       if(accOpen=="Saving"or accOpen=="Savings" or accOpen=="Savings Account"):
            print("Okay! Now there is one last step. Please provide us with your SSN,ID,or proof of adress and one of our employees will step up your account shortly")
            proof=str(input("Please submit proof of identity:"))
            if proof==proof:
                print("Thank you! Be sure to come back later to check if your accounts been open.")    
                exit()
       elif(accOpen=="Checking" or accOpen=="Check" or accOpen=="Checking Account"):
            print("Okay! Now there is one last step. Please provide us with your SSN,ID,or proof of adress and one of our employees will step up your account shortly")
            proof=str(input("Please submit proof of identity:"))
            if proof==proof:
                print("Thank you! Be sure to come back later to check if your accounts been open.")    
                exit()
    #If user chooses to make an account,Presents option between checking and Savings and then asks for proof of ID to open account.
    if userinp=="2" or userinp=="Check Balances":
        print("What is the issue your facing?")
        issue=str(input("Please describe your problem in detail:"))
        if(issue==issue):
            print("Thank you for reporting this problem, our staff will notify you as soon as fix is solved. Have a good day!")
            exit()
    if userinp=="3" or userinp=="Contact a Human" or "Human" or "Talk to a human":
        i=1
        print("Okay! Before we get you to a human representative, what seems to be the general problem you are having?")
        for problem in commonIssue:
            print(str(i)+"."+problem)
            i+=1
        probleminp=int(input("Please make a selection:"))
        if(probleminp==1):
            print("We will be transfering you to the Account Managment department immediatly. Good Bye!")
            exit()
        if(probleminp==2):
            print("Sending you to the Fund tranference department now, Have a nice day!")
            exit()
        if(probleminp==3):
            print("We will be transferring you to the Card department shortly,Thank you for using the First National Bank Service!")
            exit()
        if(probleminp==4):
            print("We are connecting your to our Customer Service branch to further take a look at your inqueries")
            exit()          
    if userinp=="4" or userinp=="exit" :
        exit()
    #List Printer and Exit selection