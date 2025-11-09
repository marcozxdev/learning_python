

# operadores #


# aritmeticos

# +, -, *, **, /, //

suma = 1 + 3
resta = 5 - 3
multiplicacion = 5 * 5
potencia = 2 ** 8
division_con_residuo = 10 / 3
divison_sin_residuo = 10 // 3
resto_de_division = 10 % 3


# logicos

_and = True and True # los dos valores deben ser verdaderos
_or = False or True # solo uno tiene que ser verdadero
_not = not True # combierte true a false y viseversa


# comparacion 
# retornan true si se cumple lo comparado o falso si no se cumple
is_igual = 1 == 1 
is_diferente = 2 != 1
is_mayor = 3 > 2 
is_menor = 3 < 4
is_mayor_o_igual = 3 >= 2 
is_menor_o_igual = 2 <= 2 


# asignacion

valor = 2

valor += 1 # cojen el valor de la variable y la aplican la operacion y guardan el resultada en la variable
valor -= 1
valor *= 2
valor **= 2
valor /= 2
valor //= 2
valor %= 3

# identidad

my_other_valor = valor
is_igual = my_other_valor is valor
is_igual = my_other_valor is not valor


# pertenencia 

in_this = 'a' in 'marco'
in_this = 'a' not in 'marco'

# bit

a = 10 # bits 1010
b = 3 # bits 0011
is_good = a & b # 0010
is_good = a | b # 1011
is_good = a ^ b # 1001
is_good = ~b
is_good = a >> 2 # 0010
is_good = a << 2 # 101000



'''
estructuras de control
'''

# condicionales

my_str = 'marco'
if my_str == 'marco':
    print(f'Hi {my_str}')
elif 'json' != my_str:
    print('tu no ers marco')
else:
    print('tu sabras quien eres')

# iterativas

for i in range(6):
    print(i)

i = 10
while i != 0:
    print(i)
    i -= 1

# manejo de exepciones

try:
    number = input('a number ')
    int(number)
except:
    print(' no se pudo conbertir en entero')



# reto extra
for i in range(10, 56):
    if (i % 2 == 0 and i != 16) : 
        print(i)