from tkinter import Tk, Entry, END, Button, Label
import os

totalDamage = 0


root = Tk()
root.title("Delayed Damage Tracker")
#root.geometry("400x600")

damageLabel = Label(root, text=totalDamage)

def button_reset():
    #clear damage counter
    entryField.delete(0, END)
    root.damageLabel.destroy()

    return

def button_commit():
    try:
        poolDamage = int(entryField.get())
    except:
        poolDamage = 0

    try:
        #save the pending damage then destroy the label
        totalDamage = int(root.damageLabel.cget("text"))
        root.damageLabel.destroy()
    except:
        totalDamage = 0

    
    entryField.delete(0, END)

    totalDamage += poolDamage

    root.damageLabel = Label(root, text=totalDamage)
    root.damageLabel.pack()

#Define fields
entryField = Entry(root, width=10, borderwidth=5)
poolDescription = Label(root, text = "Pending Damage")
damageDescription = Label(root, text = "Total Damage")

#Define buttons

button_1 = Button(root, text="End Turn", command=button_commit)
button_2 = Button(root, text="Reset", command=button_reset)

#display stuff

button_1.pack()
button_2.pack()
entryField.pack()
#damageLabel.pack()


root.mainloop()
