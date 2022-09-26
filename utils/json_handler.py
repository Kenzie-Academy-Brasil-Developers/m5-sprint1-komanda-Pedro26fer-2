import json
from textwrap import indent


def read_json(databse_path):

    try:
        with open(databse_path, "r", encoding="utf8") as menu_json:
            if not menu_json:
                return list()
            return json.load(menu_json)
    except IOError:
        return list()

    



def write_json(database_path, new_plate: dict):
    
    with open(database_path, "r", encoding="utf8") as menu:
        file = json.load(menu)
        new_plate = {**new_plate, "id": len(file)+1}
        file = [*file, new_plate ]
        with open(database_path, "w", encoding="utf8") as file_json:
            json.dump(file, file_json, indent= 4)

    return file[-1]    
      

