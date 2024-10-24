import random
import json

def get_materials():
    CFG = open(f"cfg.json", "r", encoding="utf-8").read()
    cfg = json.loads(CFG)    

    material = []
    
    for i in cfg["materials"]:
        material.append(i)
    return material

class wepons:
    
    def craft(material : str, type : str) -> dict:
        CFG = open(f"cfg.json", "r", encoding="utf-8").read()
        cfg = json.loads(CFG)

        materials = get_materials()
        if material in materials and type in cfg["wapon_types"]:
            item = {}

            item["type"] = type
            item["material"] = material
            item["strength"] = cfg["materials"][item["material"]]["strength"]
            item["damage"] = cfg["wapons"][item["type"]]["damage"] + cfg["materials"][item["material"]]["damage"]
            item["range"] = cfg["wapons"][item["type"]]["range"]
            item["properties"] = cfg["wapons"][item["type"]]["properties"]
            item["speed"] = cfg["wapons"][item["type"]]["speed"] + cfg["materials"][item["material"]]["speed"]
            item["damage_type"] = cfg["wapons"][item["type"]]["damage_type"]
            for i in cfg["effects"]:
                r = random.randint(1, 100)
                if r <= cfg["effects"][i]["procentage"]:
                    item["effects"] =  i
                    break
                else:
                    item["effects"] = "None"
            return item
        else:
            return None
    
    def make() -> dict:
        CFG = open(f"cfg.json", "r", encoding="utf-8").read()
        cfg = json.loads(CFG)

        materials = get_materials()

        item = {}

        item["type"] = random.choice(cfg["wapon_types"])
        item["material"] = random.choice(materials)
        item["strength"] = cfg["materials"][item["material"]]["strength"]
        item["damage"] = cfg["wapons"][item["type"]]["damage"] + cfg["materials"][item["material"]]["damage"]
        item["range"] = cfg["wapons"][item["type"]]["range"]
        item["properties"] = cfg["wapons"][item["type"]]["properties"]
        item["speed"] = cfg["wapons"][item["type"]]["speed"] + cfg["materials"][item["material"]]["speed"]
        item["damage_type"] = cfg["wapons"][item["type"]]["damage_type"]
        for i in cfg["effects"]:
            r = random.randint(1, 100)
            if r <= cfg["effects"][i]["procentage"]:
                item["effects"] =  i
                break
            else:
                item["effects"] = "None"
        return item
    
class armor:
    
    pass