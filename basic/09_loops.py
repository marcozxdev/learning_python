### Loops ###

# while #

my_condition = 0
while my_condition <= 10: # el while funciona mientras tenga una condicion y sea True
    print(my_condition)
    my_condition += 1
else: # el else es opcional
    print('my_condition es mayor que 10 osea', my_condition)


while my_condition < 20:
    my_condition += 1
    if my_condition == 16: # se pueden poner bucles y condiconales dentro de los bucles
        print('hi ', my_condition)
        break
    print(my_condition)


# For #

my_list = ['pera', 'manzana', 'banana', 'mango']
for element in my_list: # un for itera estructras que so iterables o en rangos
    print(element)

my_set = {'marco', 'ismael', 'alejo'}
for element in my_set:
    if 'marco' in my_set:
        print('marco')

my_tuple = ('hello', 'que tal')
for element in my_tuple:
    print(element)

my_dict = {
    "nombre": 'marco',
    "pais": 'colombia'
}
for element in my_dict.values(): # le aplico el .value() al dict par que me devuelva los valores y no las keys
    print(element)
    if element == 'marco':
        break