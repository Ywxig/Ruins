import json
import random
import math

const_SB = 5.67 * (10 ** -8) 
L_sun = 3.828 * (10 ** 26)


'''
#1 - пустой блок
#2 - астероид


#10 - планета
#20 - скопление астеройдов
#30 - космическая база
'''

class map:

    class gen:

        def Star() -> dict:
            star = {}
            star["radius"] = random.randint(70_000, 1_000_000) #Km
            star["teperatur"] = random.randint(4_000, 30_000) #K
            star["L"] = 4*math.pi*((2*star["radius"]) ** 2) * const_SB*(star["teperatur"] ** 4) #Lu
            star["mass"] = (star["L"]/L_sun) ** 1/3.5 #Kg
            return star

        def Objects(Objects : int, Obj_typs : dict) -> dict:
            """
            Objects - Деопозон жилаемых обектов
            Obj_typs - Типы обектов
            """
            names = Obj_typs["name"]
            arr = []
            for _ in range(random.randint(2, Obj_typs["objects"])):
                type_Obj = random.choice(Obj_typs["types"])
                if type_Obj == "Planet":
                    obj = {}
                    obj["name"] = random.choice(names)
                    obj["type"] = type_Obj
                    obj["radius"] = random.randint(250, 140_000)
                    obj["ro"] = random.randint(4000, 7000) #kg/m3
                    obj["mass"] = (4/3) * math.pi * (obj["radius"] * 4) * obj["ro"]

                if type_Obj == "Station":
                    obj = {}
                    obj["name"] = random.choice(names)
                    obj["type"] = type_Obj
                    obj["heght"] = random.randint(100, 1000)
                    obj["size"] = obj["heght"] ** 3
                    obj["population"] = obj["size"] / random.randint(30, 60)

                if type_Obj == "Factory":
                    obj = {}
                    obj["name"] = random.choice(names)
                    obj["type"] = type_Obj
                    obj["heght"] = random.randint(10, 100)
                    obj["size"] = obj["heght"] ** 3
                    obj["population"] = obj["size"] / random.randint(30, 60)

                arr.append(obj)
                names.remove(obj["name"])
            return arr

    def global_map(name_save, config = "cfg.json"):
        file_ = open(config, "r", encoding="utf-8").read()
        data_ = json.loads(file_)

        f = "saves/"+str(name_save)+'.json'

        data = {}
        systems = []

        names = data_["system_name"]

        for _ in range(data_["systems_count"]):
            system = {}
            
            system["star"] = map.gen.Star()
            system["ojects"] = map.gen.Objects(Objects = random.randint(5, 10), Obj_typs = data_)
            
            system["system_name"] = random.choice(names)
            system["id"] = ""

            system["links"] = []

            

            
            systems.append(system)
            
            data[system["system_name"]] = systems
            names.remove(system["system_name"])
            
        r_sys = random.choice(systems)
        player = {"player" : {"sys":r_sys["system_name"],"mony":5000,"ship" : data_["ships"]["Milan"]}}
        systems.append(player)

        # сохраняем словарь с информацией в фаил соответствующий айди пользователя
        with open(f, 'w', encoding="utf-8") as file:
            json.dump(systems, file)

    def draw(x, y):
        pass

    def locator(x, y) -> dict:
        pass

class move:
    pass

class use:
    pass