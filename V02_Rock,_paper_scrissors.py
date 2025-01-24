'''Here I Update_0.2 The Game In In terms of ( user experience )'''

#-----------------------( User And Password Login_System )------------------------------------------------------
print()
user = " "
while user !="RahuL""Akash""Rakesh1":
    user = input("Please Enter Your User Name :")
    if(user=="RahuL" or user=="Akash" or user =="Rakesh1"):
        break
    else:
        print(f"\"Wrong User Name\"\n")

password =" "

while password != "Rahul@123""Rakesh@1967":
    password = input(f"Enter your Password {user} :")
    if(password=="Rahul@123" or password =="Rakesh@1967" or password =="Akash@123"):
        print()
        print("\tAccess Granted !")
        break
    else:
        print("Wrong Password")

#---------------( Game :- Rock, Paper, Scrissors )-------------------------------------------------------------
while True :
    print(f"\t{user} Welcome To Your \"Rock, Paper, Scrissors game\"")
    print()
    import random
    computer = random.choice([-1,0,1])
    User_String= " "
    while User_String != "r""p""s":
        User_String = (input(f"\"You Have Only One CHOICE\" \n Press Only One button and Choose -- ( R , P , S ) \n\n\tR = Rock, P = Paper, S = Scrissors. \n \n \"Enter You Choice\":")).lower()
        if User_String == "r" or User_String == "p" or User_String == "s":
            break

    print()
    Your_Dictionary={"r":-1,"p":0,"s":1}
    Rev_Dictionary ={-1:"Rock",0:"Paper",1:"Scrissor"}

    You = (Your_Dictionary[User_String])

    if (computer==You):
        print("Its a Draw")
    #------(You Win Code )------------{"r":-1,"p":0,"s":1}

    elif(computer==-1 and You== 0):
        print("You WIN !") # OK

    elif(computer==0 and You== 1):
        print("You WIN !") # OK

    elif(computer==1 and You== -1):
        print("You WIN !")
    #------(You lose Code )------------{"r":-1,"p":0,"s":1}
    elif(computer==0 and You== -1):
        print("You LOSE !")
    elif(computer==1 and You== 0):
        print("You LOSE !")
    elif(computer==-1 and You== 1):
        print("You LOSE !")

    print()
    print("Your Choies : " + Rev_Dictionary[You]+"\n Computer Choies : " + Rev_Dictionary[computer]+"\n\tGive an another try !")
    Last_User = input("Yes / No : ").lower()
    if Last_User != "yes":
        break
print("Thanks For Playing")