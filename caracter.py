import json
import random
import math

config = "cfg.json"

class Create:

    def Random_c() -> dict:
        file = open(config, "r", encoding="utf-8").read()
        data = json.loads(file)

        r_race = data["races"]["race_list"]


        arr = {}
        arr["dmg"] = random.choice(data["race"][random.choice(r_race)]["dmg"])
        arr["hp"] = random.choice(data["race"][r_race]["hp"])
        arr["ac"] = random.choice(data["race"][r_race]["ac"])
        

        return data

    def New(name : str,
            race : str) -> dict:
        """
        name - name lol
        """

        file = open(config, "r", encoding="utf-8").read()
        data = json.loads(file)

        data["name"] = name
        data["caractersitics"] = {}

        # сохраняем словарь с информацией в фаил соответствующий айди пользователя
        #with open(f, 'w', encoding="utf-8") as file:
        #    json.dump(data, file)

print(Create.Random_c())



