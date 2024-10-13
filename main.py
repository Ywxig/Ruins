import msvcrt
import keyboard
import random
import json
from colorama import Fore, Back
from colorama import just_fix_windows_console

foot = f"{Fore.WHITE}#"
moution = f"{Back.LIGHTBLACK_EX}{Fore.WHITE}#{Back.RESET}"

def CMD(command : list):
    if command[0] == "quit":
        return "quit"
    if command[0] == "go":
        return "go on"

def drow(map_ : list, hero_pos : tuple) -> None:
    M = map_
    M[hero_pos[1]][hero_pos[0]] = f"{Fore.CYAN}@{Fore.WHITE}"
    arr = []
    for i in M:
        arr.append("".join(i))
    print("\n".join(arr))


def map(x : int, y : int, canvas : tuple, type_map : str) -> list:
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
    
    # сохраняем словарь с информацией в фаил соответствующий айди пользователя
    with open("save.json", 'w', encoding="utf-8") as file:
        json.dump(data, file, indent=1)
    return map




scrin = (196, 50)
map_x = 50
map_y = 40
map(map_x, map_y, scrin, "DUNGEN")
file_ = open("save.json", "r", encoding="utf-8").read()

        
def main():
    x_p = 0
    y_p = 0
    mod = "no_cmd"
    while True:
        
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
            

if __name__ == "__main__":
    just_fix_windows_console()
    main()

