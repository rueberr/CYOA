# Choose.py
# by Ryan Rueber, Chris Renslow, and Stetson Jones
# Description: An adventure about a heist.


# Import Statements
import random
from tkinter import *
import tkinter.simpledialog as simpledialog
import tkinter.messagebox as messagebox
root = Tk()

root = Tk()
w = Label(root, text="Choose Your Own Adventure")
w.pack()

#Functions


def intro():
    """ Introductory Function -> starts the story going """
    messagebox.showinfo("Title", "\nHello, you have the option of being one " + \
                        "of three characters as you pull off a heist. You can " + \
                        "be Carmine (the leader), " + \
                        "Ivan (the muscle), or Houstan (the brains).")
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
        intro()

################ Ryan Rueber Functions #####################
def choice1():
    choice1 = simpledialog.askinteger("IVAN",
                                     "You have chosen Ivan to be your character. As you approach " + \
                                     "the bank Ivan must either knock out or kill the gaurds " + \
                                     "in order to safely get into the bank. (Type '1' to knock out the gaurds " + \
                                     "or type '2' to kill the guards.")

def ivan1():
    ivan1 = simpledialog.askinteger("Knock Out Guards",
                                     "You have elected to knock out the guards. " + \
                                     "would you like to knock out all of the guards " + \
                                     "or sneak around some of the guards. (Type '1' to " + \
                                     "knock out all the guards or type '2' to sneak around " + \
                                     "some of the guards).")
def ivan2():
    ivan2 = simpledialog.askinteger("Knock Out All Guards",
                                     "You have elected to knock out all of the " + \
                                     "gaurds. Would you like to knock out all of the guards " + \
                                     "or sneak around some of the guards. (Type '1' to " + \
                                     "knock out all the guards or type '2' to sneak around " + \
                                     "some of the guards).")



if (choice1 == 1):
   
    messagebox.showinfo("Knock Out",
                        "You have elected to knock out the guards. ")
    ivan1()                                


elif (choice1 == 2):
    messagebox.showinfo("Kill",
                        "You have elected to kill the guards. ")
    ivan1()
else:
    choice1()

if (ivan1 = 1):
    messagebox.showinfo("Knock Out All Guards",
                        "You have elected to knock out all guards. ")
elif (ivan = 1):
    messagebox.showinfo("Sneak",
                        "You have elected to sneak around some guards. " + \
                        "The guards wake up and kill you. HEIST FAILED.")

################ Chris Renslow Functions #####################
def choice16():
        choice16 = simpledialog.askinteger("WIN", "You take the gold and exit the way you came quietly and safely. " + \
                                       "Now you have a choice will you betray your team and take all the money for yourself or share it? " + \
                                           "1 for betray, 2 for trust")
        if (choice16 == 1):
        
            messagebox.showinfo("Betray",
                            "You kill your partners, steal the money and head to Mexico " + \
                            "THE END")
        elif (choice16 == 2):
            messagebox.showinfo("Share",
                            "You decide to be a good person and share the earning. " + \
                             "Everyone takes their cut, splits up and heads to Mexico. THE END ")
        else:
               choice16()
    
    




def choice15():
    choice15 = simpledialog.askinteger("Snuck to the Vault" , 
                                       "You snuck in to the vault and have a choice to either blast the vault open or drill it open."+ \
                                        "1 for blast 2 for drill")
    if (choice15 == 1):
        messagebox.showinfo("Blast",
                             "You blast the Vault. Planting the explosives was easy, Carmine has done it before. This time he had a feeling though, a bad one. " + \
                            "He had used to much C4, only realizing it after the blast. Ivan took cover behind a weak wall that collapes killing him in the blast. "+ \
                            "Carmine attempts to pull him out but he is already dead. He decides he cannot continue without him. HEIST FAILED ")
        intro()
        

    elif (choice15 == 2):
        messagebox.showinfo("Drill",
                            "Sneaking past the guards gives you the extra time to use your weak drill on the vault. " + \
                             "You open the vault and the shine of the gold bars against the light blinds you. 17 million in gold bars 4 million in bonds. " + \
                            "You've pulled off the biggest heist of your career. ")
        choice16()
    
    
    else:
        choice15()  
    
    
                                    







