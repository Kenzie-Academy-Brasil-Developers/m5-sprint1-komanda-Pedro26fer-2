from utils import read_json
from datetime import  datetime


def calculate_tab (count: list):
    
    MENU_PATH = 'menu.json'
    DATA_FORMATED = '%d/%m/%Y %H:%M:%S'
    time = datetime.now()
    subtotal = 0.0
    menu = read_json(MENU_PATH)

    for item in menu:
        for element_in_count in count:
            if item['id'] == element_in_count['id']:
                subtotal += item['price'] * element_in_count['amount']
                closed_komanda =  {'subtotal': subtotal, 'created_at': time.strftime(DATA_FORMATED)}
    return closed_komanda
                

        
