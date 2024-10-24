import msvcrt
import keyboard
import random
import json
from colorama import Fore, Back
from events import Event
from map import map

CFG = open(f"cfg.json", "r", encoding="utf-8").read()
CFG = json.loads(CFG)  

foot = f"{Fore.WHITE}#"
moution = f"{Back.LIGHTBLACK_EX}{Fore.WHITE}#{Back.RESET}"
ENEMY_SET = (f"{Fore.RED}B{Fore.RESET}")
EXIT = f"{Fore.GREEN}E{Fore.RESET}"

def drow(map_ : list, hero_pos : tuple) -> None:
    M = map_
    M[hero_pos[1]][hero_pos[0]] = f"{Fore.CYAN}@{Fore.WHITE}"
    arr = []
    for i in M:
        arr.append("".join(i))
    print("\n".join(arr))

def game( name ):

  

    file_ = open(f"{name}.json", "r", encoding="utf-8").read()
    M = json.loads(file_)
    
    scrin = M["scren"]
    map_x = M["map_x"]
    map_y = M["map_y"]
    x_p = 0
    y_p = 0
    game_ = True
    mod = "no_cmd"
    while game_ == True:
        
        M = json.loads(file_)
        drow(map_ = M["map"], hero_pos = (x_p, y_p))
        if mod == "cmd":
            cmd = (input(">>>")).split()
            
            if cmd[0] == "quit":
                break
            
            if cmd[0] == "go":
                mod = "no_cmd"
            
        if mod == "no_cmd":
            print(">>>")
        

        
        
        
        key = msvcrt.getch()
        
        if key == b'w' and y_p > 0 and M["map"][y_p - 1][x_p] != moution:
            y_p -= 1
            
        if key == b'd' and x_p < map_x - 1 and M["map"][y_p][x_p + 1] != moution:
            x_p += 1
            
        if key == b'a' and x_p > 0 and M["map"][y_p][x_p - 1] != moution:
            x_p -= 1
            
        if key == b's' and y_p < map_y - 1 and M["map"][y_p + 1][x_p] != moution:
            y_p += 1   

        if key == b'q':
            mod = "cmd"
                        
        Y = 0
        for i in M["map"]:
            X = 0
            for j in i:
                if j == " ":
                    break
                if M["map"][Y][X] in ENEMY_SET and (x_p, y_p) == (X, Y):
                    Event.Battel()
                if M["map"][Y][X] in EXIT and (x_p, y_p) == (X, Y):
                    map(map_x, map_y, scrin, "DUNGEN", name)
                    game( name )
                    break
                X += 1
            Y+=1