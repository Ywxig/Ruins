
import json
import random
import math

config = "cfg.json"

def wepons(w : dict) -> list:
    arr = []
    try:
        for i in w:
            arr.append(i["name"])
        return arr
    except:
        return []

def modificator(a) -> int:
    if a in [8, 9]:
        return -1
    if a in [10, 11]:
        return 0
    if a in [12, 13]:
        return 1
    if a in [14, 15]:
        return 2
    
class Create:
    
    def choise_idea(mod : dict, race : str) -> str:
        
        if mod["force"] + mod["harizma"] > 2:
            return "facism"
        
        if mod["intelect"] + mod["harizma"] > 2:
            return "liberalism"
        
        if mod["intelect"] + mod["harizma"] > 2:
            return "communism"
        else:
            return "dimocracy"
    def leder(races : list) -> dict:
        file = open(config, "r", encoding="utf-8").read()
        data = json.loads(file)
        
        r_race = random.choice(races)
        
        arr = {}
        modifications = {}
        modifications["force"] = data["races"][r_race]["force"]
        modifications["intelect"] = data["races"][r_race]["intelect"]
        modifications["harizma"] = data["races"][r_race]["harizma"]
        modifications["movement"] = data["races"][r_race]["movement"]
        modifications["body"] = data["races"][r_race]["body"]
        modifications["wizart"] = data["races"][r_race]["wizart"]
        
        arr["modifications"] = modifications
        arr["race"] = r_race
        arr["hp"] = 10 + modifications["body"]
        arr["ac"] = 10 + modifications["movement"]
        
        arr["idea"] = Create.choise_idea(modifications, arr["race"])
        
        arr["name"] = random.choice(data["races"][r_race]["names"]) + " " + random.choice(data["lastname_list"])        
        return arr
    
    def simply_c() -> dict:
        file = open(config, "r", encoding="utf-8").read()
        data = json.loads(file)
        
        r_race = random.choice(data["races"]["race_list"])
        
        arr = {}
        modifications = {}
        modifications["force"] = data["races"][r_race]["force"]
        modifications["intelect"] = data["races"][r_race]["intelect"]
        modifications["harizma"] = data["races"][r_race]["harizma"]
        modifications["movement"] = data["races"][r_race]["movement"]
        modifications["body"] = data["races"][r_race]["body"]
        modifications["wizart"] = data["races"][r_race]["wizart"]
        
        arr["modifications"] = modifications
        
        arr["hp"] = 10 + modifications["body"]
        arr["ac"] = 10 + modifications["movement"]
        
        arr["race"] = r_race
        
        arr["name"] = random.choice(data["races"][r_race]["names"]) + " " + random.choice(data["lastname_list"])        
        return arr
    
    def Random_c(name) -> dict:
        file = open(config, "r", encoding="utf-8").read()
        data = json.loads(file)

        r_race = random.choice(data["races"]["race_list"])
        r_class = random.choice(data["class"]["list"])

        

        arr = {}
        arr["name"] = name
        arr["mony"] = 5000
        arr["race"] = r_race
        arr["description"] = ""
        arr["lavel"] = 1
        arr["proficiency"] = 2
        arr["size"] = random.randint(data["races"][r_race]["size"][0], data["races"][r_race]["size"][1])
        arr["ownership"] = data["class"][r_class]["ownership"]
        arr["skills"] = data["class"][r_class]["skills"]
        arr["inventory"] = {}
        arr["class"] = r_class

        list_of_characteristics = [ 15, 14, 13, 12, 10, 8 ]

        caracteristics = {}
        caracteristics["force"] = random.choice(list_of_characteristics)
        list_of_characteristics.remove(caracteristics["force"])
        caracteristics["intelect"] = random.choice(list_of_characteristics)
        list_of_characteristics.remove(caracteristics["intelect"])
        caracteristics["harizma"] = random.choice(list_of_characteristics)
        list_of_characteristics.remove(caracteristics["harizma"])
        caracteristics["movement"] = random.choice(list_of_characteristics)
        list_of_characteristics.remove(caracteristics["movement"])
        caracteristics["body"] = random.choice(list_of_characteristics)
        list_of_characteristics.remove(caracteristics["body"])
        caracteristics["wizart"] = random.choice(list_of_characteristics)
        list_of_characteristics.remove(caracteristics["wizart"])
        
        modifications = {}
        modifications["force"] = data["races"][r_race]["force"] + modificator(caracteristics["force"])
        modifications["intelect"] = data["races"][r_race]["intelect"] + modificator(caracteristics["intelect"])
        modifications["harizma"] = data["races"][r_race]["harizma"] + modificator(caracteristics["harizma"])
        modifications["movement"] = data["races"][r_race]["movement"] + modificator(caracteristics["movement"])
        modifications["body"] = data["races"][r_race]["body"] + modificator(caracteristics["body"])
        modifications["wizart"] = data["races"][r_race]["wizart"] + modificator(caracteristics["wizart"])

        arr["modifications"] = modifications
        arr["caracteristics"] = caracteristics

        arr["hp"] = 10 + modifications["body"]
        arr["ac"] = 10 + modifications["movement"]
        
        with open(f"caracters/{name}.json", 'w', encoding="utf-8") as file:
            json.dump(arr, file, indent=2)
        
        print(f"\nname: {arr["name"]}\nclass: {arr["class"]}\nsize: {arr["size"]}\nHP: {arr["hp"]}\narmor class: {arr['ac']}\nownership: {arr["ownership"]}\nskills: {arr["skills"]}\n\ndescription: {arr['description']} \n\nmony: {arr["mony"]} \nrace: {arr["race"]} \nlavel: {arr["lavel"]}\nproficiency: {arr["proficiency"]} \n\ncaracteristics: \n\tforce: {arr["caracteristics"]["force"]} \n\tintelect: {arr["caracteristics"]["intelect"]} \n\tharizma: {arr["caracteristics"]["harizma"]}  \n\tmovement: {arr["caracteristics"]["movement"]} \n\tbody: {arr["caracteristics"]["body"]} \n\twizart: {arr["caracteristics"]["wizart"]} \n\nmodifications: \n\tforce: {arr["modifications"]["force"]} \n\tintelect: {arr["modifications"]["intelect"]} \n\tharizma: {arr["modifications"]["harizma"]}  \n\tmovement: {arr["modifications"]["movement"]} \n\tbody: {arr["modifications"]["body"]} \n\twizart: {arr["modifications"]["wizart"]}\ninventory: { wepons(arr["inventory"]) }")

