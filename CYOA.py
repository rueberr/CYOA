# Choose.py
# by Ryan Rueber, Chris Renslow, and Stetson Jones
# Description: An adventure about a heist.


# Import Statements
from tkinter import *
import tkinter.simpledialog
import tkinter.messagebox

root = Tk()
w = Label(root, text="Choose Your Own Adventure")
w.pack()

def intro():
    """ Introductory Function -> starts the story going """
    messagebox.showinfo("Title", "\nHello, you are a _____ from ____. " + \
                        "You stumble across such and such.")
    choice = simpledialog.askinteger("Choose wisely",
                                   "You have a choice to pick: 1 or 2.")
    if choice == 1:
        choice1()
    elif choice == 2:
        choice2()
    else:
        intro()

################ Ryan Rueber Functions #####################
def choice1():
    choice = simpledialog.askinteger("Choose wisely",
                                     "This is the next part of the story.  Now you must choose 1 or 2 again.")
    if (choice == 1):
        messagebox.showinfo("The End",
                            "You chose right.  THE END")

    elif (choice == 2):
        messagebox.showinfo("The End",
                            "You chose ok.  THE END")
    else:
        choice1()

################ Chris Renslow Functions #####################
def choice2():
    choice = simpledialog.askinteger("Choose wisely",
                                     "This is the next part of the story.  Now you must choose 1 or 2 again.")
    if (choice == 1):
        messagebox.showinfo("The End",
                            "You chose right.  THE END")

    elif (choice == 2):
        messagebox.showinfo("The End",
                            "You chose ok.  THE END")
    else:
        choice2()
        
################ Stetson Jones Functions #####################
def choice3():
    choice = simpledialog.askinteger("You have chosen HOUSTON", 
                                     "HOUSTON is the brains of the operation.",
                                     "The entire heist rides on you.",
                                     "Now for your first choice.",
                                     "Turn the cameras off and lose some of the money,",
                                     "Or let the feds watch as you take the money.",
                                     "Type 1 to turn off cameras, or 2 to let them watch")
    
    if (choice == 1):
        messagebox.showinfo("HOUSTON",
                            "You take control of the cameras.",
                            "you are now the only one able to see what goes on inside.",
                            

    elif (choice == 2):
        messagebox.showinfo("HOUSTON",
                            "Your choice may prove unwise but all you can think of is money.")
    else:
        choice2()

################ Main #####################
intro()

root.destroy()
