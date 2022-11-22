from functions import *

def menu():
    while True:
        print("\n**************Bienvenido a ISO CRM*************\n")
        print(" [0] Mostrar \n [1] Agregar \n [2] Eliminar \n [3] Actualizar \n [4] Salir")
        option = int(input("\n Eliga una opción: "))

        if option == 0:
            read_data()
        elif option == 1:
            print("\n Añada un producto -> ")
            add_data()
        elif option == 2:
            deleted_by_id = int(input("\nIngrese el ID del producto: "))
            delete_data(deleted_by_id)
        elif option == 3:
            updated_by_id = int(input("\nIngrese el ID del producto: ")) 
            update_data(updated_by_id)
        elif option == 4:
            break
        else :
            print("\nNo existe dicha opción. Ingrese nuevamente ...")