class Show:

    def cerecter(name : str) -> None:
        file = open(f"caracters/{name}.json", "r", encoding="utf-8").read()
        arr = json.loads(file)        
        print(f"\nname: {arr["name"]}\nclass: {arr["class"]}\nsize: {arr["size"]}\nHP: {arr["hp"]}\narmor class: {arr['ac']}\nownership: {arr["ownership"]}\nskills: {arr["skills"]}\n\ndescription: {arr['description']} \n\nmony: {arr["mony"]} \nrace: {arr["race"]} \nlavel: {arr["lavel"]}\nproficiency: {arr["proficiency"]} \n\ncaracteristics: \n\tforce: {arr["caracteristics"]["force"]} \n\tintelect: {arr["caracteristics"]["intelect"]} \n\tharizma: {arr["caracteristics"]["harizma"]}  \n\tmovement: {arr["caracteristics"]["movement"]} \n\tbody: {arr["caracteristics"]["body"]} \n\twizart: {arr["caracteristics"]["wizart"]} \n\nmodifications: \n\tforce: {arr["modifications"]["force"]} \n\tintelect: {arr["modifications"]["intelect"]} \n\tharizma: {arr["modifications"]["harizma"]}  \n\tmovement: {arr["modifications"]["movement"]} \n\tbody: {arr["modifications"]["body"]} \n\twizart: {arr["modifications"]["wizart"]}\ninventory: { wepons(arr["inventory"]) }")
        

class Edit:

    def size(name : str, ctx : str) -> None:
        file = open(f"caracters/{name}.json", "r", encoding="utf-8").read()
        arr = json.loads(file)
        arr["size"] = int(ctx)
        with open(f"caracters/{name}.json", 'w', encoding="utf-8") as file:
            json.dump(arr, file, indent=2)
        print(f"Рост успешно изменнён")

    def inventory(name : str, ctx : str) -> None:
        file = open(f"caracters/{name}.json", "r", encoding="utf-8").read()
        arr = json.loads(file)

        fi = open(f"cfg.json", "r", encoding="utf-8").read()
        cfg = json.loads(fi)

        inv = []

        for i in ctx.split(","):
            if i in cfg["items"]:
                inv.append(cfg["items"][i])
                arr["inventory"] = ctx.split(",")
            else:
                print(f"Извените, похоже что { i } нет в списке допустимого снарежения, возможно вы неправельно написали названия предмета или его нет в файле конфига!")
        
        arr["inventory"] = inv
        with open(f"caracters/{name}.json", 'w', encoding="utf-8") as file:
            json.dump(arr, file, indent=2)
        print(f"Новый список снарежения добавлен")

    def name(name : str, ctx : str) -> None:
        file = open(f"caracters/{name}.json", "r", encoding="utf-8").read()
        arr = json.loads(file)
        arr["name"] = ctx
        with open(f"caracters/{name}.json", 'w', encoding="utf-8") as file:
            json.dump(arr, file, indent=2)
        print(f"Имя успешно заменено")

    def description(name : str, ctx : str) -> None:
        file = open(f"caracters/{name}.json", "r", encoding="utf-8").read()
        arr = json.loads(file)
        arr["description"] = ctx
        with open(f"caracters/{name}.json", 'w', encoding="utf-8") as file:
            json.dump(arr, file, indent=2)
        print(f"Описание успешно изменено")

    def race(name : str, ctx : str) -> None:
        file = open(config, "r", encoding="utf-8").read()
        data = json.loads(file)

        if ctx not in data["races"]["race_list"]:
            print(f"")
        else:
            file = open(f"caracters/{name}.json", "r", encoding="utf-8").read()
            arr = json.loads(file)

            caracteristics = arr["caracteristics"]

            modifications = {}
            modifications["force"] = data["races"][ctx]["force"] + modificator(caracteristics["force"])
            modifications["intelect"] = data["races"][ctx]["intelect"] + modificator(caracteristics["intelect"])
            modifications["harizma"] = data["races"][ctx]["harizma"] + modificator(caracteristics["harizma"])
            modifications["movement"] = data["races"][ctx]["movement"] + modificator(caracteristics["movement"])
            modifications["body"] = data["races"][ctx]["body"] + modificator(caracteristics["body"])
            modifications["wizart"] = data["races"][ctx]["wizart"] + modificator(caracteristics["wizart"])

            arr["race"] = ctx

            arr["modifications"] = modifications

            with open(f"caracters/{name}.json", 'w', encoding="utf-8") as file:
                json.dump(arr, file, indent=2)



