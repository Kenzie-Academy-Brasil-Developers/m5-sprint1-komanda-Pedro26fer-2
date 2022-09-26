import json



def read_json(databse_path):

    try:
        with open(databse_path, "r", encoding="utf8") as menu_json:
            return json.load(menu_json)
    except IOError:
        return list()

    except json.JSONDecodeError:
        return list()


    



def write_json(new_plate: dict, database_path = 'menu.json'):

    try:
         with open('menu.json', "r", encoding="utf8") as menu:

            file = json.load(menu)

            if type(file) == dict:

                file_list = list()
                file_list.append(file)
                new_plate = {**new_plate, "id": len(file_list)+1}
                file_list.append(new_plate)
                with open(database_path, "w", encoding="utf8") as file_json:
                    json.dump(file_list, file_json, indent= 4) 
                return file_list[-1] 

            new_plate = {**new_plate, "id": len(file)+1}
            file = [*file, new_plate]

            with open(database_path, "w", encoding="utf8") as file_json:
                    json.dump(file, file_json, indent= 4) 
            return file[-1]          


    except IOError:
            first_plate = {**new_plate, "id": 1}
            with open(database_path, "w", encoding="utf8") as file_json:
                json.dump(first_plate, file_json, indent= 4)
                return first_plate


        

      

