'''
estructuras de control
'''


# list 
my_list = [1, 2, "3"]
my_list.append("4") # metodo para añadir un valor a la list en el final de la lista #  añadir
my_list.pop(0) # metodo para eliminar un valor por su index #  borrar
my_list[0] = 23 # actualizar
# my_list.sort() # ordenacion


# tuplas

my_tuple = ("marco", "salazar", 16)
my_tuple[1] # solo permite acceder 


# sets
my_set = {"hi" "como estas" "que ases", "bien", 18} # los datos no se repiten
my_set.add("super") # metodo para añadir # añadir
# my_set.remove("hi") # metodi para borar un valor # borrar
# nota el set no se puede ordenar


# diccionario

my_dict = {"name": "marco", "age": 16}
my_dict["alias"] = "the marcoszxdev" # forma para añadir o insertar
my_dict["age"] = 17 # forma para actualizar valores
del my_dict["alias"] # forma para eliminar un valor


"""
reto extra
"""

contacts = [
    {"name": "marco", "tel": 3045580098}
]

# print(contacts[0].get("name"))

# print(contacts.keys())

def search_contact(case):
    if case == 1:
        print("pude buscar por el nombre del contacto o el numero de telefono")
        contact = input(": ")
        for i in range(0, len(contacts) + 1, 1):
            if contact == contacts[i].get("name") or contact == contacts[i].get("tel"):
                print(f"el contacto existe\nnombre: {contacts[i]["name"]}\ntelefono: {contacts[i]["tel"]}")
                print("espero que te alla servido de ayuda adios")
                return
        print("parese que ese contacto no existe....lo siento")
    elif case == 2:
        print("para actualizar debe dar en nombre de contacto o el numero")
        contact = input(": ")
        for i in range(0, len(contacts) + 1, 1):
            if contact == contacts[i].get("name") or contact == contacts[i].get("tel"):
                print(f"el contacto existe\nnombre: {contacts[i]["name"]}\ntelefono: {contacts[i]["tel"]}")
                print("que desea actualizar el\n1.nombre\n2.telefono")
                opc = input(": ")
                if opc == "1":
                    print(f"nombre actual: {contacts[i]["name"]}")
                    new_name = input("Nuevo nombre: ")
                    contacts[i]["name"] = new_name
                    print("contacto actualizado exitozamente ")
                    return
                elif opc == "2":
                    print(f"Numero actual: {contacts[i]["tel"]}")
                    new_tel = input("Nuevo numero: ")
                    contacts[i]["tel"] = new_tel
                    print("contacto actualizado exitozamente ")
                    return
    else:
        print("para Borrar un contacto debe debe dar en nombre de contacto o el numero")
        date = input(": ")
        for i in range(0, len(contacts) + 1, 1 ):
            if date == contacts[i]["name"] or date == contacts[i]["tel"]:
                del contacts[i]
                print("contacto eleminado exitosamente")
                return

    print("parese que ese contacto no existe....lo siento")

def update_contact():
    search_contact(2)


def delete_contact():
    search_contact(3)


def add_contact():
    while True:
        try:
            name = input("nombre: ")
            tel = int(input("telefono: "))
            if name and len(str(tel)) == 10:
                print("añadiendo..")
                contacts.append({"name": name, "tel": tel})
                print(f"Nuevo contacto añadido: {name}, {tel}")
                return
            else:
                print("asegurese de llenar los campos solicitados y que los que halla mas 10 dijitos")
        except:
            print(" asegurese de poner solo numeros en el campo del telefono")



def control(case):

    match case:
        case 1:
            add_contact()
        case 2:
            search_contact(1)
        case 3:
            search_contact(2)
        case 4:
            search_contact(3)



def menu():

    while True:
        print("1.añadir contacto\n2.buscar contacto\n3.actualizar contacto\n4.borrar contacto\n5.salir")
        try: 
            opc = int(input(": "))
            if opc == 5:
                print("saliendo...")
                return
            else:
                control(opc)

        except ValueError:
            print("solo se permiten numeros")


menu()













