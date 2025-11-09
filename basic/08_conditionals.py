### Conditionals ###

my_condition = False

if my_condition: 
    print("se ejecuta la condicion del if")




my_condition = 5 * 11
if my_condition == 10: # se pueden usar operadores de comparcion para determira si algo es verdadero
    print('se ejecuta el 2ndo if') # este bloque de codigo solo se ejecuta si la condicion es true


if my_condition > 10 and my_condition < 20:  
    print('es mayor que diez y menor que 20')
elif my_condition > 50: # el elif es como un if pero si el if principal no funciona o quiero validar otra cosa muy aparte
    print('es mayor que 50')
else: # el else es como si una condicion if o elif no se cumple se ejecuta  
    print('es menor o igual que 10 y mayor que 20')

print('la ejecucion continua....')


my_string = 'my cadena de texto'
if my_string:
    print('my cadena de texto no esta  vacia ')