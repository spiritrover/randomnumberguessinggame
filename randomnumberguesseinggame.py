import random

chanceofsucsess = 3
credits = 225
addingcredits = 1

credits = credits + addingcredits

def openwrite_close(score):
    x = str(score)
    f = open("Scoreforrandomnumberguessinggame", "w")
    f.write(x)
    f.close() 

def askforpersonalrisk():
    global chanceofsucsess
    global addingcredits
    riskfactor = input("please state risk factor:low, mid, high:\n")
    if riskfactor == "low":
        addingcredits = 1
        chanceofsucsess = int(3)
    if riskfactor == "mid":
        addingcredits = 5
        chanceofsucsess = int(6)
    if riskfactor == "high":
        addingcredits = 20    
        chanceofsucsess = int(10)
    return(chanceofsucsess)
         

def game():
    score = 0
    moves = 0
    global chanceofsucsess 
    print("please enter your guess here between 1 and ", chanceofsucsess)
    guess = int(input())
    
    
    while True:

        global credits
        randomnumber = random.randint(1, chanceofsucsess)   

        if int(guess) == randomnumber:

            score = score+10
            openwrite_close(score)
            

        else:
      
            score = score-1
            openwrite_close(score)
                 


        if score > 250:
            print("You Win! Moves:",moves, "last score:", score)
            credits = credits + 5
            return()

        moves = moves +1

        if moves > 1000:
            print("You Lose :(, moves:",moves, "last score", score)
            credits = credits - 1 
            return()

while True:
    if credits >= 1:
        print("remaining credit:", int(credits))
        askforpersonalrisk()
        game()
    else:
        print("remaining credit:",int(credits)) 
        exit()
        
#LOCAL ANARCHIST TEAMS UP WITH HOMELESS TELETUBBY TO DESTROY GOVERNMENT - Technoblade