from tkinter import Tk, Entry, END, Button, Label
import os

totalDamage = 0
root = Tk()
root.title("Delayed Damage Tracker")
#root.geometry("400x600")

global damageLabel
damageLabel = Label(root, text=totalDamage)


def button_reset(damageLabel):
    #clear damage counter
    entryField.delete(0, END)
    damageLabel.destroy()

    return

def button_commit():
    try:
        poolDamage = int(entryField.get())
    except:
        poolDamage = 0

    try:
        totalDamage = int(damageLabel.cget("text"))
        damageLabel.destroy()
    except:
        totalDamage = 0

    
    entryField.delete(0, END)

    totalDamage += poolDamage

    global damageLabel
    damageLabel = Label(root, text=totalDamage)
    damageLabel.pack()

#Define fields
entryField = Entry(root, width=10, borderwidth=5)

entryField.pack()


#Define buttons

button_1 = Button(root, text="End Turn", command=button_commit)
button_2 = Button(root, text="Reset", command=button_reset)

#Put buttons on screen

button_1.pack()
button_2.pack()


root.mainloop()
