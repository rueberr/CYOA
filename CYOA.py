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
def ivan4():
    ivan4 = simpledialog.askinteger("Bodies",
                                    "You have killed the guards. Would you like to hide " + \
                                    "the bodies or leave the bodies? (Type '1' to hide the " + \
                                    "bodies or type '2' to leave the bodies.")
    if (ivan4 == 1):
        messagebox.showinfo("Bodies",
                            "You have decided to hide the bodies. " + \
                            "In the process of hiding the bodies " + \
                            "you drop your gun and it misfires and " + \
                            "kills you. HEIST FAILED.")
        intro()
    elif (ivan4 == 2):
        messagebox.showinfo("Bodies",
                            "You have decided to leave the bodies. " + \
                            "A civilian sees the bodies and calls " + \
                            "the police. HEIST FAILED.")
        intro()
    else:
        ivan4()
def ivan3():
    ivan3 = simpledialog.askinteger("Money",
                                    "You have drilled the vault and gained access " + \
                                    "to the money. Would you like to betray your friends " + \
                                    "and take the money for yourself or share the money with your friends? " + \
                                    "(type '1' to betray or type '2' to share.")
    if (ivan3 == 1):
        messagebox.showinfo("Money",
                            "You have decided to betray your friends and " + \
                            "take the money for yourself. You safely make it " + \
                            "to Canada and live a happy life with your money.")
        intro()
    elif (ivan3 == 2):
        messagebox.showinfo("Money",
                            "You have decided to share with your friends. " + \
                            "You and your friends live the rest of your " + \
                            "days in luxury.")
        intro()
    else:
        ivan3()
def ivan2():
    ivan2 = simpledialog.askinteger("Vault",
                                     "Would you like to blast the vault " + \
                                     "or drill the vault? (Type '1' to " + \
                                     "blast the vault or type '2' to drill the vault).")
    if (ivan2 == 1):
        messagebox.showinfo("Vault",
                            "You have decided to blast the vault.")
        ivan3()
    elif (ivan2 == 2):
        messagebox.showinfo("Vault",
                            "You have decided to drill the vault. " + \
                            "Unfortunately, you have no drill experience. " + \
                            "HEIST FAILED.")
        intro()
    else:
        ivan2()

def ivan1():
    ivan1 = simpledialog.askinteger("Knock Out Guards",
                                     "You have elected to knock out the guards. " + \
                                     "would you like to knock out all of the guards " + \
                                     "or sneak around some of the guards. (Type '1' to " + \
                                     "knock out all the guards or type '2' to sneak around " + \
                                     "some of the guards).")

    if (ivan1 == 1):
        messagebox.showinfo("Knock Out All Guards",
                            "You have elected to knock out all guards. ")
        ivan2()
    elif (ivan1 == 2):
        messagebox.showinfo("Sneak",
                            "You have elected to sneak around some guards. " + \
                            "The guards wake up and kill you. HEIST FAILED.")
        intro()
    else:
        ivan1()
def choice1():
    choice1 = simpledialog.askinteger("IVAN",
                                     "You have chosen Ivan to be your character. As you approach " + \
                                     "the bank Ivan must either knock out or kill the gaurds " + \
                                     "in order to safely get into the bank. (Type '1' to knock out the gaurds " + \
                                     "or type '2' to kill the guards.")
    if (choice1 == 1):
   
        messagebox.showinfo("Knock Out",
                            "You have elected to knock out the guards. ")
        ivan1()                                
    elif (choice1 == 2):
        messagebox.showinfo("Kill",
                            "You have elected to kill the guards. ")
        ivan4()
    else:
        choice1()





    


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


def choice36():



    

    messagebox.showinfo("HOUSTON",
                       "Youre finally taking a risk. you feel so alive, but"
                       "your glasses begin to fog up. As you take them off to"
                       "clean them you drop them, then as you fumble on the ground for them"
                       "you crush them. now you have no vision other than some blurs"
                       "you attempt to look at the screen but you dont notice the brigade of"
                       "charging into the bank and arresting both ivan and carmine."
                       "HEIST FAILLED")
    intro()
