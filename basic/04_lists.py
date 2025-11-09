### Lists or listas ### 

my_first_list = list()

my_other_list = []

print(len(my_first_list))


my_first_list = ["Marco", "Salazar", 16]
print(my_first_list, len(my_first_list))


my_other_list = [16, 1.75, "Marco", "Salazar"]
print(type(my_other_list))


print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-2])
# print(my_other_list[-5]) IndexError:


# asignacion con division o desempaquetado
age, height, name, surname = my_other_list
print(age, name)

age, height, name, surname = my_other_list[0], my_other_list[1], my_other_list[-2], my_other_list[-1]
print(age, name)

print(my_first_list + my_other_list)


print()
#################################################################################

# algunas metodos para las listas

other_list = ["julio", "julio" "Marco", "Marco", 0, 0, 1, 1]

print(other_list.count("Marco")) # .count(valor) retorna el numero de veces que un objeto se repite en la lista


my_first_list.append("MAXINFL") # .append(valor) inserta un nuevo valor a la lista en el final
print(my_first_list[-1])


my_first_list.insert(0, "hey 0") # .insert(index, valor) inserta un valor en el indice de la lista
print(my_first_list[0])


my_first_list[0] = "HEY 0" # similar a insert pero mas directo
print(my_first_list)


my_first_list.remove("HEY 0") # .remove(valor) borra de la lista el valor que este en la lista

my_first_list.pop() # elimina el ultimo objeto de la lista osea el -1 tambien se le puede pasar index
print(my_first_list.pop()) # lo llamamos 2 veces asi que borra 2 objetos

my_new_list = my_first_list.copy()

del my_first_list[-1] # sirve para borrar por indice tambien pero no retorna ningun valor
print(my_first_list)


my_first_list.clear() # borra todos los valores de la lista o limpia la lista
print(my_first_list)
print(my_new_list)

my_new_list.reverse() # .reverse() voltea la lista al revez
print(my_new_list)


my_new_list_int = [0, 2, 5, 11, 9, 7, 10]
my_new_list_int.sort() # .sort() Ordena la lista dependiendo de lo que aya en la lista pero
# si la lista esta conformada de un solo tipo
# se recomienda usar si la lista es de solo numeros o int porque es mas facil
print(my_new_list_int)

print(my_new_list_int.index(2)) # .index(valor) retorna el indice del valor en la list

print(my_new_list_int[0:3]) # imprime desde:hasta como definir un rango 


print()



