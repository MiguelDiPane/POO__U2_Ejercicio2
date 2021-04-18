class ViajeroFrecuente:
    #Atributos:
    __numero = 0
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millas = 0

    #Metodos
    def __init__(self,num=0,dni='',nom='',ap='',mill=0):
        self.__numero = num
        self.__dni = dni
        self.__nombre = nom
        self.__apellido = ap
        self.__millas = mill
        

    def cantidadTotaldeMillas(self):
        return self.__millas
    
    def acumularMillas(self,newMillas):
        if type(newMillas) != type(self.__millas):
            print('Error: Debe ingresar un numero entero de millas.')
        else:
            self.__millas += newMillas
            print('Millas acumuladas exitosamente!')
    
    def canjearMillas(self,cant):
        if type(cant) != type(self.__millas):
            print('Error: Debe ingresar un numero entero de millas.')
        else:
            if cant <= self.__millas:
                self.__millas -= cant
                print('Canje realizado con exito!')
            else:
                print('No dispone de las millas suficientes!')

    def getNumero(self):
        return self.__numero
