import json
import math
import random

config = 'cfg.json'

class Ship:
    
    class Create:
        
        def bluePrint(name : str,
                      class_ : str,
                      ):
            file_ = open(config, "r", encoding="utf-8").read()
            data_ = json.loads(file_)
            
            
            
            bprint = {}
            bprint["name"] = name
            bprint["class"] = class_
            
            
            f = f"ships/{name}.json"
            if open(f, "r").read() != None:
        # сохраняем словарь с информацией в фаил соответствующий айди пользователя
                with open(f, 'w', encoding="utf-8") as file:
                    json.dump(bprint, file, indent=2)                
            
        
        def new(name : str, ):
            pass
        