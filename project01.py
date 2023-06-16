import random

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 'st':
        if you == 'sc':
            return False
        elif you == 'p':
            return True
    elif comp =='sc':
        if you == 'p':
            return False
        elif you == 'st':
            return True
    elif comp == 'p':
        if you == 'st':
            return False
        elif you == 'sc':
            return True
    
        
            
        

print("Comp Trun: Stone(st) Paper(p) or Scissor(sc)?")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 'st'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 'sc'
    
you = input("Your Turn: Stone(st) Paper(p) or Scissor(sc)?")
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")
 
            
            


