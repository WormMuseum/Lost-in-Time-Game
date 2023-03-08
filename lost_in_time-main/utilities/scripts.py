import os
from colorama import Fore
from art import *
from utilities.ascii_art import donkey, ogre, lone_tower, guards, kings_castle, kings_portrait, deck_of_cards,ss_finale, wizard, hanoiTower, print_europia


"""Opening script - Story of Europia - This is the first script that will run in the game."""
def opening_script(name): 
    # Print Europia Art
    print_europia()
    print(Fore.CYAN+"Press Enter to hear the story of Europia.", end="")
    input()
    os.system("clear" if os.name == "posix" else "cls" )
    # Print the story of Europia
    print(Fore.GREEN)
    print(text2art("The Story of Europia"))
    print(Fore.BLUE)
    print(f"""\n\nThe year is 2050 and after decades of nuclear war between the super powers of the world, the planet is now on the brink of destruction.
There are but a few safe havens remaining in the world and Europia is one of them. A nation born from the chaos which engulfed Europe.
The only hope left to save humanity from certain extinction is to go back in time and prevent this disaster from occuring in the first place.
\n\nThis is where you come in {name.title()}.\n\n
You are part of an organisation established to preserve humanity known as UEDP - the Unified Effort for Disaster Prevention
and you are one of the top scientists at the organisation. As such you have been tasked to be the first passenger of
MK-23i - the world's first ever purpose built time machine (despite it still being in beta phase).
\n\nThis is a huge honour and an extremely important mission - the fate of humanity depends on it.
""")
    print(Fore.CYAN+"\nPress Enter to begin the journey.", end="")
    input()
    os.system("clear" if os.name == "posix" else "cls" )


"""Disaster Strikes script - Where the time machine crashes and bandits surround the MC - Tic Tac Toe"""
def disaster_strikes_script():
    print(Fore.RED)
    print(text2art("Disaster Strikes!!!"))
    print(text2art("             **CRASH**"))
    print(Fore.BLUE)
    print(f"""
-- Shortly after take off warning lights start filling the dashboard and smoke begins to fill the time machine. Soon after, you are 
violently thrown out of the time machine and fall unconscious. Upon regaining conciousness, you are surrounded by a band of bandits. To 
make matters worse you do not recognise where you have been teleported to. 

Your current situation:

    1 - You are surrounded by a group of bandits. 
    2 - The time machine is broken.
    3 - The current year is unknown.

Being a skillful scientist, all you need to get the time machine up and running is some basic materials. You will also need the current year.
The bandits might have some information that could help. You must defeat them if you stand any chance to return home and save mankind. ---
""")
    input(Fore.CYAN+"\nPress Enter to take on the Bandits.")
    os.system("clear" if os.name == "posix" else "cls" )

"""Wounded donkey script - The Ogre looks for his donkey and tries to attack mc. - Rock Paper Scissors"""
def wounded_donkey_script():
    print(text2art("The Wounded Donkey"))
    # This is the ascii art of the donkey
    print(donkey())
    print(Fore.BLUE+"\nHuh?! What is this? A donkey?\n\nLooks like it's injured. Let's try tend to it's wounds...")
    print(Fore.CYAN+"\n\nPress Enter to help out the donkey.", end="")
    input()
    os.system("clear" if os.name == "posix" else "cls" )
    print(Fore.GREEN)
    print(text2art("ROARRR!!!"))
    print(Fore.GREEN+"\n\t* LOUD GROWLS AND ROARS *")
    print("\n\tGRRRRRRR... Donkeeeeyyyy!!!")
    print("\n\tDooooonnnnkeeeey!!!")
    print("\n\tDonkeeeeeeey!!! Where areeee youuuuuu!?")
    print("\n\tROOAAARRRRR!!!!!!!")
    print(Fore.BLUE+"\n\nHuh? What is that terrifying sound?")
    print("\nSounds like someones lost their donkey. Could it be this one?")
    print(Fore.CYAN+"\n\nPress Enter to find out who that is?", end="")
    input()
    os.system("clear" if os.name == "posix" else "cls" )
    print(Fore.GREEN+ogre())
    print(Fore.GREEN+"\tOgre: What are you doing with my donkey? *Growls*")
    print(Fore.CYAN+"\n\tYou: Woah! Chill out, I was just trying to patch up it's wounds.")
    print(Fore.GREEN+"\n\tOgre: *Growls louder*")
    print(Fore.BLUE+"\n\nThis looks bad. This guy is angry, and since when can Ogres talk. I need to fend him off...")
    print(Fore.CYAN+"\n\nPress Enter to fend off the angry Ogre.",end="")
    input()
    os.system("clear" if os.name == "posix" else "cls" )


