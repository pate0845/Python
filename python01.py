import random

def game_result(comp,you):
    if comp==you:
        return None

    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
             return True

    elif  comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True

    elif  comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True

comp=print("comp choose Gun(g), Snake(s) or Water(w)?")
randomnum=random.randint(1,3)
if randomnum==1:
    comp='g'
elif randomnum==2:
    comp='s'
elif randomnum==3:
    comp='w'

you=input(print("comp choose Gun(g), Snake(s) or Water(w)?"))

a=game_result(comp,you)
print(f"Computer choose {comp}")
print(f"You choose {you}")

if a==None:
    print("The game is a tie")
elif  a:
    print("You Win!")
else:
    print("You Lose!")        


