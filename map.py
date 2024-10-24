import msvcrt
import keyboard
import random
import json
from colorama import Fore, Back

from items import wepons

foot = f"{Fore.WHITE}#"
moution = f"{Back.LIGHTBLACK_EX}{Fore.WHITE}#{Back.RESET}"
ENEMY_SET = (f"{Fore.RED}B{Fore.RESET}")  
EXIT = f"{Fore.GREEN}E{Fore.RESET}"

def map(x : int, y : int, canvas : tuple, type_map : str, name : str) -> list:
    map = []
    for i in range(canvas[1]):
        arr = []
        for j in range(canvas[0]):
            arr.append(" ")
        map.append(arr)
    
    Y = 0
    for i in map:
        if type_map == "WORLD":
            blocks = (f"{Fore.GREEN} {Fore.WHITE}", f"{Fore.GREEN} {Fore.WHITE}", f"{Fore.GREEN}'{Fore.WHITE}", f"{Fore.GREEN},{Fore.WHITE}")
        if type_map == "DUNGEN":
            blocks = (f"{Back.LIGHTBLACK_EX}{Fore.WHITE}#{Back.RESET}", f"{Back.LIGHTBLACK_EX}{Fore.WHITE}#{Back.RESET}")
            
        X = 0
        if Y < y:
            for j in i:
                if X < x:
                    map[Y][X] = random.choice(blocks)
                X += 1
        Y += 1
        
    if type_map == "WORLD":    
        for _ in range(round((x * y) / 20)):
            r_y = random.randint(1, y - 1)
            r_x = random.randint(1, x - 1)

            try:
                if map[r_y][r_x + 1] != moution and map[r_y][r_x - 1] != moution and map[r_y + 1][r_x] != moution and map[r_y - 1][r_x] != moution:
                    map[r_y][r_x + 1] = foot
                    map[r_y][r_x - 1] = foot
                    map[r_y + 1][r_x] = foot
                    map[r_y - 1][r_x] = foot
                    map[r_y][r_x] = moution
            except:
                pass
            
    if type_map == "DUNGEN":
        derections = ("R", "D", "L", "U")
        last_pos = [0, 0]
        dungen_len= 0
        last_derection = ""
        C_A = [f"{Fore.LIGHTBLACK_EX}.{Fore.RESET}", f"{Fore.WHITE}.{Fore.RESET}"]
        clear_aria = random.choice(C_A)
        map[last_pos[0]][last_pos[1]] = clear_aria
        while dungen_len <= round((x * y) / 5):
            clear_aria = random.choice(C_A)
            try:
                #print(last_pos)
                derection = random.choice(derections)
                if derection == "R" and last_pos[0] < x - 1 and last_derection != "L":
                    map[last_pos[1]][last_pos[0] + 1] = clear_aria
                    last_pos = [last_pos[0] + 1, last_pos[1]]
                    dungen_len += 1
                    
                if derection == "D" and last_pos[1] < y - 1 and last_derection != "U":
                    map[last_pos[1]+1][last_pos[0]] = clear_aria
                    last_pos = [last_pos[0], last_pos[1] + 1]
                    dungen_len += 1

                if derection == "L" and last_pos[0] - 1 > 0 and last_derection != "R":
                    map[last_pos[1]][last_pos[0] - 1] = clear_aria
                    last_pos = [last_pos[0] - 1, last_pos[1]]
                    dungen_len += 1
                    
                if derection == "U" and last_pos[1] - 1 > 0 and last_derection != "D":
                    map[last_pos[1]-1][last_pos[0]] = clear_aria
                    last_pos = [last_pos[0], last_pos[1] - 1]
                    dungen_len += 1
                last_derection = derection                    
            except:
                pass
        Y=0
        PROCENTAGE = 50    
        CD_ENAMY = 5
        for i in map:
            if Y <= y:
                X=0
                for j in i:
                    r = random.randint(1, 100)
                    if CD_ENAMY < 0:
                        CD_ENAMY = 5
                        
                    if X <= x and map[Y][X] in C_A:
                        CD_ENAMY -= 1
                        if r <= PROCENTAGE and CD_ENAMY == 1:
                            map[Y][X] = f"{Fore.RED}B{Fore.RESET}"
                            PROCENTAGE -= 5
                        
                    X+=1
            Y+=1
        map[0][0] = f"{Fore.WHITE}.{Fore.RESET}"
        map[0][1] = f"{Fore.WHITE}.{Fore.RESET}"
        map[1][0] = f"{Fore.WHITE}.{Fore.RESET}"
        map[1][1] = f"{Fore.WHITE}.{Fore.RESET}"
        map[last_pos[1]][last_pos[0]] = f"{Fore.GREEN}E{Fore.RESET}"
                        
    data = {}
    data["map"] = map
    data["scren"] = canvas
    data["map_x"] = x
    data["map_y"] = y
    
    
    # сохраняем словарь с информацией в фаил соответствующий айди пользователя
    with open(f"{name}.json", 'w', encoding="utf-8") as file:
        json.dump(data, file, indent=1)
    return map