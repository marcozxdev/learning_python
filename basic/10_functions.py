### Functions ###

def my_function(): # una funcion es un bloque de codigo que se ejecuata cuando se llama la funcion
    print('esto es una funcion ')

my_function()

def sum_two_values(a, b): # se le pasan parametros que son como variables que se asignan cundo se llama la funcion
    print(a + b)

sum_two_values(10, 18)


def sum_two_values_with_return(a, b): # hay funciones que retornan valores osea no se queda dentro los valores
    return a + b

my_result = sum_two_values_with_return(18, 30) # guardamos lo que retorna la funcion
print(my_result)


def print_name_with_default(name='sin name', lastname='sin apellido'): # se pueden definir parametros por defecto en caso de que cuando llamen la funcion no le asignen los parametros
    print(name, lastname)

print_name_with_default('marco', 'salazar')
print_name_with_default('marco')



# esta es una funcion que puede recibir los parametrosque sean osea *args
def print_texts(*texts): # se crea un parametro que puede guardar varias cosas
    print(texts)

print_texts('hey', 'como', 'tas')

# mas ejemplos de *args **keyargs

def print_name_to_mayus(*names): # el *names es ase como si se pudiera definir muchas cosas en un solo parametro ose como una tuple
    for name in names:
        print(name.upper())

print_name_to_mayus('marco', 'pipe')