
import requests         #libreria para hhtp
import re

###############################################################################
#Clase encargada de la comunicacion HTTP con el K64                           #
###############################################################################
class Comunicacion():

    server_address = ('192.168.0.245')
    conectado = 0

###############################################################################
# Método constructor de clase. Establece IP                                    #
###############################################################################

    def __init__(self, address):
        self.server_address = address

###############################################################################
# Método que establece IP que tiene el K64 para la comunicación               #
###############################################################################
    def setAddress(self, address):
        self.server_address = address

###############################################################################
# Método que lee el atributo "Conectado". Para saber si hay conexión          #
###############################################################################
    def get_conectado(self):
        return self.conectado

###############################################################################
# Método que setea el atributo "Conectado".                                   #
###############################################################################
    def set_conectado(self, valor):
        self.conectado = valor

###############################################################################
# Método que parsea el cuerpo HTML recibido. Para sacar las etiquetas HTML    #
###############################################################################

    def parse_body(self, body):
        cleanr = re.compile('<.*?>')
        body = re.sub(cleanr, '', body)     # Quita las etiquetas HTML dentro de < >
        return body.split(";")              # retorna el cuempo convertido en lista separada por ";"

###############################################################################
# Método que envia comando HTML al K64. El comando viene en la varible http   #
# retorna el texto HTML de respuesta del K64                                  #
###############################################################################
    def enviarHTTP(self, http):
        try:                                        #Utiliza exepcion por si no hay conexion
            body = requests.get(http, timeout=0.5)  #Envia comando HTTP y genera una exepcion de timeout de 0.5 seg
            self.conectado = 1
            return body.text
        except:                                     # Error de conexión
            print("problemas de conexion")
            self.conectado = 0
            return "Error de conexion"

###############################################################################
# Método que solicita al K64 el valor del contador del Encoder en cuadratura  #
# Retorna el valor del contador y el status del encoder en una lista          #
###############################################################################
    def getCounter(self):
        http = 'http://{}/getCounter()'.format(self.server_address)
        print(http)
        body = self.enviarHTTP(http)
        datos = self.parse_body(body)
        return datos


###############################################################################
# Método que envia el sentido de giro ForWare del encoder al K64              #
# Retorna la respuesta del k64 en una lista                                   #
###############################################################################
    def setCounterForWard(self):
        http = 'http://{}/setCounterForWard()'.format(self.server_address)
        print(http)
        body = self.enviarHTTP(http)
        datos = self.parse_body(body)
        return datos

###############################################################################
# Método que envia el sentido de giro BackWare del encoder al K64             #
# Retorna la respuesta del k64 en una lista                                   #
###############################################################################
    def setCounterBackWard(self):
        http = 'http://{}/setCounterBackWard()'.format(self.server_address)
        print(http)
        body = self.enviarHTTP(http)
        datos = self.parse_body(body)
        return datos


###############################################################################
# Método que envia solicitud de altura Drawork                                #
# Retorna la respuesta del k64 con el valor de la altura en una lista         #
###############################################################################
    def getHeightDrw(self):
        http = 'http://{}/getHeightDrw()'.format(self.server_address)
        body = self.enviarHTTP(http)
        datos = self.parse_body(body)
        return datos

###############################################################################
# Método que envia solicitud de altura en configuracion Lineal del encoder    #
# Retorna la respuesta del k64 con el valor de la altura en una lista         #
###############################################################################
    def getHeightLin(self):
        http = 'http://{}/getHeightLin()'.format(self.server_address)
        body = self.enviarHTTP(http)
        datos = self.parse_body(body)
        return datos

###############################################################################
# Método que envia solicitud de los parametros de calibracion del drawork     #
# Retorna la respuesta del k64 con los valores en una lista                   #
###############################################################################
    def getParametersDrw(self):
        http = 'http://{}/getParametersDrw()'.format(self.server_address)
        body = self.enviarHTTP(http)
        datos = self.parse_body(body)
        return datos

###############################################################################
# Método que envia solicitud de los parametros de calibracion lineal          #
# Retorna la respuesta del k64 con los valores en una lista                   #
###############################################################################
    def getParametersLin(self):
        http = 'http://{}/getParametersLin()'.format(self.server_address)
        body = self.enviarHTTP(http)
        datos = self.parse_body(body)
        return datos

###############################################################################
# Método que envia los parametros geometrico de calibracion del drawork       #
# Retorna la respuesta del k64 en una lista                   #
###############################################################################
    def setGeometry(self, Ppr, DiametroTambor, DiametroCable, Hpc, FactorAparejo):
        http = 'http://{}/setGeometry({},{},{},{},{})'.format(self.server_address,Ppr,DiametroTambor,
                                                              DiametroCable, Hpc, FactorAparejo)
        print (http)
        body = self.enviarHTTP(http)
        datos = self.parse_body(body)
        return datos

###############################################################################
# Método que envia los parametros de calibracion inicial del drawork          #
# Retorna la respuesta del k64 en una lista                                   #
###############################################################################
    def adjust(self, CapasCompletas, Huc, AltRef):
        http = 'http://{}/adjust({},{},{})'.format(self.server_address,CapasCompletas, Huc, AltRef)
        print(http)
        body = self.enviarHTTP(http)
        datos = self.parse_body(body)
        return datos

###############################################################################
# Método que envia el punto de referencia de calibracion para la configuracion#
# lineal del encoder, se utiliza en el en la calibracion por dos punto y en la#
# calibracion de punto y pendiente. Retorna la respuesta del k64 en una lista #                                  #
###############################################################################
    def setRef2(self, altRef2):
        http = 'http://{}/setRef2({})'.format(self.server_address,altRef2)
        print(http)
        body = self.enviarHTTP(http)
        datos = self.parse_body(body)
        return datos

################################################################################
# Método que enviala pendiente de calibracion para la configuracion lineal con #
#la calibración de punto y pendiente. Retorna la respuesta del k64 en una lista#
################################################################################
    def setM(self, m):
        http = 'http://{}/setM({})'.format(self.server_address,m)
        print(http)
        body = self.enviarHTTP(http)
        datos = self.parse_body(body)
        return datos

###############################################################################
# Método que envia el punto de referencia de calibracion para la configuracion#
# lineal del encoder, se utiliza en el en la calibracion por dos punto.       #
# Retorna la respuesta del k64 en una lista                                   #
###############################################################################
    def setRef1(self, altRef1):
        http = 'http://{}/setRef1({})'.format(self.server_address,altRef1)
        print(http)
        body = self.enviarHTTP(http)
        datos = self.parse_body(body)
        return datos

