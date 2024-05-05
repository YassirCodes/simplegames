import random

print("How many rounds do you want to have in the game? (Please choose between 1 to 5) or (enter 0 to exit the game)")
flag = True
compwin=0
humanwin=0
while True:
    numofgames = int(input())
    if numofgames==0:
        print("Game exited")
        break
    if numofgames>5 or numofgames<1:
        print("You chose invalid number of rounds,Please choose between 1 to 5")
        continue
    round=0
    while True:
        print("Enter 'r' for rock , 's' for scissors and 'p' for paper or enter 0 to exit the game" )
        values = ['r','s','p']
        userinp = input()
        if userinp=='0':
            print("Game exited")
            flag=False
        if userinp not in values and flag==True:
            print("You chose invalid character")
            continue
        if numofgames==round or flag==False:
            break
        print("round "+str(round+1))
        if(random.choice(values)==userinp):
            print("You won this round!")
            humanwin+=1
        else:
            print("Computer won this round!")
            compwin+=1
        round+=1
    break
print("Computer won "+str(compwin)+" games")
print("Human won "+str(humanwin)+" games")