

"""
cadenas de characteres
"""

# concatenacion

sr1 = "hi"
sr2 = "Mr marco"

sr3 = sr1 + sr2
print(sr3)

# repeticion

print(sr3 * 3)

# indexacion

print(sr3[0])

# longitud

print(len(sr3))

# slicing (porcion)
print(sr3[0:2])

# busqueda

print("hi" if "o" in sr1 else "no esta")

# remplazo
print(sr1.replace("h", "j"))


# division
print(sr1.split("h"))


# mayusculas y minusculas
print(sr2.upper())
print(sr2.lower())
print(sr2.title())
print(sr2.capitalize())


# eleminacion de espacios 
print(" hi espacios ".strip())
print(" hi espacios ".lstrip())
print(" hi espacios ".rstrip())


# busqueda al inicio y al final
print("hi halo".startswith("hi"))
print("hi halo".endswith("lo"))


# busqueda de posicion 
print("hello world".index("w"))
print("hello world".find("w"))


# busqueda de ocurrencias
print("iiii".count("i"))


# formatear una cadena de texto
print(f"saludos : {sr2}")


# transformacion en lista de caracteres
print(list(sr1))

# transformacion de lista a texto
sr4 = ["hi", "ismael"]
print(" ".join(sr4))


# transformacion numerica
sr5 = "12345"
sr5 = int(sr5)
print(type(sr5))


# comprovaciones varias
print(sr2.isalnum())
print(sr2.isalpha())
print(sr2.islower())
print(sr2.isprintable())



""""
exttra
"""


class Polindromo:
    def __init__(self, object):
        self.object = object
        
    def reversed(self):
        obj1 = list(self.object)
        obj2 = list(self.object)

        if obj1 == obj2:
            return True
        else:
            return False


word = Polindromo(input())



if word.reversed():
    print(f"la palabra {word} es un palindromo")








