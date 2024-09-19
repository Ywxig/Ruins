
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
        arr["race"] = r_race

        caracteristics = {}
        caracteristics["force"] = data["races"][r_race]["force"]
        caracteristics["intelect"] = data["races"][r_race]["intelect"]
        caracteristics["harizma"] = data["races"][r_race]["harizma"]
        caracteristics["movement"] = data["races"][r_race]["movement"]
        caracteristics["body"] = data["races"][r_race]["body"]
        caracteristics["wizart"] = data["races"][r_race]["wizart"]
        arr["caracteristics"] = caracteristics
        
        with open(f"caracters/{name}.json", 'w', encoding="utf-8") as file:
            json.dump(arr, file)
        return arr
    
class Edit:

    def name(name : str, ctx : str) -> None:
        file = open(f"caracters/{name}.json", "r", encoding="utf-8").read()
        arr = json.loads(file)
        arr["name"] = ctx
        with open(f"caracters/{name}.json", 'w', encoding="utf-8") as file:
            json.dump(arr, file)

    def race(name : str, ctx : str) -> None:
        file = open(config, "r", encoding="utf-8").read()
        data = json.loads(file)

        if ctx not in data["races"]["race_list"]:
            print(f"")
        else:
            file = open(f"caracters/{name}.json", "r", encoding="utf-8").read()
            arr = json.loads(file)
            arr["race"] = ctx

            arr["caracteristics"]["force"] = data["races"][ctx]["force"]
            arr["caracteristics"]["intelect"] = data["races"][ctx]["intelect"]
            arr["caracteristics"]["harizma"] = data["races"][ctx]["harizma"]
            arr["caracteristics"]["movement"] = data["races"][ctx]["movement"]
            arr["caracteristics"]["body"] = data["races"][ctx]["body"]
            arr["caracteristics"]["wizart"] = data["races"][ctx]["wizart"]         
            arr["mony"] = 5000

            with open(f"caracters/{name}.json", 'w', encoding="utf-8") as file:
                json.dump(arr, file)



