### Dictionaries ###

my_dict = dict()
my_other_dict = {}

my_other_dict = { # un diccionario tiene clave y valor ejemplos
    'name': 'Marco', # 'name' es la clave que almacena 'Marco'
    'lastname': 'Salazar',
    'age': 16,
}

my_dict = {
    1.1: 'numero 1',
    'name': 'Marco',
    'lastname': 'Salazar',
    'age': 16,
    'lenguages': {'python', 'javascript', 'kotlin', 'rust'},
    'altura': 1.76
}


#########################################################################################

# algunas cosas que se pueden aser #


print(type(my_dict), type(my_other_dict)) # imprimimos el tipo
print(my_dict) # imprimimos todo el diccionario con claves y valors
print(len(my_other_dict), len(my_dict)) # imprimimos cuantas claves tiene el diccionario

print(my_dict['name']) # imprime lo que almacena la clave 'name'

my_dict['altura'] = 1.77 # permite reasignar o cambiar el valor que almacena una key o clave
print(my_dict['altura'])

print(my_dict[1.1]) # permite tener keys como str, float y int

my_dict['calle'] = 'calle 13' # permite crear keys y su valor si la key no existe y si existe solo cambia el valor
print(my_dict)



###########################################################################################

# algunos metodos #

del my_dict['calle'] # sirve para borrar la key con su valor
print(my_dict)

esta_name1 = 'name' in my_dict # se pueden usar operadores de pertencia para ver si una key esta en el dict no el valor y 
esta_name2 = 'Marco' in my_dict['name'] # se pueden usar operadores de pertencia y la key para mirar si un valor esta en la key
print(esta_name1, esta_name2 )

print(my_dict.items()) # .items() retorna un listado con cada uno de los items
print(my_dict.keys()) # .keys() retorna un listado solo con las keys
print(my_dict.values()) # .values() retorna un listado pero solo con los valores que almacena las keys
print(my_dict.fromkeys('name', 'Marcos')) # recorre el primer parametro por cada letra se combierte en una key que almacena el segundo parametro
print(my_dict.fromkeys(('name', 'Marcos'))) # crea keys que no almacenan ningin valor osea none

