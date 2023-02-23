import os
import json

dict_products = {1: 'Pantalones', 2: 'Camisas', 3: 'Corbatas', 4: 'Casacas'}
dict_prices = {1: 200.00, 2: 120.00, 3:50.00,  4: 350.00}
dict_stock = {1:50, 2:45, 3:30, 4:15}
final_dict = {}

path = 'data.json'

def get_file():
    check_file = os.path.exists(path)
    if not check_file:
        create_file_data()
    return os.path.abspath(path)

def create_file_data():
    product_names = list(dict_products.values())
    product_prices = list(dict_prices.values())
    product_stock = list(dict_stock.values())
    keys = range(len(product_names))
    for i in keys:
        final_dict[i] = [product_names[i], product_prices[i], product_stock[i]]
    json_data = json.dumps(final_dict, indent=2)
    f = open("data.json", "w")
    if f:
        f.write(json_data)
    else:
        print("error")        
    f.close()


def store_json_data(data):
    with open(get_file(), 'w') as outfile:
        json.dump(data, outfile, indent=2)


def get_json_data():
    with open(get_file()) as json_file:
        data = json.load(json_file)
    return data


def read_data():
    data = get_json_data()
    hr = '='*50
    print("\n"+hr+"\nLista de productos\n\nID \t Nombre \t Precio \t Stock\n"+hr)
    for key in data:
        print(key, end='\t')
        for value in data[key]:
            print(value, end=' '*12)
        print('\n')


def add_data(name: str, price: float, quantity: int):
    if quantity>=0 and price >= 0 and name != "":
        attributes = [name, price, quantity]
        data = get_json_data()
        get_last_key = int(list(data.keys()).pop())
        new_key = get_last_key+1
        new_object = {str(new_key): attributes}
        data.update(new_object)
        store_json_data(data)
        print("\nProducto agregado existosamente!")
    else:
        print("\nDatos incorrectos! Ingrese nuevamente")


def delete_data(searching):
    data = get_json_data()
    if str(searching) in data.keys():
        data.pop(str(searching))
        store_json_data(data)
        print("\nProducto eliminado existosamente!")
    else:
        print("\nEl producto que deseas eliminar no existe. Ingresa un ID correcto")


def update_data(name: str, price: float, quantity: int, updated_id: int):
    if quantity>=0 and price >= 0 and name != "":
        data = get_json_data()
        updated_object = {str(updated_id): [name, price, quantity]}
        data.update(updated_object)
        store_json_data(data)
        print("\nProducto actualizado existosamente!")
    else:
        print("\nDatos incorrectos! El producto no pudo actualizarse correctamente")

def search(updated_id: int):
    data=get_json_data()
    if list(data.keys()).index(str(updated_id)) is not None:
        return data.get(str(updated_id))
    else:
        print("\nEl producto que deseas actualizar no existe. Ingresa un ID correcto")
