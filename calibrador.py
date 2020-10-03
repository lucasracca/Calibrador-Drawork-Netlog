import sys
import datetime
import time
from comunicacion import *

###############################################################################
def EnviarGeometria():
     inPpr = input('Ingrese PPR\n')
     try:
         ppr = int(inPpr)
     except ValueError:
         print("Ppr no es un entero")
         return

     inDiametro = input('Ingrese Diametro del tambor\n')
     try:
        diametro = float(inDiametro)
     except ValueError:
         print("Diametro tambor no es un real")
         return

     inCable = input('Ingrese Diametro del cable\n')
     try:
         cable = float(inCable)
     except ValueError:
        print("Diametro cable no es un real")
        return

     inAparejo = input('Ingrese Factor de aparejo\n')
     try:
        aparejo = float(inAparejo)
     except ValueError:
        print("Lineas del aparejo no es un real")
        return

     inHpc = input('Ingrese hiladas por capa\n')
     try:
        hpc = int(inHpc)
     except ValueError:
        print("Hpc no es un entero")
        return

     rta = comm.setGeometry(str(ppr), str(diametro), str(cable), str(hpc), str(aparejo))
     print(rta[0])
     print(hora())

###############################################################################
def EnviarAjuste():
    inAltura =input('Ingrese Altura Inicial\n')
    try:
         altura = float(inAltura)
    except ValueError:
        print("Altura de referencia no es un real")
        return
    inCapas = input('Ingrese Capas completas\n')
    try:
        capas = int(inCapas)
    except ValueError:
        print("Capas completas no es un entero")
        return
    inHiladas = input('Ingrese Hiladas en ultima capa\n')
    try:
        hiladas = int(inHiladas)
    except ValueError:
        print("Cantidad de Hiladas Última capa no es un entero")
        return
    rta =comm.adjust(str(capas), str(hiladas), str(altura))
    print(rta[0])
    print(hora())

###############################################################################
def EnviarPyM():
    inM = input('Ingrese Pendiente M\n')
    inP = input('Ingrese Punto 1\n')
    try:
        m = float(inM)
    except ValueError:
        print("Pendiente M no es un real")
        return
    try:
        n = float(inP)
    except ValueError:
        print("Punto 1 no es un real")
        return

    rta = comm.setRef2(str(n))
    print(rta[0])
    print(hora())
    rtastr = ','.join(rta)

    if 'Operación Realizada.' in rtastr :
        rta = comm.setM(str(m / 4))
        print(rta[0])
        print(hora())

###############################################################################
def EnviarPunto1():
    inPto1 =input('Ingrese Altura Referencia 1\n')
    try:
        pto1 = float(inPto1)
    except ValueError:
        print("Altura Referencia 1 no es un real")
        return
    rta = comm.setRef2(str(inPto1))
    print(rta[0])
    print(hora())

###############################################################################
def EnviarPunto2():
    inPto2 = input('Ingrese Altura Referencia 2\n')
    try:
        pto2 = float(inPto2)
    except ValueError:
        print("Altura Referencia 2 no es un real")
        return
    rta = comm.setRef1(str(inPto2))
    rtastr = ','.join(rta)
    if 'ERROR X2-X1 es igual a 0' in rtastr:
        print("El punto 2 se encuentra en la misma posicion que el punto 1" )
    else:
        print(rta[0])

###############################################################################
def LeerContador():
    contador = comm.getCounter()
    try:
        print(" El valor de contador es :",contador[0][8::], "\n\r El estado es:",contador[1])
    except:
        print(contador)
###############################################################################
def SentidoGiro():

    giro= input('Ingrese sentido de giro\n 1 para ForWare \n 2 para BackWare\n')
    if (giro == '1'):
        sentido = comm.setCounterForWard()
        print(sentido[0])
    elif (giro == '2'):
            sentido = comm.setCounterBackWard()
            print(sentido[0])
    else:
        print('Opcion ingresada invalida')

###############################################################################
def LeerAlturaDrw():
    altura = comm.getHeightDrw()
    try:
        print("Altura:",(altura[2][:-5]), "cm")
    except:
        print(altura)
###############################################################################
def LeerParametrosDrw():
    parametros = comm.getParametersDrw()
    try:
        ppr = int(parametros[0]) / 4
        print("PPR: ",ppr, '\nDiametro Tambor:', parametros[1][:-2],
              '\nDiametro Cable:', parametros[2][:-2],'\nHiladas por capas:',
              parametros[3],'\nFactor de Aparejo:', parametros[4][:-3], 
              '\nEstado:', parametros[5])
    except:
        print(parametros)
###############################################################################
def LeerAlturaLin():
    altura = comm.getHeightLin()
    try:
        print("Altura:",(altura[2][:-5]), "cm")
    except:
        print(altura)
###############################################################################
def LeerParametrosLin():
    parametros = comm.getParametersLin()
    try:
        m = float(parametros[3]) * 4
        print("Punto 1: ", parametros[0][:-5], '\nPendiente:', str(m), '\nEstado:',
              parametros[4])
    except:
        print('Pendiente no es un numero')


###############################################################################
def hora():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%d/%m/%Y %H:%M:%S')
    return st

###############################################################################
def EnviarPuntos():
    EnviarPunto1()
    EnviarPunto2()

###############################################################################
def error():
   print("Opción no valida")

###############################################################################

comm = Comunicacion('192.168.0.245')
dic ={
    '1': LeerAlturaLin,
    '2': LeerParametrosLin,
    '3': LeerAlturaDrw,
    '4': LeerParametrosDrw,
    '5': LeerContador,
    '6': SentidoGiro,
    '7': EnviarGeometria,
    '8': EnviarAjuste,
    '9': EnviarPyM,
    '10': EnviarPuntos
    }
while True:
    opcion = input("\n\nIngrese una opción\n"
                   "1 Leer Altura Linial\n"
                  "2 Leer Parametros Lineal\n"
                   "3 Leer Altura Drawork\n"
                  "4 Leer Parametros  Drawork\n"
                  "5 Leer Contador\n"
                  "6 Establecer sentido de giro\n"
                  "7 Enviar Geometria\n"
                  "8 Enviar Ajuste\n"
                  "9 Enviar Punto y Pendiente\n"
                  "10 Enviar 2 puntos\n"
                  "s Salir\n")

    if(opcion=='s'):
        break
    dic.get(opcion, error)()

    conexion = comm.get_conectado()
    if (conexion == 1):
        print('CONECTADO')
    else:
        print('DESCONECTADO')