"""Wizard of Hanoi script - From the moment the MC enters sees the tower until the Wizard set the challenge"""
def wizard_interactions():
    hanoiTower()
    print(Fore.BLUE+"""
    Wow!!! 

    What an impressive tower!!! I sure hope the wizard isn't as violent as all the other people in this era.

    Regardless, I have to make it out in one piece...
    """) 
    print(Fore.CYAN+"\n\nPress Enter to meet the wizard.", end="")
    input()
    os.system("clear" if os.name == "posix" else "cls")
    print(Fore.CYAN, end="")
    print(text2art("The Wizard Of Hanoi"))
    wizard()
    print(Fore.GREEN+"\n\tWizard: Well what do we have here? A visitor?\n\tYou sure don't look like you're from around here.")
    print(Fore.CYAN+"\n\tYou: Im not! You see my story is a rather long one...")
    print(Fore.GREEN+"\n\tWizard: Ohh.. Well let me grab us some drinks, I do love a good story...")
    print(Fore.CYAN+"\n\nPress Enter to explain your story to the Wizard.", end="")
    input()
    os.system("clear" if os.name == "posix" else "cls")

"""Wizard of Hanoi script - The Wizard sets MC the Tower of Hanoi challenge - Tower of Hanoi"""
def wizard_challenge():
    print(text2art("The Wizard Of Hanoi"))
    wizard()
    print(Fore.GREEN+"\n\tWizard: Hmmmm. I see, so you are from another era and you wish to return home.\n\tBut what is this 'nuclear weapon' you speak of? Perhaps dark magic of some sorts?")
    print(Fore.CYAN+"\n\tYou: No! It's kinda complicated to explain... But can you help me out oh mighty Wizard?")
    print(Fore.GREEN+"\n\tWizard: Well there is one thing I can think of but it would be far too difficult for you, it's out of the question.")
    print(Fore.CYAN+"\n\tYou: Please Wizard I beg of you!!! Let me at least try...")
    print(Fore.GREEN+"\n\tWizard: Well if you insist... Follow me.")
    print(Fore.CYAN+"\n\nPress Enter to follow the Wizard deeper into the tower.", end="")
    input()
    os.system("clear" if os.name == "posix" else "cls")
    print(text2art("The Tower Of Hanoi"))
    print(Fore.GREEN+"\tWizard: This is the Tower of Hanoi. A challenge like no other.\n\n\tThose who have overcome this tower have had all their wishes fulfilled.")
    print(Fore.GREEN+"""
\t\t     ||          ||          ||     
\t\t    #_1#         ||          ||     
\t\t   ##_2##        ||          ||     
\t\t  ###_3###       ||          ||     
\t\t ####_4####      ||          ||     
\t\t#####_5#####     ||          ||     
\t\t      A           B           C   
    """)
    print("\tThe rules are simple. You must move all the disks from Tower A to Tower C like so...")
    print(Fore.GREEN+"""
\t\t    ||          ||          ||      
\t\t    ||          ||         #_1#     
\t\t    ||          ||        ##_2##    
\t\t    ||          ||       ###_3###   
\t\t    ||          ||      ####_4####  
\t\t    ||          ||     #####_5##### 
\t\t     A           B           C      
    """)
    print("\n\tYou are not allowed to stack a larger disk on top of a smaller disk.")
    print("""\tThis would be an illegal move:

\t\t #####_5#####
\t\t   ###_3###  
\t\t  ####_4#### 

\n\tSince disk 5 is larger than disk 3. Pay attention to the numbers inside the disks. They can help you out.
    """)
    print("\n\tAre you ready to take on the tower?")
    print(Fore.CYAN+"\n\nPress Enter to take on the Tower of Hanoi.", end="")
    input()
    os.system("clear" if os.name == "posix" else "cls")



