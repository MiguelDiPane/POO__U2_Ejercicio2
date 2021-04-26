from claseViajeroFrecuente import ViajeroFrecuente
import re

class ManejadorViajeros:
    #Atributos
    __listaViajeros = []

    #Metodos
    def __init__(self):
        self.__listaViajeros = []
    
    def addViajero(self,num,dni,nom,ap,mill):
        #Comprobacion tipo de datos entero
        if num.isdigit() and mill.isdigit():
            num = int(num)
            mill = int(mill)
            #Comprobacion de strings sin numeros (nombre y apellido)
            if re.search('[\D]',dni) != None: #busco letras o simbolos en el dni
                print('Error al ingresar el dni. Este debe contener solo numeros')
            elif re.search('[\d\_\-\.+*]',nom) != None: #busco numeros o simbolos en el nombre
                print('Error al ingresar el nombre. Este debe contener solo letras')
            elif re.search('[\d\_\-\.+*]',ap) != None:
                print('Error al ingresar el apellido. Este debe contener solo letras')
            else:           
                viajero = ViajeroFrecuente(num,dni,nom,ap,mill)
                self.__listaViajeros.append(viajero)
                print('Viajero creado y agregado a la lista')
        else:
            print('Error: numero o millas no son numeros enteros! El viajero no puede crearse')        

    def getViajero(self,numero):
        if numero.isdigit():
            numero = int(numero)
            bandera = True
            i = 0
            while bandera and i < len(self.__listaViajeros):
                miViajero = self.__listaViajeros[i]
                if numero == miViajero.getNumero():
                    bandera = False #Encontro al viajero
                else:
                    i += 1
            if i == len(self.__listaViajeros):
                i = None
                print('Error: El numero no corresponde a un viajero registrado, reintente.')       
        else:
            print('Error: Debe ingresar un numero entero!')
            i = None
        return i #Retorno posicion en la lista

    def setData(self,pos,operacion):
        print('Viajero: {}'.format(self.__listaViajeros[pos].getNumero()))
        if operacion == 'millas':
            misMillas = self.__listaViajeros[pos].cantidadTotaldeMillas()
            print('Dispone de {} millas en total'.format(misMillas))
        elif operacion == 'acumular':
            newMillas = input('Ingrese millas acumular: ')
            if newMillas.isdigit():
                newMillas = int(newMillas)
                self.__listaViajeros[pos].acumularMillas(newMillas)
            else:
                print('Error: Numero de millas invalido.')
        elif operacion == 'canjear':
            cant = input('Ingrese millas a canjear: ')
            if cant.isdigit():
                cant = int(cant)
                self.__listaViajeros[pos].canjearMillas(cant)
            else:
                print('Error: Numero de millas invalido.')

    def repenMemoria(self):
        print('Lista almacenada en direccion de memoria: {}'.format(hex(id(self.__listaViajeros))))
        for viajero in self.__listaViajeros:
            print('Viajero almacenado en direccion de memoria {}'.format(hex(id(viajero))))