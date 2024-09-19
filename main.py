import keyboard
import world
import random
import json
from colorama import Fore, Back
import caracter

def game(game_name):
    #main llop of game!

    f = "saves/"+str(game_name)+'.json'

    file_ = open(f, "r", encoding="utf-8").read()
    data_ = json.loads(file_)

    print("Pass")

    while True:
        command = input(Fore.CYAN + "@: " + Fore.WHITE)

        if command == "me":
            for i in data_:
                try:
                    file_ = open(f"caracters/{i["player"]["name"]}.json", "r", encoding="utf-8").read()
                    data = json.loads(file_)
                    print(f"name: {data["name"]} \n$: {data["mony"]} \n•: {i["player"]["sys"]}")
                except:
                    pass
                
        

def main():
    while True:
        config = "cfg.json"
        file_ = open(config, "r", encoding="utf-8").read()
        data_ = json.loads(file_)
        print(data_["wellcome"])
        command = input(">>> ")

        if command.split()[0] == "/cm":
            world.map.global_map(command.split()[1])

        if command == "/sys":
            game_name = input(">>> ")
            f = "saves/"+str(game_name)+'.json'

            file_ = open(f, "r", encoding="utf-8").read()
            data_ = json.loads(file_)

            r_sys = random.choice(data_)

            for i in r_sys["ojects"]:
                print(i)

        if command.split()[0] == "options":
            file_ = open(config, "r", encoding="utf-8").read()
            data_ = json.loads(file_)

            if command.split()[1] == "help":
                print(data_["option_help"])
            else:
                try:
                    data_[command.split()[1]] == int(command.split()[2])
                except:
                    print("Извените но вы не можите влиеть на строковые пораметры игры!")
            with open(config, 'w', encoding="utf-8") as file:
                json.dump(data_, file)        

        if command.split()[0] == "start":
            cr = input(">>>Видите имя вашего персонажа")
            world.map.global_map(command.split()[1], cr_name = cr)
            print(f"Голактика готова к вашему приключению капитан! Голактика сохранина по имени { command.split()[1] }")
            game(game_name = command.split()[1])

        if command.split()[0] == "load":  
            game(game_name = command.split()[1])

        if command.split()[0] == "cr":  
            caracter.Create.Random_c(command.split()[1])

        if command.split()[0] == "edit":
            caracter.Edit.race(command.split()[1], command.split()[2])

if __name__ == "__main__":
    main()