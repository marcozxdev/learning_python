### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # inicialmente un diccionario

my_other_set = {'Marco', 'Arias', 16} # se define como una lista pero con {}
print(type(my_other_set))
print(len(my_other_set))

my_other_set.add('marcoszxdev')

print(my_other_set) # 1a conclucion un set no es una estructura ordenada #

my_other_set.add('marcoszxdev') # .add(valor) inserta un valor

print(my_other_set) # 2a conclucion un set no admite valores repetidos #

print(16 in my_other_set) # se puede  realizar busqueda con los operadores de pertencia


my_set = {'Python', 'Rust', 'Javascript', 'Go'}






####################################################################################################

# algunos metodos #

my_new_set = my_set.union(my_other_set) # .union(valor o set) ase una union que retorna un set con la union entre valores

my_other_set.add('marcoszxdev') # .add(valor) inserta un valor

my_other_set.remove(16) # .remove(valor) elimina el valor que este en el set
print(my_other_set)

my_other_set.clear() # .clear() borra todos los valores que aya en el set
print(my_other_set)

print(my_new_set.difference(my_set))
