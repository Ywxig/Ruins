import msvcrt
import keyboard
import random
import json

from events import Event
from game import game
from map import map
from items import wepons

from colorama import Fore, Back
from colorama import just_fix_windows_console

foot = f"{Fore.WHITE}#"
moution = f"{Back.LIGHTBLACK_EX}{Fore.WHITE}#{Back.RESET}"
ENEMY_SET = (f"{Fore.RED}B{Fore.RESET}")    

def modificator(a) -> int:
    if a in [8, 9]:
        return -1
    if a in [10, 11]:
        return 0
    if a in [12, 13]:
        return 1
    if a in [14, 15]:
        return 2

def CMD():
    while True:
        cmd = (input(">>> ")).split()    
        if cmd[0] == "wp":
            print(wepons.make())

        if cmd[0] == "get":
            file_ = open(f"{cmd[1]}.json", "r", encoding="utf-8").read()
            SAVE = json.loads(file_)
            
            print(SAVE["wapons"][int(cmd[2])])            
        
        if cmd[0] == "quit":
            break



def roll_new_ch(name:str, race:str, save:str) -> dict:
    
    CFG = open(f"cfg.json", "r", encoding="utf-8").read()
    cfg = json.loads(CFG)
    
    file_ = open(f"{save}.json", "r", encoding="utf-8").read()
    SAVE = json.loads(file_)
    
    ch = {}
    ch["name"] = name
    ch["level"] = 0
    ch["race"] = race
    fe = {}
    list_of_fe = [ 15, 14, 13, 12, 10, 8 ]
    
    fe["force"] = random.choice(list_of_fe)
    list_of_fe.remove(fe["force"])
    
    fe["wisdom"] = random.choice(list_of_fe)
    list_of_fe.remove(fe["wisdom"])
    
    fe["intellect"] = random.choice(list_of_fe)
    list_of_fe.remove(fe["intellect"])
    
    fe["physique"] = random.choice(list_of_fe)
    list_of_fe.remove(fe["physique"])
    
    fe["dexterity"] = random.choice(list_of_fe)
    list_of_fe.remove(fe["dexterity"])
    
    ch["feature"] = fe
    
    modifications = {}
    modifications["force"] = cfg["races"][race]["modificators"]["force"] + modificator(fe["force"])
    modifications["intellect"] = cfg["races"][race]["modificators"]["intellect"] + modificator(fe["intellect"])
    modifications["dexterity"] = cfg["races"][race]["modificators"]["dexterity"] + modificator(fe["dexterity"])
    modifications["physique"] = cfg["races"][race]["modificators"]["physique"] + modificator(fe["physique"])
    modifications["wisdom"] = cfg["races"][race]["modificators"]["wisdom"] + modificator(fe["wisdom"])
    
    ch["modifications"] = modifications
    
    ch["wepon"] = wepons.craft("wood", "sword")
    
    SAVE["ch"] = ch
    with open(f"{save}.json", 'w', encoding="utf-8") as file:
        json.dump(SAVE, file, indent=1)
        
    return ch

def main():
    CFG = open(f"cfg.json", "r", encoding="utf-8").read()
    cfg = json.loads(CFG)
    print(cfg["start_words"])
    while True:
        cmd = (input(">>> ")).split()
        if cmd[0] == "start":
            scrin = cfg["scrin"]
            map_x = cfg["map_x"]
            map_y = cfg["map_y"]
            map(map_x, map_y, scrin, "DUNGEN", cmd[1])
            game( cmd[1] )
        
        if cmd[0] == "cr":
             roll_new_ch(cmd[2], cmd[3], cmd[1])

        if cmd[0] == "test":
            CMD()
             
        if cmd[0] == "load":
            game( cmd[1] )
        
        if cmd[0] == "quit":
            break

if __name__ == "__main__":
    just_fix_windows_console()
    main()