"""Lost time machine script - The guards arrest the mc after he loses his time machine and take the mc
   to the king. The king challenges the mc to a game of blackjack - Blackjack"""
def lost_machine():
    print(Fore.RED, end="")
    print(text2art("The Lost Time Machine"))         
    lone_tower()
    print(Fore.CYAN+"\n\tHuh?! Where is my time machine?!?!")
    print("\n\tI Know I left it right here next to that large tower before I met with the Wizard.")
    print("\n\tThis is a NIGHTMARE!!! I'm never going to make it back home. AGHHHHHH!!!!!")
    print(Fore.BLUE+"\n\t\t- You start to freak out -")
    print(Fore.CYAN+"\n\tThe world is going to end. Humanity will go extinct. All because I lost my time machine.")
    print("\n\tWhat can I do? What can I do?")
    print("\n\nPress Enter to look for your time machine.", end="")
    input()
    os.system("clear" if os.name == "posix" else "cls")
    guards()
    print(Fore.GREEN+"\n\tGuards: You there!!! Surrender at once!!!")
    print(Fore.CYAN+"\n\tYou: - Frightened and nervous - Me? Wha wha what is going on?")
    print(Fore.GREEN+"\n\tGuards: You are being detained under the orders of the King - His Royal Highness King Jack Black III -")
    print(Fore.CYAN+"\n\tYou: Huh?! The King?! But I didn't even do anything...")
    print("\n\nPress Enter to surrender.", end="")
    input()
    os.system("clear" if os.name == "posix" else "cls")
    
def kings_challenge(name):
    kings_castle()
    print(Fore.CYAN+"\n\tWOW!!! What an amazing castle!!!")
    print("\nPress Enter to proceed to the castle.", end="")
    input()
    os.system("clear" if os.name == "posix" else "cls")
    kings_portrait()
    print(Fore.CYAN+"What is going on? Looks like someone is getting knighted... But why am I here?... - Press Enter to find out.", end="")
    input()
    os.system("clear" if os.name == "posix" else "cls")
    print(text2art("An audience with the King"))
    print(Fore.GREEN+f"\n\tKing's attendant: Your majesty, the next item on the agenda is the case of {name.title()}.")
    print(Fore.CYAN+"\nHuh? That's me. I wonder what the king is going to do with me...")
    print(Fore.GREEN+f"\n\tKing's attendant: {name.title()} step forward!")
    print(Fore.CYAN+"\nIm so nervous I can't stop shaking. What is going to happen to me?")
    print(Fore.GREEN+"\n\tKing's attendant: Kneel before his majesty.")
    print(Fore.CYAN+"\n- You kneel abruptly -")
    print(Fore.GREEN+"\n\tKing Jack Black III: You may rise... You are here because my guards came across a curious machine on one of their patrols.")
    print("\tIt has been brought to my attention that this machine belongs to you.")
    print(Fore.CYAN+"\nHuh? Machine... What is he going on about...? Oh my TIME MACHINE!!! The king has it?\nThat's perfect now I can just politely ask him to return it.")
    print("\n\tYou: Yes your majesty that machine does indeed belong to me. I need it to get back home. Could I please have it back?")
    print(Fore.GREEN+"\n\tKing Jack Black III: Hmm... Well I see no reason not to return it back to you... under one condition.")
    print(Fore.CYAN+"\nWhat?! Condition?! I should have known it would never be that simple. Nothing in this forsaken era is.")
    print("\n\nPress Enter to find out the condition is.", end="")
    input()
    os.system("clear" if os.name == "posix" else "cls")
    print(Fore.GREEN, end="")
    print(text2art("The Kings Condition"))
    deck_of_cards()
    print("\n\tKing Jack Black III: Here in this kingdom we have a noble tradition going back generations...")
    print("\n\t\"Whomever manages to clear me out in a game of Blackjack shall be awarded knighthood\" \n\n\tKnighthood is the highest honour attainable in this kingdom.")
    print("\n\tIn addition, you will have your machine of time, or whatever you called it, returned back to you.")
    print(Fore.CYAN+"\nWhat?! Clear out King Jack Black III in a game of Blackjack?\n\nWhy does that sound deliberate?\n\nSo his name just happened to sound like his favourite game? Regardless...")
    print(Fore.GREEN+"\n\n\tYou: I ACCEPT YOUR MAJESTY!!!"+Fore.CYAN)
    print("\n\nPress Enter to take on the King.", end="")
    input()
    os.system("clear" if os.name == "posix" else "cls")


