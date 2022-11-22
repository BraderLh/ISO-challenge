import os
import json


json_files = [pos_json for pos_json in os.listdir('./') if pos_json.endswith('.json')]


def read_data():
    f = open(json_files[0])
    data = json.load(f)
    hr = '='*50
    print(hr+"\nLista de productos\n"+hr)
    for key in data:
        print(key, end=' '*5)
        for value in data[key]:
            print(value, end=' '*5)
        print('\n')
    f.close()
    

def add_data():
    name = str(input("\n Nombre del producto: "))
    price = float(input("\n Precio del producto: "))
    quantity = int(input("\n Stock del producto: "))

    attributes = [name, price, quantity]

    with open(json_files[0]) as f:
        data = json.load(f)
    
    get_last_key = int(list(data.keys()).pop())
    new_key = get_last_key+1
    new_object = {str(new_key): attributes}
    data.update(new_object)

    with open('addional-data', 'w') as f:
        json.dump(data, f, indent=2)
    
    f.close()


def delete_data(deleted_id: int):
    with open(json_files[0]) as f:
        data = json.load(f)
    if list(data.keys()).index(str(deleted_id)):
        data.pop(str(deleted_id))
        
        with open('deleted-data.json', 'w') as f:
            json.dump(data, f, indent=2)
    else:
        print("\nEste ID no se encuentra en tus datos. Ingresa un ID correcto")
    
    f.close()


def update_data(updated_id: int):
    with open(json_files[0]) as f:
        data = json.load(f)
    try:
        list(data.keys()).index(str(updated_id))
        name = str(input("\n Nombre del producto: "))
        price = float(input("\n Precio del producto: "))
        quantity = int(input("\n Stock del producto: "))
        #print('unrelease:', data)
        updated_object = {str(updated_id): [name, price, quantity]}
        data.update(updated_object)
        #print('release', data)
        with open('updated-data.json', 'w') as f:
            json.dump(data, f, indent=2)
    except ValueError:
        print("\nEste ID no se encuentra en tus datos. Ingresa un ID correcto")
    
    f.close()
