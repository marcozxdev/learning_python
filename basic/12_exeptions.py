### Exeptions ###


num1 = 1
num2 = '2'

# try exept

try: # lo que valla dentro del try si llega a causar error manda a ejecutar el codigo que halla en el exept
    print(num1 + num2)
    print('help')
except: # se ejcuta si el bloque de codigo que halla en try da error
    print('olle no puedes sumar un un int con un str')


# try exept else

try:
    print(1 + 1)
except:
    print('se a producido un error')
else:
    print('la ejecucion contina1') # el else solo se ejecuta si no ha errores en el try 

print('runing..')

# try except else finally

try:
    print(1 + 1)
except:
    print('se a producido un error')
else:
    print('la ejecucion contina1') 
finally: # finlly siempr se ejecuta alla o no alla error
    print('runing2..')

print('running3....')


# Exeptions for type #

try:
    print(1 + '1')
except TypeError: # TypeError es para errores dee Typo de dato
    print('estas sumando str y int y eso no se puede aser', 'se a producido un TypeError')
except ValueError:
    print('error por ValueError') # se puden controlar los  varios tipos de errores


# captura de informacion del las exepciones o errores #
try:
    print('1' + 1)
except TypeError as error:
    print('se a producido un error 5')
    print(error)

