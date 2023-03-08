from colorama import Fore, Style
from art import *
import os
from games.rps import RPS
from random import randint
from utilities.scripts import opening_script, disaster_strikes_script, btb_win, btb_lose, btb_tie, wounded_donkey_script, wd_win, wd_lose, wd_tie, wizard_interactions, wizard_challenge, tower_win, tower_lose_1, tower_lose_2, lost_machine, blackjack_win, blackjack_lose, kings_challenge, time_to_guess, worlds_saviour, not_close_enough, outright_failed
from utilities.ascii_art import spaceship_animation
from games.tictactoe import Tic_Tac_Toe
from games.towerOfHanoi import TowerOfHanoi
from games.blackjack.blackjack_finale import Blackjack

class LostInTime:
    def __init__(self):
        self.name = ""
        self.material_acquired = 0
        self.current_era = str(randint(1000, 1700))

    def make_font_bold(self):
        print(Style.BRIGHT, end="")
    
    # Large Title
    def title_screen(self):
        os.system("clear" if os.name == "posix" else "cls")
        print(Fore.RED, end="")
        print(text2art("lost", font="block"))
        print(text2art("in", font="block"))
        print(text2art("time", font="block"))
        print(Fore.CYAN+f"Press Enter to start game.",end="")
        input()
        os.system("clear" if os.name == "posix" else "cls")

    def get_users_name(self):
        print("Enter your name: ", end="")
        users_name = input()
        os.system("clear" if os.name == "posix" else "cls")
        self.name = users_name

    def welcome_user(self):
        print(Fore.GREEN, end="")
        print(text2art(f"Welcome {self.name.title()}"))
        print(Fore.BLUE)
        print(text2art(f"The fate of humanity\nrests on your shoulders!"))
        print(Fore.CYAN+"Press Enter to begin adventure.", end="")
        input()
        os.system("clear" if os.name == "posix" else "cls")

    def story_of_europia(self):
        opening_script(self.name)
        spaceship_animation()

    def disaster_strikes(self):
        disaster_strikes_script()
    
    # Tic Tac Toe Game
    def beat_the_bandits(self):
        print(Fore.BLUE)
        print(text2art("Beat the Bandits"))
        print(Fore.GREEN+"The Bandits are O and your are X.")
        print("\nYou must beat them in this game of strategy and wit.\n"+Fore.BLUE)
        game = Tic_Tac_Toe("easy", "Tic Tac Toe")
        result = game.start()
        if result == 1:
            # Player won
            self.material_acquired += 2
            btb_win(self.material_acquired, self.current_era)
        elif result == 2:
            # Player lost
            btb_lose(self.material_acquired)
        else:
            # Tie Condition
            self.material_acquired += 1
            btb_tie(self.material_acquired)

    # Rock Paper Scissors Game Template
    def wounded_donkey(self):
        wounded_donkey_script()
        # This is where the Rock Paper Scissors Game goes
        rps = RPS()
        rps_result = rps.play_game()
        if rps_result == 1:
            # Win condition
            self.material_acquired += 2
            wd_win(self.material_acquired, self.current_era)
        elif rps_result == 2:
            # Tie condition
            self.material_acquired += 1
            wd_tie(self.material_acquired)
        else:
            # Lose condition
            wd_lose(self.material_acquired)

    def wizard_of_hanoi(self):
        # Player meets the Wizard for the first time
        wizard_interactions()
        # Wizard set the Player a challenge
        wizard_challenge()
        game = TowerOfHanoi(5)
        tower_result = game.start_game()
        if tower_result == 1:
            # Win condition
            self.material_acquired += 4
            tower_win(self.material_acquired, self.current_era)
        elif tower_result == 2:
            # Losing Condition for Round 1
            tower_lose_1(self.material_acquired)
            rematch = TowerOfHanoi(3)
            rematch_result = rematch.start_game()
            if rematch_result == 1:
                # Player won the rematch
                self.material_acquired += 2
                tower_win(self.material_acquired, self.current_era)
            else:
                # Player lost the rematch
                tower_lose_2(self.material_acquired)

    def king_jack_black(self):
        lost_machine()
        kings_challenge(self.name)
        # Blackjack Game begins
        print(Fore.GREEN, end="")
        print(text2art("Blackjack"))
        print(Fore.CYAN+"\nYou are facing the King at Blackjack. You start off with 100 gold pieces each.")
        print("\nThe goal is to clear out the King. You choose how much you want to bet at the start of each round.")
        blackjack = Blackjack()
        blackjack_result = blackjack.start_game()
        if blackjack_result == 1:
            # Win Condition
            self.material_acquired = 10
            print(Fore.GREEN+"\nYou have cleared out the king!!! Press Enter to claim your reward.", end="")
            input()
            os.system("clear" if os.name == 'posix' else "cls")
            blackjack_win(self.material_acquired, self.current_era)
        elif blackjack_result == 2:
            # Lose Condition
            self.material_acquired += 5
            print(Fore.RED+"\nThe King has cleared you out!!! Press Enter to see what's next.", end="")
            input()
            os.system("clear" if os.name == 'posix' else "cls")
            blackjack_lose(self.material_acquired)

    def current_year(self):
        correct_year = self.current_era
        guess = time_to_guess(self.current_era)
        if guess == correct_year and self.material_acquired >= 10:
            worlds_saviour(self.name)
        elif guess == correct_year and self.material_acquired < 10:
            not_close_enough(self.material_acquired, self.name)
        else:
            outright_failed()

    def start_game(self):
        self.make_font_bold()
        self.title_screen()
        self.get_users_name()
        self.welcome_user()
        self.story_of_europia()
        self.disaster_strikes()
        self.beat_the_bandits()
        self.wounded_donkey()
        self.wizard_of_hanoi()
        self.king_jack_black()
        self.current_year()

        
game = LostInTime()
game.start_game()
