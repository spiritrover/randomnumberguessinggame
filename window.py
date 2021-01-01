from tkinter import *
import tkinter


window = Tk()
window.title("stupid programm")
window.geometry("1920x1080")


def onclickbtn1():
    print('easy mode', enterguess.get())  

def onclickbtn2():
    print('mid mode', enterguess.get())

def onclickbtn3():
    print('hard mode', enterguess.get())

def getenteredguess(event):
    print(event, enterguess.get())



#risk settings (buttons 1 - 3)
btn1 = Button(window, text = "low risk", height=20, width= 50, command=onclickbtn1)
btn1.place(x=200, y=20)

btn2 = Button(window, text = "mid risk", height=20, width= 50, command=onclickbtn2)
btn2.place(x=750, y=20)

btn3 = Button(window, text = "high risk", height=20, width= 50, command=onclickbtn3)
btn3.place(x=1350, y=20)

enterguess = Entry(window, width= 25)
enterguess.place(x=850, y=500)
enterguess.bind("<Return>", getenteredguess)

btn1.place()
btn2.place()
btn3.place()
enterguess.place()

window.mainloop()