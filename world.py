import json
import random
import math
import caracter
from colorama import Fore

sigma = 5.67 * (10 ** -8) 
L_sun = 3.828 * (10 ** 26)

DEBUG_MODE = False

def SHOW(a, MODE):
    if DEBUG_MODE:
        print(a)
    else:
        pass

class get:
    
    class events():
        def text(event_name : str) -> str:
            file_ = open("cfg.json", "r", encoding="utf-8").read()
            cfg = json.loads(file_)
            return cfg["history"][event_name]["text"]
        
        def baf(event_name : str, baf_ : str):
            file_ = open("cfg.json", "r", encoding="utf-8").read()
            cfg = json.loads(file_)
            return cfg["history"][event_name]["bafs"][baf_]
    
    def list_events():
        file_ = open("cfg.json", "r", encoding="utf-8").read()
        cfg = json.loads(file_)
        
        arr = []
        
        for i in cfg["history"]:
            arr.append(i)
        return arr      

    def condition(event_name : str, condition : str):
        file_ = open("cfg.json", "r", encoding="utf-8").read()
        cfg = json.loads(file_)
        
        return cfg["history"][event_name]["conditions"][condition]
    
    def conditions(event_name : str):
        file_ = open("cfg.json", "r", encoding="utf-8").read()
        cfg = json.loads(file_)
        
        arr = []
        
        for i in cfg["history"][event_name]["conditions"]:
            arr.append(i)
        return i
            

class map:

    class gen:
        
        def city(name : str, races : list, pop = 4000) -> dict:
            
            file_ = open("cfg.json", "r", encoding="utf-8").read()
            cfg = json.loads(file_)
            
            arr = {}
            arr["name"] = name
            arr["population"] = pop
            arr["factory"] = 0
            arr["war_factory"] = 0
            arr["aria"] = 36 #Km^3
            arr["ore"] = 0
            
            resurses = {} # ресурсы
            resurses["titanium"] = 0 # Титан (основа для всей высоко уровневой техники)
            resurses["iron"] = 0 # Железа (ресурс для создания инструментов и строительства)
            resurses["gold"] = 0 # Золото (ценный ресурс, хороший проводник а также средство поддержания экономики)
            resurses["rubber"] = 0 # Резина (необхадима для разного рода техники)
            resurses["wood"] = 0 # Древесина (материал для домов и других зданий можно применить в качестве топлива)
            resurses["oil"] = 0 # Нефть (ценейший ресрс для машино сторения)
            resurses["gas"] = 0 # Газ (ольтернотивный источьник топлитва для наземного и воздушного транспорта)
            
            army = {}
            army["population"] = pop / 3
            army["wapon"] = 0
            army["tanks"] = 0
            army["air"] = 0
            
            mashins = {}
            mashins["tank"] = {}
            mashins["air"] = {}
            mashins["wapon"] = {}
            
            army["mashins"] = mashins
            
            arr["army"] = army            
            arr["resurses"] = resurses
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
            
            for _ in range(random.randint(1, len(data_["materials"]["list"]) * 2)):
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
        def Global(loops : int, gelaxy : str, show = True) -> None:
            """
            Данная функция симулирует жизнь на планетах
            
            """
            
            
            
            
            file_ = open("cfg.json", "r", encoding="utf-8").read()
            cfg = json.loads(file_)
            
            f = "saves/"+str(gelaxy)+'.json'

            file_ = open(f, "r", encoding="utf-8").read()
            data_ = json.loads(file_)          
            for _ in range(loops):
                
                o = 0
                for system in data_:
                    
                    
                    #Итерация по всем обектам в системе, кроме звезды
                    
                    if o != len(data_) - 1:
                        for obj in system["ojects"]:
                            if obj["population"] < 2 and len(obj["citys"]) < 4:
                                obj["population"] += 1
                            elif obj["population"] >= 2 and len(obj["citys"]) < 4:
                                obj["population"] += obj["population"] / 2
                            events_list = get.list_events()
                            event = random.choice(events_list)
                            SHOW(events_list, DEBUG_MODE)
                            
                            for i in obj["citys"]:
                                resurses: dict = i["resurses"]
                                factorys: int = i["factory"]
                                war_factorys: int = i["war_factory"]
                                army = i["army"]
                                
                                industry_bafs = cfg["ideas"][i["idea"]]["bafs"]["support industry"]
                                war_bafs = cfg["ideas"][i["idea"]]["bafs"]["support war"]
                                
                                ore: list = obj["materials"]
                                SHOW(ore, MODE=DEBUG_MODE)
                                
                                # Завдо производит мирную продукцию и добывает ресурсы
                                if "titan_ore" in ore:
                                    resurses["titanium"] += cfg["materials"]["titan_ore"]["elemnts"]["Ti"] * (factorys + industry_bafs)
                                if "iron_ore" in ore:
                                    resurses["iron"] += cfg["materials"]["iron_ore"]["elemnts"]["Fe"] * (factorys + industry_bafs)                                
                                if "gold_ore" in ore:
                                    resurses["gold"] += cfg["materials"]["gold_ore"]["elemnts"]["Au"] * (factorys + industry_bafs)
                                if "wood" in ore:
                                    resurses["wood"] += 1 * (factorys + industry_bafs)
                                if "oil" in ore:
                                    resurses["oil"] += 1 * (factorys + industry_bafs)
                                for i in ore:
                                    if cfg["materials"]["gases"] in ore:
                                        resurses["gas"] += cfg["materials"][i]["elemnts"]["H"] * factorys
                                        
                                # Военные фабрики производят необходимое для войны
                                if war_factorys >= 1:
                                    if army["mashins"]["tank"] != {}:
                                        army["tanks"] += 1 * (war_factorys + war_bafs)
                                    if army["mashins"]["air"] != {}:
                                        army["air"] += 1 * (war_factorys + war_bafs)
                                    if army["mashins"]["wapon"] != {}:
                                        army["wapons"] += 1 * (war_factorys + war_bafs)
                                                                                
                            #Выбор случайных событий из списка
                            if obj["population"] >= get.condition(event, "population"):
                                if show:
                                    print(Fore.MAGENTA + obj["objects_name"] + Fore.WHITE + " " + get.events.text(event))
                                obj["population"] += get.events.baf(event, "population")

                                # Событие зарождение новой рассы
                                if event == "new_race" and random.randint(1, 100) >= 20:
                                    arr: list = obj["races"]
                                    rrace = random.choice(cfg["races"]["race_list"])
                                    if rrace not in arr:
                                        arr.append(rrace)
                                    obj["races"] = arr

                                # Событие основание нового города
                                if event == "new_city" and random.randint(1, 100) >= 40 and len(obj["citys"]) < 4:
                                    arr: list = obj["citys"]
                                    arr.append(map.gen.city(random.choice(cfg["citys_name"]), obj["races"], get.condition(event, "population")))
                                    obj["citys"] = arr
                                    obj["population"] -= get.condition(event, "population")

                                # Событие основание нового города
                                if event == "new_building" and random.randint(1, 100) >= 40 and len(obj["citys"]) > 0:
                                    for i in obj["citys"]:
                                        builds: list = cfg["buildings"]["list"]
                                        build = random.choice(builds)
                                        i[build] += 1
                            
                    o += 1
                SHOW(f"{Fore.YELLOW}[step: {_+1}]{Fore.WHITE}", MODE=DEBUG_MODE)       
                    
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