def time_to_guess(current_year):
    attempts = 0
    guess = None
    correct_year = current_year
    print(Fore.GREEN+ss_finale)
    print(Fore.CYAN+"\tYou: MY TIME MACHINE!!! It's so good to see you again, I was going crazy thinking I lost you...")
    print(Fore.CYAN+"\n\nYou need to put together all the clues you have gathered so far to figure out the current year.")
    while attempts < 3 and guess != correct_year:
        if not guess == correct_year and attempts:
            print(Fore.RED+"\n\tIncorrect!!!")
        w_attempt = "attempts" if (3-attempts) > 1 else "attempt"
        guess = input(Fore.CYAN+f"\nEnter the current year.\n\nYou have {3 - attempts} {w_attempt} remaining. >>> ")
        os.system("clear" if os.name == "posix" else "cls")
        attempts += 1
    return guess


"""You Win the game - You guess the current year correctly and you have acquired all the materials needed."""
def worlds_saviour(name):
    print(Fore.GREEN,end="")
    print(text2art("YOU DID IT!"))
    print("\nCongratulations on clearing the game!!! You can now return home and warn people from coming to this terrible era. just kidding.")
    print("\nHowever due to your efforts humanity now has a real chance at time traveling to an era before the war started and negotiating\na peace treaty which prevents the nuclear war from breaking out in the first place.")
    print(f"\nYou can be proud of yourself {name.title()}. You might of just saved the world.")
    input(Fore.CYAN+"\n\nPress Enter to return home.")

"""Game Failed - When you guess the current year correctly but not enough materials acquired"""
def not_close_enough(materials, name):
    print(Fore.GREEN,end="")
    print(text2art("Well Done!"))
    print(Fore.CYAN+"\nCongratulations on guessing the correct year! However you have not managed to acquire all the materials needed to rebuild the time machine.")
    print(f"\nYou have acquired {materials} materials. You needed 10 in order to rebuild the time machine.")
    print(f"\nIm afraid for you {name.title()} it's...\n\n"+Fore.RED)
    print(text2art("GAME OVER!!!"))

"""Game Failed - When you guess the current year incorrectly"""
def outright_failed():
    print(Fore.RED,end="")
    print(text2art("Failed!!!"))
    print(Fore.CYAN+"\nYou haven't managed to guess the correct year and as such are unable to get the time machine started.")
    print("\n\nIt's the end of the road for you im afraid. You are out of options!\n\n"+Fore.RED)
    print(text2art("GAME OVER!!!"))

"""Beat the bandits - tic tac toe game - win condition script"""
def btb_win(materials, current_era):
    print(Fore.GREEN)
    print(text2art("Well Done!!!"))
    print("You have triumped over those rowdy rebels!\n")
    print("Gained:\n")
    print("\t+ You have acquired {0}/10 materials needed to rebuild the time machine.".format(materials))
    print(f"\t+ You learn that you are currently in the 1{current_era[1] if current_era[2] == '0' and current_era[3] == '0' else str(int(current_era[1])+1)}th century.")
    if current_era[2] == '0' and current_era[3] == '0':
        print(Fore.CYAN+f"\n\t\tCurrent century: {str(int(current_era)-99)} - {current_era} <--- In this range.")
    else:
        print(Fore.CYAN+f"\n\t\tCurrent century: 1{current_era[1]}01 - 1{str(int(current_era[1])+1)}00 <--- In this range.")
    print(Fore.BLUE+"\n\nRemember all the clues you gather along your journey. They are crucial if you want to make it back home.")
    input(Fore.CYAN+"\n\nPress Enter to continue your journey")
    os.system("clear" if os.name == "posix" else "cls")
     

"""Beat the bandits - Tic Tac Toe game - Lose condition script"""
def btb_lose(materials):
    print(Fore.RED)
    print(text2art("Failed!!!"))
    print("Lost:\n")
    print("\t- You have not acquired any materials.")
    print("\t- You currently have {0}/10 materials needed to rebuild the time machine.".format(materials))
    print("\t- You have not gained any clues.")
    print(Fore.BLUE+"\n\nNow you must ensure you win the remaining challenges.")
    print("\nClues and materials are vital to pass the final challenge.")
    input(Fore.CYAN+"\n\nPress Enter to continue your journey")
    os.system("clear" if os.name == "posix" else "cls")
     