def choice35():

    choice35 = simpledialog.askinteger("HOUSTON",
                                      "You hear a few shots ring out and you hit the jammer."
                                      "all calls and radio within the bank are blocked."
                                      "You watch on the cameras as Carmine and Ivan blast the vault"
                                      "as they are loading the bags into the van you hear sirens"
                                      "as they get closer ivan is shot in the leg by a lone surviving"
                                      "guard. Carmine shoots the guard and runs over to help Ivan."
                                      "But you are starting to panic as you hear the sirens just"
                                      "A few blocks away. type 1 to leave with the money or 2 to"
                                      "stay with your team.")


    
    if (choice35 == 1):
        messagebox.showinfo("HOUSTON",
                            "The tires squeal as you tear down the road."
                            "as you turn you see cops begin to pour onto the street and surround"
                            "Carmine and Ivan. you hear shots ring out as you drive away."
                            "they continue for a few seconds and abruptly end."
                            "no reason to turn back now, and anyway youre already"
                            "on your way to a sandy beach in mexico where you can lather"
                            "yourself in 10,000 spf sunscreen and drink virgin cuba libres all day")
        intro()
    elif (choice35 == 2):
        messagebox.showinfo("HOUSTON",
                            "Carmine picks Ivan up and tosses him in the back of the van"
                            "and he gets in the front. You drive away just in time and"
                            "are unseen by police. You all sit in silence for a moment"
                            "then in a heavy russian accent ivan says 'just a small town"
                            "girl, livin in a lonely world' soon the whole van erupts in"
                            "song as you head for Mexico")
        intro()
def choice34():

    messagebox.showinfo("HOUSTON",
                        "The mask over your face may as well be smothering you."
                        "You cant breathe as you try to keep up. as soon as you"
                        "walk through the door you trip and hit your head"
                        "you wake up in a pair of handcuffs next to ivan and carmine."
                        "HEIST FAILED")
    intro()
def choice33():

    choice33 = simpledialog.askinteger("HOUSTON",
                                      "Now that you made the decision to stay you are the"
                                      "eye in the sky. Its your call now. do you want to"
                                      "jam all police scanners or just watch for the cops on the cams?"
                                      "type 1 to jam them or 2 to watch.")

    if (choice33 == 1):
        messagebox.showinfo("HOUSTON",
                            "playin it safe huh?"
                            "dont waanna take a little risk?"
                            "Just like always.")



        choice35()

    elif (choice33 == 2):
        messagebox.showinfo("HOUSTON",
                            "Wow Houston im impressed. youre taking a risk."
                            "I thought you were just a nerd.")
        choice36()
    else:
        choice33()
def choice32():

    choice32 = simpledialog.askinteger("HOUSTON",
                                     "You get set up and head inside you let the others do the"
                                     "heavy lifting and you just walk back to the vault."
                                     "You realize that this vault is fairly easy to hack,"
                                     "but you did bring explosives to blow the vault..."
                                     "type 1 to hack or 2 to blow it.")

    if (choice32 == 1):
        messagebox.showinfo("HOUSTON",
                            "You connect your computer to the vault and hack away"
                            "after a few seconds you get it to open and your team"
                            "moves in. as they are collecting money you attempt to"
                            "Your computer but it errors the system and the vault"
                            "locks closing your team inside"
                            "HEIST FAILED")

    elif (choice32 == 2):
           messagebox.showinfo("HOUSTON",
                               "youve logged thousands of hours playing call of duty"
                               "What could possibly go wrong? you set and prime the C-4"
                               "you take cover and hit the blast button. shrapnell hits"
                               "ivan and disfigures him as all of the money is ruined"
                               "you probably shouldnt of used so much"
                               "HEIST FAILED")
    else: choice32()
def choice31():

    choice31 = simpledialog.askinteger("HOUSTON",
                                      "You turn off the cameras. It was easy... too easy..."+ \
                                      "but now you are faced with a choice. stay in the saftey of the van"+ \
                                      "or risk it and go inside with the team and make sure they get the job done right."+ \
                                      "type 1 to stay, or 2 to go.")
    if (choice31 == 1):
        messagebox.showinfo("HOUSTON",
                            "You're a bit wimpy, but then again you always have been"+ \
                            "no ammount of therapy could erase the bullying")
        choice33()


    elif (choice31 == 2):
        messagebox.showinfo("HOUSTON",
                            
                            "Youre taking the brave way, this may gain you respect"
                            "with your team, but this is scary stuff..."
                            "and you forgot your inhaler")
        choice34()
        
    else:
        choice31()
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
        choice31()
    else:
        choice3()


################ Main #####################
intro()

root.destroy()
