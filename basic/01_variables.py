# Variables
# nota: del my_sting # borra la variable
my_first_string_variable = "my primera variable alfanumerica" # asi se define una variable
print(my_first_string_variable, type(my_first_string_variable))

# o tambien definiendo el tipo de dato
my_string: str = "un string"

my_int_variable = 17 # asi se define una variable
print(my_int_variable, type(my_int_variable))

my_int_to_string = str(my_int_variable)
print(my_int_to_string, type(my_int_to_string))

my_float_variable = 1.8 # asi se define una variable
print(my_float_variable, type(my_float_variable))

my_bool_variable = False # asi se define una variable
print(my_bool_variable, type(my_bool_variable))



print()
########################################################################################

# tipando variables (opcional) tipar la variable es decirle de que tipo va a ser
# forzamos el tipo
string: str = "esto es un string"
print(type(string))

int: int = 26 # tipo entero o int
print(type(int))

float: float = 16.1 # tipo flotante o float
print(type(float))

boolean: bool = True # tipo bool o booleano
print(type(boolean))



print()
####################################################################################

# concatenacion de variables o datos en un print
# print() puede recibir varios parametros y concatenacion separando cada valor por ,
print(my_first_string_variable, my_int_variable, my_float_variable, my_bool_variable)

# ejemplo
print("Esto es u string:", my_first_string_variable)



print()
##########################################################################################

# algunas funciones del sistema:

# print()
print('hola desde print') # sirve para imprimir en consola los valores
# que se le pasan en los parentices como variables o returns de una funcion etc

# input() pide datos por consola qe se guarda en una variable
data = input("escribe algo ")

# len(valor)
len(my_first_string_variable) # len(valor) retorna el tamaño del valor
print("tamaño de string:", len(my_first_string_variable)) # imprimimos lo que retorna len()  




print()
#####################################################################################

# variables en una sola línea ¡Cuidado con usar esta sintaxis!
name, surname, alias, age = "marco", "salazar", "marcos", 16 # se define una por una en la linea
print("my name is:", name, "my age is:", age)# concatenacion de variables o datos en un print




print()
###############################################################################################

# entradas o inputs para guardar datos en una variable o en un lugar
# variable = input() la variable guarda el dato que escriben por consola 
name_input = input("como te llamas ")
age_input = input("cual es tu edad ")

print(name_input, age_input)




print()
###############################################################################################

# concluciones #

'''
una varible guarda datos en la memoria ram y son parecidas a las de algebra
print() imprime por consola algo segun lo que le den
input() pide datos al usuario 
len() retorna la cantidad de caracteres objetos o valores de algo dependindo lo que se de como parametro
type() retorna el tipo de dato

existen varios tipos de datos como

string = str
integer = int
float = float
bool = bool


'''