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
    messagebox.showinfo("THE HEIST", "\nHello, you have the option of being one " + \
                        "of three characters as you pull off a heist. You can " + \
                        "be Carmine (the leader), " + \
                        "Ivan (the muscle), or Houston (the brains).")
    choice = simpledialog.askstring("Choose wisely",
                                   "Type 'Ivan', 'Houston', or 'Carmine'.")
    choice = choice.lower()
    if choice == "ivan":
        choice1()
    elif choice == "carmine":
        choice2()
    elif choice == "houston":
        choice3()
    else:
        choice3()

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
                                             "would you like to")

    elif (choice == 2):
        messagebox.showinfo("The End",
                            "You chose ok.  THE END")
    else:
        choice1()

################ Chris Renslow Functions #####################
def choice14():
    choice14 = simpledialog.askinteger( "Roof" ,"Kill the guards or try and sneak past them to the vault on the roof? 1 for kill 2 for sneak")

    if (choice14 == 1):
        messagebox.showinfo("Kill",
                            "You kill the guards but Ivan gets shot, enters rage mode and pushes several guards off a balcony." + \
                            "This alerts the guards and they kill the team. HEIST FAILED")
        intro()
        

    elif (choice14 == 2):
        messagebox.showinfo("Sneak",
                            "You try and sneak past the roof guards and the guards in the bank spot you through the skylights."+ \
                             "They alert the police. HEIST FAILED")
        intro()
    
    
    else:
        choice14()             

        
def choice13():
    choice13 = simpledialog.askinteger( "Basement" ,"Kill the guards or try and sneak past them to the vault in the basement? 1 for kill 2 for sneak")

    if (choice13 == 1):
        messagebox.showinfo("Kill",
                            "You try to quietly kill the guards but the others hear you, and ambush you as you come out of the basement. HEIST FAILED")
        intro()
    elif (choice13 == 2):
        messagebox.showinfo("Sneak",
                            "You easily sneak past the dimwitted guards and head to the Vault")
    
    
    else:
        choice13()             



def choice11():
    choice11 = simpledialog.askinteger("Roof or Basement" ,"You can either go in on the roof of the bank or underground through the basement." + \
                          "1 for roof 2 for basement")
    if (choice11 == 1):
        messagebox.showinfo("Roof",
                            "You go in on the roof and down into the bank")
        choice14()
    elif (choice11 == 2):
        messagebox.showinfo("Basement",
                            "You go underground and through the basement quietly and enter the bank")
        choice13()
    
    
    else:
        choice11()                                          

def choice12():
    choice12 = simpledialog.askinteger("Front Door" , "You go in guns blazing through the front door and make your way to the Vault." + \
                            "Will you drill the Vault or blast the Vault open with explosives? 1 for Drill 2 for blast")
    if (choice12 == 1):
        messagebox.showinfo("Drill",
                            "You try and drill the vault but the drill you brought was to weak for the Vault." + \
                            "You take too long, the cops come and see the dead bodies and kill the team. HEIST FAILED")
        intro()
                                             

    elif (choice12 == 2):
        messagebox.showinfo("Blast",
                            "You blast the Vault. You use to much explosives and Ivan is blown away and killed." + \
                            "Without all of your team you cannot continue" + \
                            "HEIST FAILED")
        intro()
        
    else:
        choice12()

def choice2():
    choice2 = simpledialog.askinteger("CARMINE",
                                     "You chose the leader of the team, Carmine. He will command and make all the major choices in the heist."+ \
                                     "Will you go in stealthily or go in the front door to begin the heist? 1 for stealth 2 for guns blazing. ")
    if (choice2 == 1):
        messagebox.showinfo("Stealth",
                            "You decide to go in stealthy.")
        choice11()                                     

    elif (choice2 == 2):
        messagebox.showinfo("Loud",
                            "You decide to go in the front door.")
        choice12()
    else:
        choice2()
        
################ Stetson Jones Functions #####################
def choice3():
    choice = simpledialog.askinteger("You have chosen HOUSTON", 
                                     "HOUSTON is the brains of the operation."
                                     "The entire heist rides on you."
                                     "Now for your first choice."
                                     "Turn the cameras off and lose some of the money,"
                                     "Or let the feds watch as you take the money."
                                     "Type 1 to turn off cameras, or 2 to let them watch")
    
    if (choice == 1):
        messagebox.showinfo("HOUSTON",
                            "You take control of the cameras."+ \
                            "you are now the only one able to see what goes on inside.")
        choice31()
                            

    elif (choice == 2):
        messagebox.showinfo("HOUSTON",
                            "Your choice may prove unwise but all you can think of is money.")
        choice32()
    else:
        choice2()

def choice31():

    choice = simpledialog.askinterger("")

    choice = simpledialog.askinterger("HOUSTON",
                                      "You turn off the cameras. It was easy... too easy..."+ \
                                      "but now you are faced with a choice. stay in the saftey of the van"+ \
                                      "or risk it and go inside with the team and make sure they get the job done right."+ \
                                      "type 1 to stay, or 2 to go.")
    if (choice == 1):
        messagebox.showinfo("HOUSTON",
                            "You're a bit wimpy, but then again you always have been"+ \
                            "no ammount of therapy could erase the bullying")

    if (choice === 2):
        messagebox.showinfo("HOUSTON",
                            "Youre taking the brave way, this may gain you respect"
                            "with your team, but this is scary stuff..."
                            "and you forgot your inhaler")

################ Main #####################
intro()

root.destroy()
