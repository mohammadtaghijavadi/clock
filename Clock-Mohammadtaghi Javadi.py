from tkinter import *
import time

window = Tk()
window.title = ('Digital Clock')
window.geometry = ('600x400')

def myTime():
    hour = time.strftime ('%H')
    minute = time.strftime ('%M')
    second = time.strftime ('%S')
    am_pm = time.strftime ("%p")
    day = time.strftime ("%A")
    zone = time.strftime ("%Z")
    myText = hour + ":" + minute + ":" + second + " " + am_pm
    myText2 = day + ", " + zone

    myLebal.config(text=myText)
    myLebal2.config(text=myText2)
    myLebal.after(1000, myTime)


myLebal = Label(window, text="", font=(
    'Arial', 72), fg='white', bg='green')
myLebal.pack()
myLebal2 = Label(window, text=" ", font=("Arial", 24))
myLebal2.pack()


myTime()

window.mainloop()