"""Beat the bandits - Tic Tac Toe game - Tie condition script"""
def btb_tie(materials):
    print(Fore.CYAN)
    print(text2art("Tie!!!"))
    print(Fore.CYAN+"Outcome:\n")
    print(Fore.GREEN+"\t+ You have gained {0}/10 materials needed to rebuild the time machine.".format(materials))
    print(Fore.RED+"\t+ You have not gained any clues.")
    print(Fore.BLUE+"\n\nYou must ensure you win the remaining challenges.")
    print("\nClues and materials are vital to pass the final challenge.")
    input(Fore.CYAN+"\n\nPress enter to continue your journey")
    os.system("clear" if os.name == "posix" else "cls")


"""Wounded Donkey - Win Condition Script - Rock Paper Scissors game"""
def wd_win(materials, current_era):
    decade = None
    # xx00 - xx09
    if current_era[2] == '0':
        decade = "first"
    # xx10 - xx19
    elif current_era[2] == '1':
        decade = "2nd"
    # xx20 - xx29
    elif current_era[2] == '2':
        decade = "3rd"
    # xx30 - xx39
    elif current_era[2] == '3':
        decade = "4th"
    # xx40 - xx49
    elif current_era[2] == '4':
        decade = "5th"
    # xx50 - xx59
    elif current_era[2] == '5':
        decade = "6th"
    # xx60 - xx69
    elif current_era[2] == '6':
        decade = "7th"
    # xx70 - xx79
    elif current_era[2] == '7':
        decade = "8th"
    # xx80 - xx89
    elif current_era[2] == '8':
        decade = "9th"
    # xx90 - xx99
    else:
        decade = "last"
    print(Fore.GREEN, end="")
    print(text2art("Congratulations!!!"))
    print("You have overcome that impetuous Ogre!")
    print("\nGained:\n")
    print("\t+ You have acquired {0}/10 materials needed to rebuild the time machine.".format(materials))
    print(f"\t+ You learn that you are currently in the {decade} decade of the century.")
    print("\t+ The Ogre offers you his assistance.")
    print(Fore.CYAN+f"\n\t\tCurrent decade: xx{current_era[2]}0 - xx{current_era[2]}9 <--- In this range.\n")
    print(Fore.BLUE+ "\n\nThe Ogre takes you to a tower where a wizard resides. The Ogre insists that the wizard can help you.\n")
    print(Fore.CYAN+"\n\nPress Enter to proceed to the tower.",end="")
    input()
    os.system("clear" if os.name == "posix" else "cls")


"""Wounded Donkey - Tie Condition Script - Rock Paper Scissors game"""
def wd_tie(materials):
    print(Fore.CYAN)
    print(text2art("Tie!!!"))
    print("Outcome:\n")
    print(Fore.GREEN+"\t+ You have acquired one material needed to rebuild the time machine.\n\t+ Currently {0}/10 materials acquired.".format(materials))
    print(Fore.CYAN+"\t- You have not gained any clues.")
    print(Fore.CYAN+"\n\nThe Ogre informs you that he has angered a mighty wizard and he is going to offer you up to the wizard to get back in his good graces.")
    print("\nYou are unable to decline.\n")
    print(Fore.CYAN+"\n\nPress Enter to find out what the wizard has in store for you.", end="")
    input()
    os.system("clear" if os.name == "posix" else "cls")


"""Wounded Donkey - Lose Condition Script - Rock Paper Scissors game"""
def wd_lose(materials):
    print(Fore.RED)
    print(text2art("Failed!!!"))
    print("Lost:\n")
    print("\t- You have not acquired any materials needed to rebuild the time machine.\n\t- Currently {0}/10 materials acquired.".format(materials))
    print("\t- You have not gained any clues.")
    print(Fore.CYAN+"\n\nThe Ogre informs you that he has angered a mighty wizard and he is going to offer you up to the wizard to get back in his good graces.")
    print("\nYou are unable to decline.\n")
    print(Fore.CYAN+"\n\nPress Enter to find out what the wizard has in store for you.", end="")
    input()
    os.system("clear" if os.name == "posix" else "cls")


