

def is_str(*valuess):

    if type(valuess[0]) == list:
        values = valuess[0]
    else:
        values = list(valuess)
        




def to_int_float(type='int', *values):
    pass





def operation(operation: str='_', *numberss):
    
    if type(numberss[0]) == list:
        numbers = numberss[0]
    else:
        numbers = list(numberss)

    if 0 in numbers: # esto valida que no alla 0 y los elimina en caso tal de que esten
        for i in numbers:
            if i == 0 or i == 0.0:
                numbers.remove(0)

    if len(numbers) <= 1 : # valida que cuando se llame la funciona alla al menos un numero + o -
        return 'I need more numbers (> 0 or < 0 "not 0")'
    

    resultado = numbers[0] 
    numbers.pop(0)
    
    match operation: # logica de las operaciones dependiendo de el parametro
        case '+':
            for i in numbers:
                resultado += i
            return resultado
        case '-':
            for i in numbers:
                resultado -= i
            return resultado
        case '*':
            for i in numbers:
                resultado *= i
            return resultado
        case '/':
            for i in numbers:
                resultado /= i
            return resultado
        case _ : # retorna en caso tal de que la operacion no exista o 
            return 'no have operation or no suport operation'

def suma(*numbers):
    if not numbers:
        return 'this def no have numbers'
    return  operation('+', *numbers)
suma()

def resta(*numbers):
    if not numbers:
        return 'this def no have numbers'
    return operation('-', *numbers)

def multiplica(*numbers):
    if not numbers:
        return 'this def no have numbers'
    return operation('*', *numbers)

def division(*numbers):
    if not numbers:
        return 'this def no have numbers'
    return operation('/', *numbers)

# print(suma(1, 1, 1, 1, 1, 1))

# print(resta(1, 2, 0))

# print(multiplica(0, 2))

# print(division(0, 0, 0))

# numbers = [1, 2]
# resultado = numbers[0]
# numbers.pop(0)
# for i in numbers:
#     resultado += i

# print(resultado)