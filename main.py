from claseManejadorViajeros import ManejadorViajeros
from claseMenu import Menu
import time
import csv

#Funcion test para testear la creacion de viajeros
def test():
    nombreArch = 'viajerosTest.csv'
    print('Lectura de archivo: {}'.format(nombreArch))
    archivo = open(nombreArch)
    reader = csv.reader(archivo,delimiter=',')
    manejadorTest = ManejadorViajeros()
    bandera = True
    for fila in reader:
        if bandera:
            bandera = False
        else:     
            numero = fila[0]
            dni = fila[1]
            nombre = fila[2]
            apellido = fila[3]
            millas = fila[4]
            print('Datos viajero: {}'.format(fila))
            time.sleep(0.5)
            manejadorTest.addViajero(numero,dni,nombre,apellido,millas)
    archivo.close()

if __name__ == '__main__':
    manejadorCreado = False
    menuPrincipal = Menu()
    menuPrincipal.define_menu(['[1]- Actividad 1','[2]- Actividad 2','[3]- Actividad 3','[4]- Ejecutar funcion test','[0]- Salir'])
    menuPrincipal.showMenu()
    opcion = menuPrincipal.selectOption()
    manejador = ManejadorViajeros()
    while(opcion != 0):
        #Apartado 1
        if opcion == 1:    
            nombreArch = 'viajeros.csv'
            print('Lectura de archivo: {}'.format(nombreArch))
            archivo = open(nombreArch)
            reader = csv.reader(archivo,delimiter=',')
            bandera = True
    
            for fila in reader:
                if bandera:
                    bandera = False
                else:
                    numero = fila[0]
                    dni = fila[1]
                    nombre = fila[2]
                    apellido = fila[3]
                    millas = fila[4]
                    manejador.addViajero(numero,dni,nombre,apellido,millas)
            archivo.close()
            input('Presione ENTER para volver al menu...')

        #Apartado 2
        elif opcion == 2:
            numero = input('Ingrese numero viajero frecuente: ')
            pos = manejador.getViajero(numero)
            if pos != None:
                menuSecundario = Menu()
                menuSecundario.define_menu(['[1]- Consultar cantidad de millas','[2]- Acumular millas','[3]- Canjear millas','[0]- Volver a menu principal'])
                menuSecundario.showMenu()
                opcion2 = menuSecundario.selectOption()
                while opcion2 != 0:     
                    if opcion2 == 1:
                        manejador.setData(pos,'millas')
                    elif opcion2 == 2:
                        manejador.setData(pos,'acumular')
                    elif opcion2 == 3:
                        manejador.setData(pos,'canjear')
                    input('Presione ENTER para continuar...')
                    menuSecundario.showMenu()
                    opcion2 = menuSecundario.selectOption()
            input('Presione ENTER para volver al menu...')

        #Apartado 3
        elif opcion == 3:
            #Mostrar el almacenamiento en memoria para la lista cargada con 4 viajeros
            #Cargo lista con 4 viajeros
            manejador = ManejadorViajeros() 
            nombreArch = 'viajeros.csv'
            print('Lectura de archivo: {}'.format(nombreArch))
            archivo = open(nombreArch)
            reader = csv.reader(archivo,delimiter=',')
            bandera = True
            cont = 0
            for fila in reader:
                if bandera:
                    bandera = False
                else:
                    numero = fila[0]
                    dni = fila[1]
                    nombre = fila[2]
                    apellido = fila[3]
                    millas = fila[4]
                    manejador.addViajero(numero,dni,nombre,apellido,millas)
                    cont += 1
                    if cont == 5:
                        break 
            archivo.close()
            manejador.repenMemoria()
            input('Presione ENTER para volver al menu...')

        #Funcion test
        elif opcion == 4:
            test()
            input('Presione ENTER para volver al menu...')

        else:
            input('Presione ENTER para volver al menu...')
        menuPrincipal.showMenu()
        opcion = menuPrincipal.selectOption()
        