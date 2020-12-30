import random
credits = 225

def openwrite_close(score):
    x = str(score)
    f = open("Scoreforrandomnumberguessinggame", "w")
    f.write(x)
    f.close() 


def game():
    guess = int(input("please enter your guess here:\n"))
    score = 0
    moves = 0
    
    while True:

        global credits
        randomnumber = random.randint(1, 10)   

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
        game()
    else:
        print("remaining credit:",int(credits)) 
        exit()
        
               