import copy
import os
from colorama import Fore, Style
print(Style.BRIGHT)
class TowerOfHanoi:
    def __init__(self, disk_size):
        self.max_disk_size = disk_size
        self.completed_tower = list(range(self.max_disk_size,0,-1))
        self.towers = {'A':copy.copy(self.completed_tower), 'B':[], 'C':[]}
    
    def input_instructions(self):
        print(Fore.RED+"\n\tIncorrect Value Entered!!!")
        print(Fore.CYAN+"\nEnter the letter of the tower you want to move the disk from followed by the letter of the tower you want to move the disk to.")
        print("\n\tExample:\n\t\t"+Fore.GREEN+"ab"+Fore.CYAN+" - to move disk from tower a to tower b.")
        print(Fore.GREEN+"\t\tac"+Fore.CYAN+" - to move disk from tower a to tower c.")
        print(Fore.CYAN+"\nNote:\n\t"+Fore.GREEN+"- Inputs are not case sensitive\n\t- No whitespaces in between the letters\n\n"+Fore.RED+"-"*145)
    
    def display_disk(self, width):
        emptySpace = " " * (self.max_disk_size - width) 
        if width == 0:
            print(f"\t{emptySpace}||{emptySpace}",end="")
        else:
            disk = '#'*width
            numLabel = str(width).rjust(2,"_")
            print(f"\t{emptySpace}{disk}{numLabel}{disk}{emptySpace}",end="")
       
    def printer(self):
        print(Fore.GREEN)
        for i in range(self.max_disk_size, -1, -1):
            for tower in (self.towers["A"], self.towers["B"], self.towers["C"]):
                if i >= len(tower):
                    self.display_disk(0)
                else:
                    self.display_disk(tower[i])
            print()
        emptySpace = " " * self.max_disk_size
        print(Fore.GREEN+"\t{0} A{0}\t{0} B{0}\t{0} C{0}".format(emptySpace))
        print()
    
    def player_move(self):
        while True:
            self.printer() 
            try:
                options = ["AB", "AC", "BA","BC","CA","CB"] 
                response = input(Fore.CYAN+"Move disk from which tower to which tower? (A - B - C)\n\nEnter"+Fore.RED+ " forfeit "+Fore.CYAN+"to give up.\n\n>>> ").upper().strip()
                os.system("clear" if os.name == "posix" else "cls")
                if response == "FORFEIT":
                    return "forfeit"
                if response not in options:
                    self.input_instructions()
                    continue
                else:
                    f_tower, t_tower = response[0], response[1]
                    from_tower = self.towers[f_tower.upper()]
                    to_tower = self.towers[t_tower.upper()] 
                    if not from_tower:
                        print(Fore.RED+"\n\tInvalid Move!!!")
                        print(Fore.CYAN+"\nThere are no disks to move on that tower.\n")
                        continue
                    if to_tower and from_tower[-1] > to_tower[-1]:
                        print(Fore.RED+"\n\tInvalid Move!!!")
                        print(Fore.CYAN+"\nYou cannot place a larger disk on top of a smaller disk.")
                        print("\nNote the number in the middle of the disk indicates the disk's size.\n")
                        continue
                    else:
                        return (from_tower, to_tower)
            except ValueError:
                self.input_instructions()
 
    def start_game(self):
        while True:
            if self.towers["C"] == self.completed_tower:
                self.printer()
                return 1
            response = self.player_move()
            if response == "forfeit":
                return 2
            from_tower, to_tower = response
            to_tower.append(from_tower.pop())
    
if __name__ == '__main__':
    new_game = TowerOfHanoi(3)
    new_game.start_game()