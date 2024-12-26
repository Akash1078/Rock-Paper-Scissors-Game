
#--------------( Game :- Rock, Paper, Scrissors )-------------------------------------------------------------
import random

computer = random.choice([-1,0,1])
User_String = (input("Enter You Choice:")).lower()
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

print("Your Choies : " + Rev_Dictionary[You]+"\n Computer Choies : " + Rev_Dictionary[computer])