"""Tower of Hanoi - Win Script"""
def tower_win(materials, current_era):
    year = None
    # xx00 - xx09
    if current_era[3] == '0':
        year = "first"
    # xx10 - xx19
    elif current_era[3] == '1':
        year = "2nd"
    # xx20 - xx29
    elif current_era[3] == '2':
        year = "3rd"
    # xx30 - xx39
    elif current_era[3] == '3':
        year = "4th"
    # xx40 - xx49
    elif current_era[3] == '4':
        year = "5th"
    # xx50 - xx59
    elif current_era[3] == '5':
        year = "6th"
    # xx60 - xx69
    elif current_era[3] == '6':
        year = "7th"
    # xx70 - xx79
    elif current_era[3] == '7':
        year = "8th"
    # xx80 - xx89
    elif current_era[3] == '8':
        year = "9th"
    # xx90 - xx99
    else:
        year = "last"
    print(Fore.GREEN)
    print(text2art("YOU DID IT!!!"))
    print("You have defeated the mighty Tower of Hanoi!\n")
    print("Gained:\n")
    print("\t+ You have acquired {0}/10 materials needed to rebuild the time machine.".format(materials))
    print(f"\t+ You learn that you are currently in the {year} year of the decade.")
    print(Fore.CYAN+f"\n\t\tCurrent year: xxx{current_era[3]} <--- Do you remember the century and the decade from previous challenges?")
    print(Fore.BLUE+"\n\nNow you must put together all the clues you have gathered along your journey.")
    print(Fore.CYAN+"\n\nPress Enter to continue your journey", end="")
    input()
    os.system("clear" if os.name == "posix" else "cls")

"""Tower of Hanoi - Lose Script - First Round - 5 Disks"""
def tower_lose_1(materials):
    print(Fore.RED)
    print(text2art("You Failed!!!"))
    print("Lost:\n")
    print("\t- You have not gained any materials.")
    print("\t- You currently have {0}/10 materials needed to rebuild the time machine.".format(materials))
    print("\t- You have not gained any clues.")
    print(Fore.BLUE+"\n\nAll is not lost... The Wizard wants to give you another chance to challenge the Tower.")
    print("\nThis time instead of 5 disks you only need to take on 3. This is your last chance so make it count!!!")
    print(Fore.CYAN+"\n\nPress Enter to take on the Tower again.", end="")
    input()
    os.system("clear" if os.name == "posix" else "cls")


"""Tower of Hanoi - Lose Script - Second Round - 3 Disks"""
def tower_lose_2(materials):
    print(Fore.RED)
    print(text2art("You Failed!!!"))
    print("Lost:\n")
    print("\t- You have not gained any materials.")
    print("\t- You currently have {0}/10 materials needed to rebuild the time machine.".format(materials))
    print("\t- You have not gained any clues.")
    print(Fore.BLUE+"\n\nYou have not managed to defeat the Tower of Hanoi so you are back at square one.")
    print("\nYou have not gained any new materials and you only have the clues you have gained from previous challenges.")
    print(Fore.CYAN+"\n\nPress Enter to continue your journey.", end="")
    input()
    os.system("clear" if os.name == "posix" else "cls")


