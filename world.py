import json
import random
import math
import caracter
from colorama import Fore

sigma = 5.67 * (10 ** -8) 
L_sun = 3.828 * (10 ** 26)


'''
#1 - пустой блок
#2 - астероид


#10 - планета
#20 - скопление астеройдов
#30 - космическая база

'''

class get:
    def conditions(event_name : str):
        file_ = open("cfg.json", "r", encoding="utf-8").read()
        cfg = json.loads(file_)
        
        arr = []
        
        for i in cfg["history"][event_name]["conditions"]:
            arr.append(i)
        return i
            

class map:

    class gen:
        
        def city(name : str, races : list) -> dict:
            
            file_ = open("cfg.json", "r", encoding="utf-8").read()
            cfg = json.loads(file_)
            
            arr = {}
            arr["name"] = name
            
            arr["buildings"] = []
            arr["leder"] = caracter.Create.leder(races)
            arr["idea"] = arr["leder"]["idea"]
            arr["tension"] = cfg["ideas"][arr["idea"]]['bafs']["tension"]
            arr["support alliance"] = cfg["ideas"][arr["idea"]]['bafs']["support alliance"]
            arr["support war"] = cfg["ideas"][arr["idea"]]['bafs']["support war"]
            arr["support industry"] = cfg["ideas"][arr["idea"]]['bafs']["support industry"]
            return arr
        
        def ores():
            file_ = open("cfg.json", "r", encoding="utf-8").read()
            data_ = json.loads(file_)
            
            arr = []
            
            for _ in range(random.randint(1, len(data_["materials"]["list"]))):
                arr.append(random.choice(data_["materials"]["list"]))

            return arr
        def Star() -> dict:
            
            star = {}
            star["radius"] = random.randint(70_000, 1_000_000) #Km
            star["teperatur"] = random.randint(4_000, 30_000) #K
            star["L"] = 4*math.pi*((2*star["radius"]) ** 2) * sigma*(star["teperatur"] ** 4) #Lu
            star["mass"] = (star["L"]/L_sun) ** 1/3.5 #Kg
            star["name"] = random.choice(["Lumina", "Aetheris", "Noxara", "Celestia", "Solara", "Stellaris", "Galaxion", "Astralis", "Novae", "Orionis"])
            print(f"{Fore.YELLOW} --add new star {star["name"]}{Fore.WHITE}")
            return star

        def Objects(Objects : int, Obj_typs : dict, L_star : float) -> dict:
            """
            Objects - Деопозон жилаемых обектов
            Obj_typs - Типы обектов
            """
            names = Obj_typs["objects_name"]
            arr = []
            for _ in range(random.randint(2, Obj_typs["objects"])):
                
                type_Obj = random.choice(Obj_typs["types"])
                if type_Obj == "Planet":
                    obj = {}
                    obj["objects_name"] = random.choice(names)
                    obj["type"] = type_Obj
                    obj["radius"] = random.randint(250, 140_000)#Km
                    obj["ro"] = random.randint(4000, 7000) #kg/m3
                    obj["mass"] = (4/3) * math.pi * (obj["radius"] * 4) * obj["ro"]
                    obj["population"] = 0
                    obj["ore"] = ((4/3) * math.pi * obj["radius"] ** 3) * 0.5
                    obj["materials"] = map.gen.ores()
                    obj["tension"] = 0
                    obj["temp"] = random.randint(-100, 80)
                    obj["races"] = []
                    obj["history"] = []
                    obj["citys"] = []
                    
                if type_Obj == "Asteroid":
                    obj = {}
                    obj["objects_name"] = random.choice(names)
                    obj["type"] = type_Obj
                    obj["radius"] = random.randint(1, 250)#Km
                    obj["ro"] = random.randint(4000, 7000) #kg/m3
                    obj["mass"] = (4/3) * math.pi * (obj["radius"] * 4) * obj["ro"]
                    obj["population"] = 0
                    obj["ore"] = ((4/3) * math.pi * obj["radius"] ** 3) * 0.7
                    obj["materials"] = map.gen.ores()
                    obj["tension"] = 0
                    obj["temp"] = random.randint(-100, 80)
                    obj["races"] = []
                    obj["history"] = []
                    obj["citys"] = []
                    
                print(f"{Fore.YELLOW} ---add new obj {obj["objects_name"]}{Fore.WHITE}")
                arr.append(obj)
                names.remove(obj["objects_name"])
            return arr
        
    class Simulate:
        def Global(loops : int, gelaxy : str) -> None:
            """
            Данная функция симулирует жизнь на планетах
            
            """
            
            
            
            
            file_ = open("cfg.json", "r", encoding="utf-8").read()
            cfg = json.loads(file_)
            
            f = "saves/"+str(gelaxy)+'.json'

            file_ = open(f, "r", encoding="utf-8").read()
            data_ = json.loads(file_)            
            for _ in range(loops):
                for system in data_:
                    try:
                        for obj in system["ojects"]:
                            city = obj["citys"]
                            races = obj["races"]
                            history_stec = obj["history"]
                            r = random.randint(0, 20)
                            
                            if r == 0 and obj["population"] < cfg["history"]["new_race"]["conditions"]["population"]:
                                obj["population"] += 1
                                new_race = random.choice(cfg["races"]["race_list"])
                                if new_race in obj["races"]:
                                    pass
                                else:
                                    history_stec.append(f'{cfg["history"]["new_race"]["text"]} {new_race}')
                                    print(f'{Fore.MAGENTA} {obj["objects_name"]} {Fore.WHITE} {cfg["history"]["new_race"]["text"]} {Fore.GREEN} {new_race}')
                                    races.append(new_race)
                                    obj["population"] = obj["population"] + cfg["history"]["new_race"]["bafs"]["population"]

                            if r == 1 and obj["population"] > cfg["history"]["new_city"]["conditions"]["population"]:
                                arr = []
                                
                                if obj["citys"] == []:
                                    new_city = random.choice(cfg["citys_name"])
                                    history_stec.append(f'{cfg["history"]["new_city"]["text"]} {new_city}')
                                    obj["population"] = obj["population"] + cfg["history"]["new_race"]["bafs"]["population"]
                                    city.append(map.gen.city(new_city, obj["races"]))
                                                                        
                                for i in obj["citys"]:
                                    arr.append(i["name"])
                                new_city = random.choice(cfg["citys_name"])
                                
                                if new_city not in arr:
                                    history_stec.append(f'{cfg["history"]["new_city"]["text"]} {new_city}')
                                    print(f'{Fore.MAGENTA} {obj["objects_name"]} {Fore.WHITE} {cfg["history"]["new_city"]["text"]} {Fore.GREEN} {new_city}')
                                    obj["population"] = obj["population"] + cfg["history"]["new_race"]["bafs"]["population"]
                                    city.append(map.gen.city(new_city, obj["races"]))
                                
                            if obj["population"] >= 4:
                                obj["population"] = round(obj["population"] + (obj["population"]/3))
                                
                            obj["citys"] = city    
                            obj["races"] = races
                            obj["history"] = history_stec
                         
                    except:
                        pass
            
            # сохраняем словарь с информацией в фаил соответствующий айди пользователя
            with open(f, 'w', encoding="utf-8") as file:
                json.dump(data_, file, indent=2)
                
    def global_map(name_save,cr_name, config = "cfg.json"):
        file_ = open(config, "r", encoding="utf-8").read()
        data_ = json.loads(file_)

        f = "saves/"+str(name_save)+'.json'

        data = {}
        systems = []

        names = data_["system_name"]

        for _ in range(data_["systems_count"]):
            
            system = {}
            
            system["star"] = map.gen.Star()
            system["ojects"] = map.gen.Objects(Objects = random.randint(5, 10), Obj_typs = data_, L_star = system["star"]["L"])
            
            system["system_name"] = random.choice(names)
            system["id"] = ""
            links = []
            print(f"{Fore.YELLOW} -add new system {system["system_name"]}{Fore.WHITE}\n")
            for _ in range(random.randint(1, 4)):
                
                rand = random.randint(0, data_["systems_count"])
                if rand not in links:
                    
                    links.append(rand)
                else:
                    pass


            system["links"] = links

            systems.append(system)
            
            data[system["system_name"]] = systems
            names.remove(system["system_name"])
            
        r_sys = random.choice(systems)
        player = {"meta" : {"player_sys":r_sys["system_name"], "player_name" : cr_name, "player_obj" : "", "history":[]}}
        systems.append(player)

        # сохраняем словарь с информацией в фаил соответствующий айди пользователя
        with open(f, 'w', encoding="utf-8") as file:
            json.dump(systems, file, indent=2)
