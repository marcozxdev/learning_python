

import time

productos = {
    1: {'name': 'Javon rey', 'price': 3_000, 'cantidad': 0},
    2: {'name': 'Arroz', 'price': 2_500, 'cantidad': 0},
    3: {'name': 'Carne', 'price': 22_000, 'cantidad': 0},
    4: {'name': 'Panela', 'price': 5_700, 'cantidad': 0},
    5: {'name': 'Avena', 'price': 3_000, 'cantidad': 0},
}

def add_product(name, price):
    # nota: mas tarde marco, debes implementar la opcion de añadir productos
    pass


def operacion_para_pagar(total):
    print(f'total ${total}')
    while True:
        try:
            cantidad = int(input('ingrese el dinero $ '))
            print()
            if not cantidad:
                print('asegurese de poner un monto\n')
                time.sleep(1.5)
            if cantidad < total:
                print(f'pagastte con {cantidad} pero el total es {total}\nel  dinero es insuficiente\n')
                time.sleep(1.5)
                
            elif cantidad > total or cantidad == total:
                devuelta = cantidad - total
                print(f'pagaste con {cantidad} y tu devuelta es de {devuelta}')
                print('feliz dia adios')
                return
        except ValueError:
            print('\nasegurese de solo escribir numeros')

def borrar_cantidad():
    for i in productos:
        productos[i]['cantidad'] = 0
    return


def generar_factura():
    
    try:
        while True:
            precio_total = 0
            print('\nSu Factura:\n')
            for i in productos:
                nombre = productos[i]['name']
                cantidad = productos[i]['cantidad']
                precio = productos[i]['price']
                total = 0 if cantidad == 0 else precio * cantidad
                precio_total += total
                print(f"{nombre} unds {cantidad} : ${total}")

            print(f'su total es de {precio_total}')
            print("1.Pagar pedido\n2.Cancelar pedido")
            opc = int(input(': '))
            
            if opc == 1:
                operacion_para_pagar(precio_total)
                print('bye..')
                return
            elif opc == 2:
                borrar_cantidad()
                return
            else:
                print("asegurese de elegir una opcion")

            time.sleep(3.0)
    except ValueError:
        print("solo se admiten numeros")


def validar_opc_y_añadir(opc):

    
    if opc in productos:
        productos[opc]['cantidad'] += 1
    else:
        print('\nAsegurese de poner solo numeros y en el rango establecido\n ')
        time.sleep(3.0)


def menu():

        while True: 
            print('\nBienvenido a Mercatodo\nQue desea llevar? || Cantidad de productos que as seleccionados')
            for i in productos:
                print(f"{i}. {productos[i]['name']}  ${productos[i]['price']}  Cantidad: {productos[i]['cantidad']}")
                
            try:
                salir = len(productos) + 1
                pagar = len(productos) + 2
                print(f"{salir}.salir")
                print(f"{pagar}.Generar factura")
                opc = int(input(':'))

                if opc == salir:
                    print('saliendo...')
                    time.sleep(1.0)
                    return
                elif opc == pagar:
                    generar_factura()
                    return
                else:
                    validar_opc_y_añadir(opc)
                    
            except ValueError:
                print("Asegurese de poner solo numeros\n")


menu()