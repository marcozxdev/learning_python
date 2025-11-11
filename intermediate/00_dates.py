
## dates ##

from datetime import datetime # libreria del sistema para manejar fechas y horas


date_now = datetime.now() # se inicializa el objeto tipo datetime.now() para mostrar la hora actual

date_future = datetime(2026, 9, 17) # se crea el objeto con unas fechas definidas 

date_timestamp = date_now.timestamp() # retorna el poxis para guardar el codigo de la fecha en float


def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)         # funcion para imprimir la fecha con todo incluido el tiempo y poxis en float
    print(date.minute)
    print(date.second)
    print(date.timestamp())


print_date(date_now)
print_date(date_future)


print("######################################")

from datetime import time

current_time = time(6, 9, 24)

print(current_time.hour)
print(current_time.minute)  # en el modulo time la clase time(toca darle el tiempo como parametro) ya que la clase solo sirve para dale el formato
print(current_time.second)       
print(current_time.microsecond)
print(current_time)


print("############################")

from datetime import date


current_date = date(2026, 9 , 17) # en este modulo date tambien toca darle la fecha como parametro ya que el solo se encarga de formatearla

print(current_date)