def choice14():
    choice14 = simpledialog.askinteger( "Roof" ,"Kill the guards or try and sneak past them to the vault on the roof? 1 for kill 2 for sneak ")

    if (choice14 == 1):
        messagebox.showinfo("Kill",
                            "You kill the guards but Ivan gets shot, enters rage mode and pushes several guards off a balcony. " + \
                            "This alerts the guards and they kill the team. HEIST FAILED")
        intro()
        

    elif (choice14 == 2):
        messagebox.showinfo("Sneak",
                            "You try and sneak past the roof guards and the guards in the bank spot you through the huge skylights on top of the bank. "+ \
                             "They alert the police. HEIST FAILED ")
        intro()
    
    
    else:
        choice14()             

        
def choice13():
    choice13 = simpledialog.askinteger( "Basement" ,"Kill the guards or try and sneak past them to the vault in the basement? 1 for kill 2 for sneak ")

    if (choice13 == 1):
        messagebox.showinfo("Kill",
                            "You try to quietly kill the guards but the others hear you. " + \
                            "Being a position of tactical superiority the guards are easily able to take you down. . HEIST FAILED")
        intro()
    elif (choice13 == 2):
        messagebox.showinfo("Sneak",
                            "You easily sneak past the dimwitted guards and head to the Vault. It is a huge custom made bank vault. " + \
                            "You estimate the weight to be over 3 tons, the biggest the team has ever scored.")
        choice15()
    
    
    else:
        choice13()             



def choice11():
    choice11 = simpledialog.askinteger("Roof or Basement" ,"You can either go in on the roof of the bank or underground through the basement. " + \
                          "1 for roof 2 for basement")
    if (choice11 == 1):
        messagebox.showinfo("Roof",
                            "The team climbs the building opposite the bank and ziplines across. Ivan picks the lock to to the roof entrance and they enter. " + \
                            "They go down the stairs and encounter guards")
        choice14()
        
    elif (choice11 == 2):
        messagebox.showinfo("Basement",
                            "Ivan picks a lock to the banks basement entrance. The team enters and goes up the stairs and encounters guards.")
        choice13()
    
    
    else:
        choice11()                                          

def choice12():
    choice12 = simpledialog.askinteger("Front Door" , "You go in guns blazing through the front door and make your way to the Vault. " + \
                            "Will you drill the Vault or blast the Vault open with explosives? 1 for Drill 2 for blast")
    if (choice12 == 1):
        messagebox.showinfo("Drill",
                            "You try and drill the vault but the drill you brought was to weak for the Vault. " + \
                            "You take too long, the cops come and see the dead bodies and start shooting. " + \
                            "The team shoots back but the cops soon overwhelm them. Running out of ammo, the team starts dropping one by one. " + \
                            "Ivan first then Houston until Carmine is the only one left. He fights to his last breath... HEIST FAILED")
        intro()
                                             

    elif (choice12 == 2):
        messagebox.showinfo("Blast",
                            "You blast the Vault. Planting the explosives was easy, Carmine has done it before. This time he had a feeling though, a bad one. " + \
                            "He had used to much C4, only realizing it after the blast. Ivan took cover behind a weak wall that collapes killing him in the blast. "+ \
                            "Carmine attempts to pull him out but he is already dead. He decides he cannot continue without him. HEIST FAILED")
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
                            "You decide to go in the front door. This may not be a wise choice but it could be easier.")
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

<<<<<<< HEAD

=======
>>>>>>> 5157600109c187f1d3c869f07eda068ecfc5bff9
    choice = simpledialog.askinterger("HOUSTON",
                                      "You turn off the cameras. It was easy... too easy..."+ \
                                      "but now you are faced with a choice. stay in the saftey of the van"+ \
                                      "or risk it and go inside with the team and make sure they get the job done right."+ \
                                      "type 1 to stay, or 2 to go.")
    if (choice == 1):
        messagebox.showinfo("HOUSTON",
                            "You're a bit wimpy, but then again you always have been"+ \
                            "no ammount of therapy could erase the bullying")



################ Main #####################
intro()

root.destroy()
