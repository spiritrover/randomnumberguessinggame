from tkinter import *
import tkinter


window = Tk()
window.title("stupid programm")
window.geometry("1920x1080")

self_v1 = IntVar()

def onclickbtn1():
    print('easy mode', enterguess.get())  

def onclickbtn2():
    print('mid mode', enterguess.get())

def onclickbtn3():
    print('hard mode', enterguess.get())

def getenteredguess(event):
    print(enterguess.get())

def PlayAgain():
    print('i would like to play again')

#risk settings (buttons 1 - 3)
btn1 = Radiobutton(window, text = "low risk", height=20, width= 50,variable=self_v1, command=onclickbtn1, activebackground='#47FF00', tristatevalue= False)
btn1.place(x=200, y=40)

btn2 = Radiobutton(window, text = "mid risk", height=20, width= 50,variable=self_v1, command=onclickbtn2, activebackground='#47FF00', tristatevalue= False)
btn2.place(x=750, y=40)

btn3 = Radiobutton(window, text = "high risk", height=20, width= 50,variable=self_v1, command=onclickbtn3, activebackground='#47FF00', tristatevalue= False)
btn3.place(x=1350, y=40)

#play again with selected settings (button 4)
btn4 = Button(window, text = 'Play Again', height= 10, width= 75, command=PlayAgain)
btn4.place(x= 675, y=900)

enterguess = Entry(window, width= 25)
enterguess.place(x=850, y=500, height=45)
enterguess.bind("<Return>", getenteredguess)


#labels
l1 = Label(window, text= '----------------------------------------------------------------------------------------------------------------------------------------Enter Guess Here----------------------------------------------------------------------------------------------------------------------------------------')
l1.place(x= 200, y= 425)

l2 = Label(window, text= '----------------------------------------------------------------------------------------------------------------------------------------State Risk Level Here----------------------------------------------------------------------------------------------------------------------------------------')
l2.place(x= 200, y=20)

l3 = Label(window, text= 'remainingcredits:')
l3.place(x= 20,y= 20)

l4 = Label(window, text= 'moves:')
l4.place(x= 600, y=750 )

l5 = Label(window, text= 'gameresult:')
l5.place(x= 600,y= 700)


btn1.place()
btn2.place()
btn3.place()
enterguess.place()

window.mainloop()


