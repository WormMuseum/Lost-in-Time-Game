import random
from colorama import Fore, Style
from art import *
import os
print(Style.BRIGHT, end="")


"""
    Outcome:
    player beating the ogre
    rock beats scissors
    rock ties with rock
    rock loses to paper

    scissors beats paper
    scissors ties with scissors
    scissors loses to rock

    paper beats rock 
    paper ties with paper
    paper loses to scissors

"""


class RPS:
    def __init__(self):
        self.options = ("rock", "paper", "scissors")
        self.player_score = 0
        self.random_score = 0

    def print_title(self):
        print(Fore.GREEN, end="")
        print(text2art("Rock Paper Scissors!"))
        print(Fore.CYAN, end="")
        print("You have 6 rounds to beat the Ogre.")
        print("\nThe player with the most points after 6 rounds wins.")

    def print_results(self):
        print(Fore.CYAN+f"\n\tFinal score:\n\tPlayer: {self.player_score}\n\tComputer: {self.random_score}")

    def print_scoreboard(self):
        print(Fore.BLUE+"\n\n\tPlayer:"+Fore.CYAN+f" {self.player_score}"+Fore.BLUE+"\n\tOgre: "+Fore.CYAN+f"{self.random_score}\n")

    def play_game(self):
        self.print_title()
        for i in range(6):
            while True:
                print(Fore.CYAN+"\nChoose rock, paper, or scissors: "+Fore.GREEN, end="")
                player_choice = input().lower()
                if player_choice in self.options:
                    break
                print(Fore.RED+"\nInvalid choice. Try again.")
            os.system("clear" if os.name == "posix" else "cls")
            print(text2art(f"Round  {i+1}"))
            random_choice = random.choice(self.options)

            # Player Wins
            if player_choice == "rock" and random_choice == "rock":
                print("\nYou pick up a rock and throw it at the Ogre.")
                print("\nThe Ogre picks up a rock and throws it at you.")
                print("\nThe rocks cancel each other out - It's a tie.")
                self.player_score += 1
                self.random_score += 1

            elif player_choice == "rock" and random_choice == "scissors":
                print("\nYou pick up a rock and throw it at the Ogre.")
                print("\nThe Ogre tries to defend himself with a pair of scissors.")
                print("\nRock smashes scissors - You Win!")
                self.player_score += 1

            elif player_choice == "rock" and random_choice == "paper":
                print("\nYou pick up a rock and throw it at the Ogre.")
                print("\nThe Ogre catches the rock in a large sheet of reinforced paper and hurls it back at you.")
                print("\nPaper beats rock - You Lose!")
                self.random_score += 1

            elif player_choice == "scissors" and random_choice == "paper":
                print("\nYou attack the Ogre with a pair of scissors.")
                print("\nThe Ogre tries to defend himself with a sheet of paper.")
                print("\nScissors slices paper - You Win!")
                self.player_score += 1
            
            elif player_choice == "scissors" and random_choice == "scissors":
                print("\nYou attack the Ogre with a pair of scissors.")
                print("\nThe Ogre defends himself with a pair of scissors.")
                print("\nThe scissors cancel each other out. It's a Tie!")
                self.player_score += 1
                self.random_score += 1

            elif player_choice == "scissors" and random_choice == "rock":
                print("\nYou attack the Ogre with a pair of scissors.")
                print("\nThe Ogre hurls a giant rock at you.")
                print("\nRock crushes scissors - You Lose!")
                self.random_score += 1
            
            elif player_choice == "paper" and random_choice == "rock":
                print("\nYou throw a large stack of A4 paper at the Ogre.")
                print("\nThe Ogre tries to defend himself with a rock.")
                print("\nPaper overpowers rock. You Win!")
                self.random_score += 1

            elif player_choice == "paper" and random_choice == "paper":
                print("\nYou throw a large stack of A4 paper at the Ogre.")
                print("\nThe Ogre throws some A4 paper back at you.")
                print("\nPaper cancels out paper. It's a tie.")
                self.player_score += 1
                self.random_score += 1
            
            elif player_choice == "paper" and random_choice == "scissors":
                print("\nYou throw a large stack of A4 paper at the Ogre.")
                print("\nThe Ogre cuts up all the pieces of paper.")
                print("\nScissors beats paper. You Lose!")
                self.random_score += 1
            self.print_scoreboard()
            
        if self.player_score > self.random_score:
            # Player wins
            return 1
        elif self.player_score == self.random_score:
            # Its a tie
            return 2
        else:
            # Player lost
            return 3



if __name__ == '__main__':
    game = RPS()
    game.play_game()
