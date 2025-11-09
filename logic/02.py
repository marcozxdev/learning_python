

'''
funciones definidas por el usuario
'''

#  simple

def greet():
    print('hello python')

greet()

def return_greet():
    return "hello python"

print(return_greet())


# con argumento
def arg_greet(name):
    print(f"hello, {name}")

arg_greet("name")


# con argumentos

def args_greet(name, age):
    print(f"hello, {name} su edad es {age}")

args_greet("name", 16)

# con argumentos por defecto

def args_greet_default(name="marco", age=16):
    print(f"hello, {name} su edad es {age}")

args_greet_default("ismael", 13)

# con varios valores de retorno

def multi_returns(name, lastname, age):
    return name, lastname, age

print(multi_returns("marco ", "salazar", 16))

# con un numero variable de  argumentos

def variable_args(*values):
    for i in values:
        print(f'hi, {i}')

variable_args("marco", "julio", "ismael")


def key_variable_args(**values):
    for i, j in values.items():
        print(f'hi, {i} {j}')

key_variable_args(name='marco', age=16)


"""
funciones dentro de funciones
"""


def outer_function():
    def inner_function():
        print('print desde la funcion interna')
    inner_function()

outer_function()


"""
funciones ya establecidas por el lenguaje
"""

print() # Imprime en consola 
len(multi_returns(18,18, 18)) # retorna la cantidad de valores 
type(str) # retorna el tipo de dato de un valor

"""
variables locales y globales
"""

global_dollar = 4_000 # variable que todas las funciones pueden acceder

def modify_price():
    my_dollar = 4_090 # variable que ssolo se pude aceder dentro de esta funcion
    print(global_dollar + 56)






"""
extra reto
"""

def solution(value1: str="a", value2: str="b") -> int:
    count = 0
    for i in range(1, 101):
        if i % 5 and i % 3 == 0:
            print(value1 + value2)
        elif i % 3 == 0:
            print(value1)
        elif i % 5 == 0:
            print(value2)
        else:
            print(i)
            count += 1

    return count


print(solution())






















