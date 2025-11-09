### Tuples or Tuplas ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (16, 1.76, "Marco", "Salazar", "Marco")
my_other_tuple = (18, 19, 90)
print(my_tuple, type(my_tuple), len(my_tuple))

print(my_tuple[0], my_tuple[-2]) # casi igual que en las listas mas adelante sera diferente



print()
#################################################################################
# algunos metodos para las tuplas #

print(my_tuple.count("Marco")) # .count(valor) retorna el numero de veces que un objeto se repite en la tuple
print(my_tuple)


print(my_tuple.index("Salazar")) # .index(valor) retorna el indice del valor en la tuple
print(my_tuple)



"""diferencias de las listas"""

# my_tuple[1] = "si dio" # las tuplas no permiten asignamiento  osea son inmutables

my_sum_tuple = my_tuple + my_other_tuple # pero si se pueden sumar

print(my_sum_tuple) 
print(my_sum_tuple[0:4]) 

my_tuple = list(my_tuple)

print(my_tuple)
print(type(my_tuple))

my_tuple[4] = "Salazar Arias" # type: ignore
print(tuple(my_tuple))

# del my_other_tuple[1] # TypeError: 'tuple' object doesn't support item deletion

del my_other_tuple 
# print(my_other_tuple) # NameError: name 'my_other_tuple' is not defined

##########################################################################