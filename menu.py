from functions import *

def menu():
    filename = get_file()
    while True:
        print("\n**************Bienvenido a ISO CRM*************\n")
        print(" [0] Mostrar \n [1] Agregar \n [2] Eliminar \n [3] Actualizar \n [4] Salir")
        option = int(input("\n Eliga una opción: "))    
        if option == 0:
            read_data()
        elif option == 1:
            name = str(input("\n Nombre del producto: "))
            price = float(input("\n Precio del producto: "))
            quantity = int(input("\n Stock del producto: "))
            add_data(name, price, quantity)
        elif option == 2:
            searching = str(input("\nIngrese el ID o el nombre del producto: "))
            delete_data(searching)
        elif option == 3:
            updated_by_id = int(input("\nIngrese el ID del producto: "))
            search(updated_by_id) 
            if search is not None:
                name = str(input("\n Nombre del producto: "))
                price = float(input("\n Precio del producto: "))
                quantity = int(input("\n Stock del producto: "))
                update_data(name, price, quantity, updated_by_id)
        elif option == 4:
            break
        else :
            print("\nNo existe dicha opción. Ingrese nuevamente ...")
