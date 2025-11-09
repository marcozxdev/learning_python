### Modules ###

import basic.my_module as my_module

my_module.suma(12, 12) # se pone primero el nombre del modulo despues .(lo que quiere usar) y asi se reutiliza codigo de otros archivos

print(my_module.suma(12, 12))

from basic.my_module import suma, resta, multiplica, division # esta es una forma de importar cosas especificas de un modulo o archivo.py

print(suma(1, 1)) # y asi se pude usar la funcion o clase directamente importada si nesecidad del module.(function or class etc)
print(resta(1, 21))
print(multiplica(7,3))
print(division(10, 2))

# my_module.operation('1')

import math  # modulo que viene con python par aser operaciones matematicas avanzadas
print(math.pi)
print(math.pow(2, 8))

from math import pi as PI # se le puden poner pronombres al las cosas especificas que se importan o al modulo

print(PI)
