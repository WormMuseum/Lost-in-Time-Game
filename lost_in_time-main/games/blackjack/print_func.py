from colorama import Fore, Style

# Function to print the cards
def print_cards(cards, hidden, player):
    if player:
        print("\nYour hand:")
    suits_values = {"Spades":"\u2664", "Hearts":"\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}
    print(Style.BRIGHT, end="")
    s = ""
    for key, value in cards.items():
        s = s + "\t ________________"
    if hidden:
        s += "\t ________________"
    print(s)
 
 
    s = ""
    for key,value in cards.items():
        s = s + "\t|                |"
    if hidden:
        s += "\t|                |"    
    print(s)
 
    s = ""
    for key,value in cards.items():
        if key[0]+key[1] == '10':
            s = s + "\t|  {}            |".format(value)
        elif value == 10:
            s = s + "\t|  {}             |".format(key[0])
        elif key[0]+key[1]+key[2] == "Ace":
            s = s + "\t|  {}             |".format(key[0])
        else:
            s = s + "\t|  {}             |".format(value)  
    if hidden:
        s += "\t|                |"    
    print(s)
 
    s = ""
    for key, value in cards.items():
        s = s + "\t|                |"
    if hidden:
        s += "\t|      * *       |"
    print(s)    
 
    s = ""
    for key, value in cards.items():
        s = s + "\t|                |"
    if hidden:
        s += "\t|    *     *     |"
    print(s)    
 
    s = ""
    for key, value in cards.items():
        s = s + "\t|                |"
    if hidden:
        s += "\t|   *       *    |"
    print(s)    
 
    s = ""
    for key, value in cards.items():
        s = s + "\t|                |"
    if hidden:
        s += "\t|   *       *    |"
    print(s)    
 
    s = ""
    for key, value in cards.items():
        suit = key.split(" ")[-1]
        s = s + "\t|       {}        |".format(suits_values[suit])
    if hidden:
        s += "\t|          *     |"
    print(s)    
 
    s = ""
    for key, value in cards.items():
        s = s + "\t|                |"
    if hidden:
        s += "\t|         *      |"
    print(s)    
 
    s = ""
    for key, value in cards.items():
        s = s + "\t|                |"
    if hidden:
        s += "\t|        *       |"
    print(s)
 
    s = ""
    for key, value in cards.items():
        s = s + "\t|                |"
    if hidden:
        s += "\t|                |"
    print(s)
 
    s = ""
    for key, value in cards.items():
        s = s + "\t|                |"
    if hidden:
        s += "\t|                |"
    print(s)    
 
    s = ""
    for key, value in cards.items():
        if key[0]+key[1] == '10':
            s = s + "\t|             {} |".format(value)
        elif value == 10:
            s = s + "\t|             {}  |".format(key[0])
        elif key[0]+key[1]+key[2] == "Ace":
            s = s + "\t|             {}  |".format(key[0])
        else:
            s = s + "\t|            {}   |".format(value)
    if hidden:
        s += "\t|        *       |"        
    print(s)    
         
    s = ""
    for key, value in cards.items():
        s = s + "\t|________________|"
    if hidden:
        s += "\t|________________|"
    print(s)        
 
    print()