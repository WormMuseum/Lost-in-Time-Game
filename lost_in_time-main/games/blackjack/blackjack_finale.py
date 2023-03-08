#setup
import random
import os
if __name__ == "__main__":
    from print_func import print_cards
else:
    from .print_func import print_cards
from colorama import Fore, Style
from art import *

class Blackjack:
    def __init__(self):
        self.king = 0
        self.user = 0
        self.usercards={}
        self.kingcards={}
        self.wallet = 100
        self.deck = {
            'Ace of Spades': 11,
            '2 of Spades': 2,
            '3 of Spades': 3,
            '4 of Spades': 4,
            '5 of Spades': 5,
            '6 of Spades': 6,
            '7 of Spades': 7,
            '8 of Spades': 8,
            '9 of Spades': 9,
            '10 of Spades': 10,
            'Jack of Spades': 10,
            'Queen of Spades': 10,
            'King of Spades': 10,
            'Ace of Hearts': 11,
            '2 of Hearts': 2,
            '3 of Hearts': 3,
            '4 of Hearts': 4,
            '5 of Hearts': 5,
            '6 of Hearts': 6,
            '7 of Hearts': 7,
            '8 of Hearts': 8,
            '9 of Hearts': 9,
            '10 of Hearts': 10,
            'Jack of Hearts': 10,
            'Queen of Hearts': 10,
            'King of Hearts': 10,
            'Ace of Clubs': 11,
            '2 of Clubs': 2,
            '3 of Clubs': 3,
            '4 of Clubs': 4,
            '5 of Clubs': 5,
            '6 of Clubs': 6,
            '7 of Clubs': 7,
            '8 of Clubs': 8,
            '9 of Clubs': 9,
            '10 of Clubs': 10,
            'Jack of Clubs': 10,
            'Queen of Clubs': 10,
            'King of Clubs': 10,
            'Ace of Diamonds': 11,
            '2 of Diamonds': 2,
            '3 of Diamonds': 3,
            '4 of Diamonds': 4,
            '5 of Diamonds': 5,
            '6 of Diamonds': 6,
            '7 of Diamonds': 7,
            '8 of Diamonds': 8,
            '9 of Diamonds': 9,
            '10 of Diamonds': 10,
            'Jack of Diamonds': 10,
            'Queen of Diamonds': 10,
            'King of Diamonds': 10
        }
    def make_font_bold(self):
        print(Style.BRIGHT, end="")

    def print_wallet(self, wallet):
        print(Fore.GREEN+"\n\tYour wallet:", wallet)
        print(Fore.GREEN+"\tKing's wallet:",200 - wallet)

    #functions
    def check_ace(self, user_or_king):
        for key, value in user_or_king.items():
            options = ['Ace of Spades','Ace of Hearts','Ace of Clubs','Ace of Diamonds']
            if key in options:
                total = sum(user_or_king.values())
                if total > 21:
                    user_or_king[key] = 1

    def KingsPick(self):
        if len(list(self.deck))==0:
            self.deck = {
            'Ace of Spades': 11,
            '2 of Spades': 2,
            '3 of Spades': 3,
            '4 of Spades': 4,
            '5 of Spades': 5,
            '6 of Spades': 6,
            '7 of Spades': 7,
            '8 of Spades': 8,
            '9 of Spades': 9,
            '10 of Spades': 10,
            'Jack of Spades': 10,
            'Queen of Spades': 10,
            'King of Spades': 10,
            'Ace of Hearts': 11,
            '2 of Hearts': 2,
            '3 of Hearts': 3,
            '4 of Hearts': 4,
            '5 of Hearts': 5,
            '6 of Hearts': 6,
            '7 of Hearts': 7,
            '8 of Hearts': 8,
            '9 of Hearts': 9,
            '10 of Hearts': 10,
            'Jack of Hearts': 10,
            'Queen of Hearts': 10,
            'King of Hearts': 10,
            'Ace of Clubs': 11,
            '2 of Clubs': 2,
            '3 of Clubs': 3,
            '4 of Clubs': 4,
            '5 of Clubs': 5,
            '6 of Clubs': 6,
            '7 of Clubs': 7,
            '8 of Clubs': 8,
            '9 of Clubs': 9,
            '10 of Clubs': 10,
            'Jack of Clubs': 10,
            'Queen of Clubs': 10,
            'King of Clubs': 10,
            'Ace of Diamonds': 11,
            '2 of Diamonds': 2,
            '3 of Diamonds': 3,
            '4 of Diamonds': 4,
            '5 of Diamonds': 5,
            '6 of Diamonds': 6,
            '7 of Diamonds': 7,
            '8 of Diamonds': 8,
            '9 of Diamonds': 9,
            '10 of Diamonds': 10,
            'Jack of Diamonds': 10,
            'Queen of Diamonds': 10,
            'King of Diamonds': 10
        }
            for item in self.kingcards:
                self.deck.pop(item)
            for item in self.usercards:
                self.deck.pop(item)
        card = random.choice(list(self.deck.items()))
        self.deck.pop(card[0])
        self.kingcards.update({card[0]:card[1]})
        self.check_ace(self.kingcards)

    def print_value(self, value):
        print(Fore.CYAN+"\nYour current score is "+ str(self.user) + '.')

    def won_bet(self, amount, wallet):
        print(Fore.GREEN+"\tYou Win!")
        print(Fore.CYAN+f"\nYou have taken {amount} gold pieces from the King.")

    def lost_bet(self, amount, wallet):
        print(Fore.GREEN+f"\tThe King Wins!")
        print(Fore.CYAN+f"\nThe King has taken {amount} gold pieces from you.")

    def UsersPick(self):
        if len(list(self.deck))==0:
            self.deck = {
            'Ace of Spades': 11,
            '2 of Spades': 2,
            '3 of Spades': 3,
            '4 of Spades': 4,
            '5 of Spades': 5,
            '6 of Spades': 6,
            '7 of Spades': 7,
            '8 of Spades': 8,
            '9 of Spades': 9,
            '10 of Spades': 10,
            'Jack of Spades': 10,
            'Queen of Spades': 10,
            'King of Spades': 10,
            'Ace of Hearts': 11,
            '2 of Hearts': 2,
            '3 of Hearts': 3,
            '4 of Hearts': 4,
            '5 of Hearts': 5,
            '6 of Hearts': 6,
            '7 of Hearts': 7,
            '8 of Hearts': 8,
            '9 of Hearts': 9,
            '10 of Hearts': 10,
            'Jack of Hearts': 10,
            'Queen of Hearts': 10,
            'King of Hearts': 10,
            'Ace of Clubs': 11,
            '2 of Clubs': 2,
            '3 of Clubs': 3,
            '4 of Clubs': 4,
            '5 of Clubs': 5,
            '6 of Clubs': 6,
            '7 of Clubs': 7,
            '8 of Clubs': 8,
            '9 of Clubs': 9,
            '10 of Clubs': 10,
            'Jack of Clubs': 10,
            'Queen of Clubs': 10,
            'King of Clubs': 10,
            'Ace of Diamonds': 11,
            '2 of Diamonds': 2,
            '3 of Diamonds': 3,
            '4 of Diamonds': 4,
            '5 of Diamonds': 5,
            '6 of Diamonds': 6,
            '7 of Diamonds': 7,
            '8 of Diamonds': 8,
            '9 of Diamonds': 9,
            '10 of Diamonds': 10,
            'Jack of Diamonds': 10,
            'Queen of Diamonds': 10,
            'King of Diamonds': 10
        }
            for item in self.kingcards:
                self.deck.pop(item)
            for item in self.usercards:
                self.deck.pop(item)
        card = random.choice(list(self.deck.items()))
        self.deck.pop(card[0])
        self.usercards.update({card[0]:card[1]})
        self.check_ace(self.usercards)

    def print_hand(self, hand, king):
        print("|"+"-"*50+"|")
        print("|"+"\tCard Suit\t\tValue"+" "*14+"|")
        print("|"+"-"*50+"|")
        for key, value in hand.items():
            if value > 9:
                print("|"+f"\t{key:<20} \t{value}"+" "*17+"|")
            else:
                print("|"+f"\t{key:<20} \t{value}"+" "*18+"|")
        print("|"+"-"*50+"|")
    
    # Start of the main function
    def start_game(self):
        self.make_font_bold()
        if self.wallet < 1:
            # Lose Condition
            return 2
        elif self.wallet >= 200:
            # Win Condition
            return 1
        while True:
            try:
                print(Fore.CYAN+"\nHow much do you want to bet on this round? ", end="")
                amount = int(input())
                if amount > self.wallet:
                    print(Fore.RED+f"\nYou don't have enough to place that bet. The max bet you can place is {self.wallet}.")
                    continue
                if amount < 1:
                    print(Fore.RED+"\nMinimum amount you can bet is 1 gold piece.")
                    continue
                break
            except ValueError:
                print(Fore.RED+"\nChoose a number!!!")
        os.system('cls' if os.name == 'nt' else 'clear')
        self.usercards.clear()
        self.kingcards.clear()
        # At this stage both the king and the player are dealt two cards
        for i in range(2):
            self.KingsPick()
        public = {tupes for index, tupes in enumerate(self.kingcards.items()) if index == 0}
        key = tuple(public)[0]
        hidden_values = {key[0]:key[1]}
        print(Fore.GREEN+"The King's hand:",list(self.kingcards)[0], "and a hidden card.")
        print(Fore.GREEN, end="")
        print_cards(hidden_values, True, False)
        self.print_hand(hidden_values, True) 

        for i in range(2):
            self.UsersPick()


        print(Fore.CYAN, end="")
        print_cards(self.usercards, False, True)
        self.print_hand(self.usercards, False)

        #calculating values, printing your value
        self.king = sum(self.kingcards.values())

        self.user = sum(self.usercards.values())
        self.print_value(self.user)
        print()

        #If at the start the round any player get 21 end the round
        if self.king == 21 and self.user == 21:#draw
            print("It's a draw. Press Enter to reveal the Kings cards.", end="")
            input()
            os.system("clear" if os.name == "posix" else "cls")
            print(Fore.GREEN+f"The Kings hidden card was a {list(self.kingcards.keys())[1]}.")
            print(Fore.GREEN, end="")
            print_cards(self.kingcards, False, False)
            self.print_hand(self.kingcards, True)
            print(Fore.CYAN+"You both have 21!\n")
            print("\tIt's draw! Nobody wins any gold pieces!")
            self.print_wallet(self.wallet)
            return self.start_game() 
        elif self.king == 21:#king wins
            print("The King's got a Blackjack. Press Enter to reveal the Kings cards.", end="")
            input()
            os.system("clear" if os.name == "posix" else "cls")
            self.wallet -= amount
            print(Fore.GREEN+f"The Kings hidden card was a {list(self.kingcards.keys())[1]}.")
            print(Fore.GREEN, end="")
            print_cards(self.kingcards, False, False)
            self.print_hand(self.kingcards, True)
            self.lost_bet(amount, self.wallet)
            self.print_wallet(self.wallet)
            return self.start_game()
        elif self.user == 21:#user wins
            self.wallet += amount
            self.won_bet(amount, self.wallet)
            self.print_wallet(self.wallet)
            return self.start_game()

        #hitting or standing?
        while True:
            print(Fore.CYAN+"Hit or Stand: ",end="")
            choice = input()
            os.system("clear" if os.name == "posix" else "cls")
            if choice.lower() == "hit": 
                self.UsersPick()
                self.user = sum(self.usercards.values())
                print(Fore.CYAN, end="")    
                print_cards(self.usercards, False, True)
                self.print_hand(self.usercards, False)
                self.print_value(self.user)
                if self.user>21:
                    print(Fore.RED+"\n\tYou've gone bust!!!\n")
                    self.wallet -= amount
                    self.lost_bet(amount, self.wallet)
                    self.print_wallet(self.wallet)
                    return self.start_game()
                if self.user == 21:
                    self.wallet += amount
                    print()
                    self.won_bet(amount, self.wallet)
                    self.print_wallet(self.wallet)
                    return self.start_game()
                print()
            elif choice.lower() == "stand":
                break
            else:
                print(Fore.RED+"\n\tThat is not an option!\n"+Fore.CYAN)
                print_cards(self.usercards, False, True)

        print(Fore.GREEN+f"The Kings hidden card was a {list(self.kingcards.keys())[1]}.")
        print(Fore.GREEN, end="")
        print_cards(self.kingcards, False, False)
        #king's turn
        while self.king < 17:
            self.KingsPick()
            print(Fore.GREEN+"The King has picked up a",list(self.kingcards)[-1])
            print(Fore.GREEN, end="")
            print_cards(self.kingcards, False, False)
            self.king = sum(self.kingcards.values())
        self.print_hand(self.kingcards, True) if sum(self.kingcards.values()) >= 17 else None

        #deciding if you won or lost or draw
        print(Fore.GREEN+"\nThe King's total score is "+str(self.king)+".")
        print()
        if (self.king > self.user and self.king < 22) or self.user > 21:
            self.wallet -= amount
            self.lost_bet(amount, self.wallet)
        elif self.user > self.king and self.user < 22:
            self.wallet += amount
            self.won_bet(amount, self.wallet)
        elif self.user < 22 and self.king > 21:
            self.wallet += amount
            self.won_bet(amount, self.wallet)
        else:
            print("\tIt's draw! Nobody wins anything!")
        self.print_wallet(self.wallet)
        return self.start_game()

if __name__ == "__main__":
    os.system("clear" if os.name == "posix" else "cls")
    print(Style.BRIGHT, end="")
    print(Fore.GREEN, end="")
    print(text2art("Blackjack"))
    print(Fore.CYAN+"\nYou are facing the King at Blackjack. You start off with 100 gold pieces each.")
    print("\nThe goal is to clear out the King. You choose how much you want to bet at the start of each round.")
    game = Blackjack()
    result = game.start_game()
    if result == 1:
        print(Fore.GREEN+"\nYou have cleared out the king!!!")
    elif result == 2:
        print(Fore.RED+"\nThe King has cleared you out!!!")

