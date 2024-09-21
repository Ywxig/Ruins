
import json
import random
import math

config = "cfg.json"

class Create:

    def Random_c(name) -> dict:
        file = open(config, "r", encoding="utf-8").read()
        data = json.loads(file)

        r_race = random.choice(data["races"]["race_list"])

        arr = {}
        arr["name"] = name
        arr["mony"] = 5000
        arr["race"] = r_race
        arr["description"] = ""

        modifications = {}
        modifications["force"] = data["races"][r_race]["force"]
        modifications["intelect"] = data["races"][r_race]["intelect"]
        modifications["harizma"] = data["races"][r_race]["harizma"]
        modifications["movement"] = data["races"][r_race]["movement"]
        modifications["body"] = data["races"][r_race]["body"]
        modifications["wizart"] = data["races"][r_race]["wizart"]

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
        
        arr["modifications"] = modifications
        arr["caracteristics"] = caracteristics
        
        with open(f"caracters/{name}.json", 'w', encoding="utf-8") as file:
            json.dump(arr, file, indent=2)
        
        print(f"\nname: {arr["name"]} \nmony: {arr["mony"]} \nrace: {arr["race"]} \n\ncaracteristics: \n\tforce: {arr["caracteristics"]["force"]} \n\tintelect: {arr["caracteristics"]["intelect"]} \n\tharizma: {arr["caracteristics"]["harizma"]}  \n\tmovement: {arr["caracteristics"]["movement"]} \n\tbody: {arr["caracteristics"]["body"]} \n\twizart: {arr["caracteristics"]["wizart"]} \n\nmodifications: \n\tforce: {arr["modifications"]["force"]} \n\tintelect: {arr["modifications"]["intelect"]} \n\tharizma: {arr["modifications"]["harizma"]}  \n\tmovement: {arr["modifications"]["movement"]} \n\tbody: {arr["modifications"]["body"]} \n\twizart: {arr["modifications"]["wizart"]}")

class Show:

    def cerecter(name : str) -> None:
        file = open(f"caracters/{name}.json", "r", encoding="utf-8").read()
        arr = json.loads(file)        
        print(f"\nname: {arr["name"]} \nmony: {arr["mony"]} \nrace: {arr["race"]} \n\ncaracteristics: \n\tforce: {arr["caracteristics"]["force"]} \n\tintelect: {arr["caracteristics"]["intelect"]} \n\tharizma: {arr["caracteristics"]["harizma"]}  \n\tmovement: {arr["caracteristics"]["movement"]} \n\tbody: {arr["caracteristics"]["body"]} \n\twizart: {arr["caracteristics"]["wizart"]} \n\nmodifications: \n\tforce: {arr["modifications"]["force"]} \n\tintelect: {arr["modifications"]["intelect"]} \n\tharizma: {arr["modifications"]["harizma"]}  \n\tmovement: {arr["modifications"]["movement"]} \n\tbody: {arr["modifications"]["body"]} \n\twizart: {arr["modifications"]["wizart"]}")
        

class Edit:

    def name(name : str, ctx : str) -> None:
        file = open(f"caracters/{name}.json", "r", encoding="utf-8").read()
        arr = json.loads(file)
        arr["name"] = ctx
        with open(f"caracters/{name}.json", 'w', encoding="utf-8") as file:
            json.dump(arr, file, indent=2)

    def description(name : str, ctx : str) -> None:
        file = open(f"caracters/{name}.json", "r", encoding="utf-8").read()
        arr = json.loads(file)
        arr["description"] = ctx
        with open(f"caracters/{name}.json", 'w', encoding="utf-8") as file:
            json.dump(arr, file, indent=2)

    def race(name : str, ctx : str) -> None:
        file = open(config, "r", encoding="utf-8").read()
        data = json.loads(file)

        if ctx not in data["races"]["race_list"]:
            print(f"")
        else:
            file = open(f"caracters/{name}.json", "r", encoding="utf-8").read()
            arr = json.loads(file)

            modifications = {}
            modifications["force"] = data["races"][ctx]["force"]
            modifications["intelect"] = data["races"][ctx]["intelect"]
            modifications["harizma"] = data["races"][ctx]["harizma"]
            modifications["movement"] = data["races"][ctx]["movement"]
            modifications["body"] = data["races"][ctx]["body"]
            modifications["wizart"] = data["races"][ctx]["wizart"]

            arr["race"] = ctx

            arr["modifications"] = modifications

            with open(f"caracters/{name}.json", 'w', encoding="utf-8") as file:
                json.dump(arr, file, indent=2)



