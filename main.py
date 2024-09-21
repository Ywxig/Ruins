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
            i = data_[len(data_) - 1]

            file_ = open(f"caracters/{i["player"]["name"]}.json", "r", encoding="utf-8").read()
            data = json.loads(file_)
            print(f"name: {data["name"]} \n$: {data["mony"]} \n•: {i["player"]["sys"]}")


        if command == "help":
            config = "cfg.json"
            file_ = open(config, "r", encoding="utf-8").read()
            data = json.loads(file_)
            print(f"{data["game_comm_help"]}")

        if command == "sys":

            for i in data_:
                try:
                    file_ = open(f"caracters/{i["player"]["name"]}.json", "r", encoding="utf-8").read()
                    data = json.loads(file_)
                    plaer = i["player"]["sys"]
                except:
                    pass

            for i in data_:
                if i["system_name"] == plaer:
                    print(f"system: { i["system_name"] }\nobjects: { str(len(i["ojects"])) }\nname star: { i["star"]["name"] }")
                    break
            
        if command == "quit":
            break

                
        

def main():

    config = "cfg.json"
    file_ = open(config, "r", encoding="utf-8").read()
    data_ = json.loads(file_)
    print(data_["wellcome"])

    while True:
        
        command = input(">>> ")

        if command == "/sys":
            game_name = input(">>> ")
            f = "saves/"+str(game_name)+'.json'

            file_ = open(f, "r", encoding="utf-8").read()
            data_ = json.loads(file_)

            r_sys = random.choice(data_)

            for i in r_sys["ojects"]:
                print(i)

        if command.split()[0] == "start":
            cr = input(">>>Видите имя вашего персонажа ")
            world.map.global_map(command.split()[1], cr_name = cr)
            print(f"Голактика готова к вашему приключению капитан! Голактика сохранина по имени { command.split()[1] }")
            game(game_name = command.split()[1])

        if command.split()[0] == "load":  
            game(game_name = command.split()[1])

        if command.split()[0] == "showc":  
            caracter.Show.cerecter(command.split()[1])

        if command.split()[0] == "new":  
            caracter.Create.Random_c(command.split()[1])

        if command.split()[0] == "edit":
            if command.split()[2] == "-r":
                race = input(f">>>Введите новую рассу \" список расс { data_["races"]["race_list"] } \" для {command.split()[1]} ")
                caracter.Edit.race(command.split()[1], race)

            if command.split()[2] == "-d":
                desc = input(f">>>Введите новое описание для {command.split()[1]} ")
                caracter.Edit.description(command.split()[1], desc)

if __name__ == "__main__":
    main()