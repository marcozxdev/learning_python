### Operators ###


######################################################################################

# operadores aritmeticos #

print(11 + 4) # suma
print(11 - 4) # resta
print(11 * 4) # multiplicacion
print(11 / 4) # division con resto
print(11 // 4) # division entera o redondeada
print(11 % 4) #  division pero de el resto
print(2 ** 4) # potenciacion

print(1 + 2 - 1 * 10 / 5 ** 2)


# algunas formas de usar con cadenas de texto

print("hola" + "mundo" + "como vas") # es parecido a concatenar con ,
print("hola" * 2) # multiplica la palabra
print("hola" +  str(2)) # toca comvertir el numero que se va a sumar 



print()
##########################################################################################

# Operadores de comparacion #

print(5 > 6) # mayor que
print(5 < 6) # menor que
print(5 >= 6) # mayor o igual que
print(5 <= 6) # menor o igual que
print(5 == 6) # igual que
print(5 != 6) # distinto que


# algunas formas de uso 
print("hello" > "python")
print("hello" < "python")
print("hello" == "python")

## nota: es pueden usar de varias meneras con str, float, int etc..
## tambien ten en cuenta que si se comparan str lo ase python alfabeticamente



print()
########################################################################################

# Operadores logicos #

print(3 > 4 and "hello" > "python") # and los dos valores deben ser True pra devolver True
print(3 > 4 or "hello" > "python") # or debe haber minimo un True para devolver True
print(not (3 < 4)) # lo contradice osea (not (3 < 4) = Falso)

print()
# ejemplos
print(3 < 4 and "hello" < "python")
print(3 < 4 or "hello" < "python")
print(3 < 4 or "hello" > "python")
print(not (3 > 4))
print(not(True or False))
print(False and False)


print()

##########################################################################################

# Operadores de pertenencia #

fruits = ['apple', 'mango', 'banana', 'carrot']

exist_fruit = 'carrot' in fruits # retorna true porque carrot si esta en fruits
print(exist_fruit)

exist_cars = 'GTR' in fruits # retorna false porque no esta el GTR
print(exist_cars)

exist_cars = 'gtr' not in fruits # retorna true porque no esta
print(exist_cars)




# nota: estos operadores se pueden usar par casi cualquier tipo de variable