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
    messagebox.showinfo("Title", "\nHello, you have the option of being one " + \
                        "of three characters as you pull off a heist. You can " + \
                        "be Carmine (the leader), " + \
                        "Ivan (the muscle), or Houstan (the brains).")
    choice = simpledialog.askstring("Choose wisely",
                                   "Type 'Ivan', 'Houstan', or 'Carmine'.")
    choice = choice.lower()
    if choice == "ivan":
        choice1()
    elif choice == "houstan":
        choice2()
    elif choice == "carmine":
        choice3()
    else:
        intro()

################ Ryan Rueber Functions #####################
def choice1():
    messagebox.showinfo
    choice = simpledialog.askinteger("IVAN",
                                     "You have chosen Ivan to be your character. As you approach " + \
                                     "the bank Ivan must either knock out or kill the gaurds " + \
                                     "in order to safely get into the bank. (Type '1' to knock out the gaurds " + \
                                     "or type '2' to kill the guards.")
    if (choice == 1):
        def ko():
            choice = simpledialog.askinteger("Choose wisely",
                                             "You have elected to knock out the guards. " + \
                                             "would you like to 

    elif (choice == 2):
        messagebox.showinfo("The End",
                            "You chose ok.  THE END")
    else:
        choice1()

################ Chris Renslow Functions #####################
                                             



def choice2():
    choice = simpledialog.askinteger("CARMINE",
                                     "You chose the leader of the team, Carmine. He will command and make all the major choices in the heist."+ \
                                     "Will you go in stealthily or go in the front door? 1 for stealth 2 for guns blazing. ")
    if (choice == 1):
        messagebox.showinfo("Stealth",
                            "You decide to go in stealthy.")

    elif (choice == 2):
        messagebox.showinfo("Loud",
                            "You decide to go in the front door.")
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
                            "you are now the only one able to see what goes on inside.")
        choice31()
                            

    elif (choice == 2):
        messagebox.showinfo("HOUSTON",
                            "Your choice may prove unwise but all you can think of is money.")
        choice32()
    else:
        choice2()

def choice31():
    choice = simpledialog.askinterger("

################ Main #####################
intro()

root.destroy()