"""Blackjack Win Script - Blackjack""" 
def blackjack_win(material, current_era):
    decade = None
    # xx00 - xx09
    if current_era[2] == '0':
        decade = "first"
    # xx10 - xx19
    elif current_era[2] == '1':
        decade = "2nd"
    # xx20 - xx29
    elif current_era[2] == '2':
        decade = "3rd"
    # xx30 - xx39
    elif current_era[2] == '3':
        decade = "4th"
    # xx40 - xx49
    elif current_era[2] == '4':
        decade = "5th"
    # xx50 - xx59
    elif current_era[2] == '5':
        decade = "6th"
    # xx60 - xx69
    elif current_era[2] == '6':
        decade = "7th"
    # xx70 - xx79
    elif current_era[2] == '7':
        decade = "8th"
    # xx80 - xx89
    elif current_era[2] == '8':
        decade = "9th"
    # xx90 - xx99
    else:
        decade = "last" 
    print(Fore.GREEN)
    print(text2art("YOU DID IT!!!"))
    print("Congratulations! You have defeated the king!\n")
    print("Gained:\n")
    print("\t+ You recieve the honour of knighthood. With this great honour you recieve abundant gifts and wealth.")
    print("\t+ You have acquired {0}/10 materials needed to rebuild the time machine.".format(material))
    print("\t+ The king returns your time machine back to you.")
    print("\t+ The king offers you a clue from any one of the previous challenges.")
    print(Fore.CYAN+"\nAs a reward for beating the king you are offered a chance to recieve a clue from any of the previous challenges.")
    print("\nYou can only pick one clue to recieve - either the current century, current decade or current year.")
    # Offer the player a clue and let the player pick which clue they want to recieve - century, decade, year
    while True:
        print("\nWhich do you pick? - Enter century, decade or year. >>> ", end="")
        choice = input().lower()
        if choice in ("century", "decade", "year"):
            os.system("clear" if os.name == "posix" else "cls")
            break
    if choice == "century":
        print(Fore.CYAN)
        print(text2art("Century"))
        print(f"\t+ You are currently in the 1{current_era[1] if current_era[2] == '0' and current_era[3] == '0' else str(int(current_era[1])+1)}th century.")
        if current_era[2] == '0' and current_era[3] == '0':
            print(Fore.CYAN+f"\n\t\tCurrent century: {str(int(current_era)-99)} - {current_era} <--- In this range.")
        else:
            print(Fore.CYAN+f"\n\t\tCurrent century: 1{current_era[1]}01 - 1{str(int(current_era[1])+1)}00 <--- In this range.")
        print(Fore.CYAN+"\n\nPress Enter to return to your time machine.", end="")
        input()
        os.system("clear" if os.name == "posix" else "cls")
    elif choice == "decade":
        print(Fore.CYAN)
        print(text2art("Decade"))
        print(Fore.GREEN+f"\t+ You learn that you are currently in the {decade} decade of the century.")
        print(Fore.CYAN+f"\n\t\tCurrent decade: xx{current_era[2]}0 - xx{current_era[2]}9 <--- In this range.\n")
        print(Fore.CYAN+"\n\nPress Enter to return to your time machine.", end="")
        input()
        os.system("clear" if os.name == "posix" else "cls")
    else:
        print(Fore.CYAN)
        print(text2art("Year"))
        print(Fore.GREEN+f"\t+ You learn that you are currently in the {decade} year of the decade.")
        print(Fore.CYAN+f"\n\t\tCurrent year: xxx{current_era[3]}")
        print(Fore.CYAN+"\n\nPress Enter to return to your time machine.", end="")
        input()
        os.system("clear" if os.name == "posix" else "cls")


"""Blackjack Lose Script - Blackjack""" 
def blackjack_lose(materials):
    print(Fore.RED)
    print(text2art("Failed!!!"))
    print(Fore.CYAN+"\nYou haven't managed to defeat the king! However the king rewards you for participating and returns your time machine back to you.")
    print(Fore.GREEN+"\nGained:\n")
    print("\t+ You have your time machine returned back to you.")
    print("\t+ The king awards you 5 materials for participating.")
    print("\t+ You have acquired {0}/10 materials needed to rebuild the time machine.".format(materials))
    print(Fore.RED+"Lost:\n")
    print("\t- You have not managed to gain any clues you have potentially missed out on.")
    print("\t- You must rely on the clues you currently have and the materials you were just awarded in addition\n\t  to the materials you already had to rebuild your time machine.")
    if materials >= 10:
        print(Fore.GREEN+f"\n\nWell Done!!! You have managed to acquire {materials}/10 materials so you can rebuild your time machine.")
        print("\nNow you must guess the correct year and you're as good as home.")
        input(Fore.CYAN+"\nPress Enter to proceed to your time machine.")
        os.system("clear" if os.name == "posix" else "cls")
    else:
        print(Fore.CYAN+f"\n\nYou haven't managed to acquire the 10 materials needed to rebuild your time machine. You have only acquired {materials} materials.")
        print("\nThat means you won't be able to rebuild your time machine.")
        input(Fore.CYAN+"\nPress Enter to proceed to your time machine.")
        os.system("clear" if os.name == "posix" else "cls")
