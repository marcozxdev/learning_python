### Classes ###

class MyEmptyPerson: # una clase sirve para modelaar o crear una estructura para un objeto
    pass


class Person:
    def __init__(self, name='Marco', lastname='Salazar', age=16): # metodo constructor para pedir valores cuando se este instanciando la clase

        # atributos 
        self.display_name = name # el self.name es para aser referencia a .name cundo se le este aplicando al objeto
        self.lastname = lastname
        self.age = age

        # propiedad
        self.__name = name # propiedad o atributo privado

    
    def name_complet(self): # se puden crear funciones que siempre deben recibir el parametro self
        print(f'Nombre: {self.display_name} Apellido: {self.lastname} Edad: {self.age}')


    ### Formas para acceder a propiedades privadas ###
    
    # atraves de decoradores

    @property
    def private_name(self):
        return self.__name
    
    @private_name.setter
    def private_name(self, new_name):
        if not new_name:
            return 'not have new_name'
        self.__name = new_name

#####################

    # mediante funciones getters y setters #

    # metodo set solo para modificar propiedades privadas
    def set_name(self, name):
        self.__name = name


    # metodo get solo para acceder a  propiedades privadas
    def get_name(self): # funcion get que retorna el atributo privado __name retorna lo que almacena
        return self.__name





my_person = Person('marco', 'arias', 17) # instanci o objeto

print(my_person.display_name) # el .name es para aseder a el atributo de la clasepass

my_person.name_complet() # se llaman funciones que solo se puden aplicar alcualquier insancia de la clase

my_person.age = 16 # se puden cambiar los atributos despues de crear el objeto

my_person.get_name() # retorna una propiedad definida dentro de la clase que sea privada y la unica forma pra acceder es utilizando una funcion get ya definida dentro de la clase
print(my_person.get_name())
my_person.set_name('david') # cambia la propiedad privada

my_person.private_name # retorna lo que hay en la propiedad __name 
print(my_person.private_name)
my_person.private_name = 'Marco' # se cambia nomas la propiedad privada __name
print(my_person.private_name)

print(my_person.age)