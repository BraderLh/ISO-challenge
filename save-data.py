import json

dict_products = {1: 'Pantalones', 2: 'Camisas', 3: 'Corbatas', 4: 'Casacas'}
dict_prices = {1: 200.00, 2: 120.00, 3:50.00,  4: 350.00}
dict_stock = {1:50, 2:45, 3:30, 4:15}
final_dict = {}


def create_json_file():
    product_names = list(dict_products.values())
    product_prices = list(dict_prices.values())
    product_stock = list(dict_stock.values())
    keys = range(len(product_names))

    for i in keys:
        final_dict[i] = [product_names[i], product_prices[i], product_stock[i]]

    json_data = json.dumps(final_dict)
    #load_data = json.loads(json_data)
    f = open("data.json", "w")
    f.write(json_data)
    f.close()

create_json_file()
