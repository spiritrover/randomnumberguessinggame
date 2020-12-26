import random

score = 0

moves = 0

guess = input("please enter your guess here:\n")

def openwrite_close(score):
    x = str(score)
    f = open("Scoreforrandomnumberguessinggame", "w")
    f.write(x)
    f.close() 


while True:

    randomnumber = random.randint(1, 6)   

    if int(guess) == randomnumber:

        score = score+6
        openwrite_close(score)

    else:
      
        score = score-1
        openwrite_close(score)      


    if score > 250:
        print("You Win! Moves:",moves, "last score:", score)
        exit()

    moves = moves +1

    if moves > 1000:
        print("You Lose :(, moves:",moves, "last score", score)
        exit()


