import random


def game(comp,you):
    if(you=="s"):
        if(comp=="p"):
            return False
        elif(comp=="sc"):
            return True
        else:
            return None
    elif(you=="p"):
        if(comp=="s"):
            return True
        elif(comp=="sc"):
            return False
        else:
            return None
    elif(you=="sc"):
        if(comp=="s"):
            return False
        elif(comp=="p"):
            return True
        else:
            return None
    else:
        print("You take wrong input, try it again :)")

comp=random.randint(1,3)
if(comp==1):
    comp="s"
elif(comp==2):
    comp="p"
else:
    comp="sc"

you=input("Choose stone(s) or paper(p) or scissors(sc) to play: ")

print(f"you take {you} and computer takes {comp}")


a=game(comp,you)
if(a==True):
    print("You won the game")
elif(a==False):
    print("You loss the game, better luck next time")
elif(a==None):
    print("Match draw")
