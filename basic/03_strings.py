### Strings ###

my_string = "Mi string"
my_other_string = "Mi otro string"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

print("\\ un nose como se llame \\")

my_new_line_string = "Este es un string \ncon salto de linea"
print(my_new_line_string)


my_tab_string = "\tEste es un string con tabulación"
print(my_tab_string)

print()
#################################################################################

# formateo de strings #

# algunos ejemplos de formateo de string nota el formateo de strings no es lo mismo a 
# concatenar

name, surname, age = "Marco", "Salazar", 16

print("Mi nombre es: %s %s y mi edad es: %d " %(name, surname, age)) # con %s

print("Mi nombre es: {} {} y mi edad es: {} ".format(name, surname, age)) # con .format(variables)

print(f"Mi nombre es: {name} {surname} y mi edad es: {age} ") # con f-string

print()
###############################################################################################

# Desempaquetado de caracteres #

lenguage = "python"
a, b, c, d, e, f = lenguage
print(a, b, c, d)
print(e, f)


print()
######################################################################################

# metodos de stings #

lenguage_slice = lenguage[0:3] 
print(lenguage_slice)

lenguage_slice = lenguage[1:]
print(lenguage_slice)

lenguage_slice = lenguage[-2]
print(lenguage_slice)

lenguage_slice = lenguage[0::2]
print(lenguage_slice)


print()

# Reverse 

reversed_lenguage = lenguage[::-1] # retorna el string al raves
print(reversed_lenguage)



print()
###########################################################################

# Funciones o metodos para strings #
lenguage = " python is Easy Easy"

print(lenguage.capitalize()) # pone la primera letra en Mayus

print(lenguage.upper()) # pone todas las palabras a Mayus

print(lenguage.count("Easy")) # cuenta cuantas veces esta la letra o palabra

print("12".isnumeric())  # mira si el string solo esta compuesto por numeros
print(lenguage.isnumeric())  # mira si el string solo esta compuesto por numeros

print(lenguage.lower()) # pone todas las palabras o letras a minus


print(lenguage.upper().isupper()) # lo transformamos y luego validamos 

print(lenguage.startswith("py")) # valida si inicia el string por lo qeu le pasamos

print(lenguage.title()) # pone la primera letra de cada palabra a Mayus

print(lenguage.strip()) # elimina los espacios que hay en el string 



# entre muchos mas metodos pa ra aplicar a los strings busca y aprende

print()
