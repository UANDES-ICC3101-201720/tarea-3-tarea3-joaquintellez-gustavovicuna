# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 20:36:40 2018

@author: gus19
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 22:08:34 2018

@author: gus19
"""
#Create socket: s = socket.socket (socket_family, socket_type, protocol=0)

import socket               # Import socket module

def Recibir_Mensaje():
    
    message=s.recv(1024)
    print 'Recibiendo mensaje: '+ message
    message= message.split(',')
    syn, ack, modo, archivo= int(message[0]), int(message[1]), int(message[2]), message[3]
    
    #1. En caso de recibir un mensaje de no encontrado:
    if (archivo=='404'):
        print 'El archivo no fue encontrado :('
    #2. Si es un handshake:
    if (ack==1):
        return 1
    else:
        # 3. Si es una solicitud del server:
        if (modo==1):
            print 'Buscando archivo...\n'
            # TODO: Buscar archivo y enviarlo de vuelta:
            
            
        # 4. Si es el archivo solicitado:
        else:
            print 'Archivo recibido :)'
            print archivo

def Solicitar_Archivo(nombre):
    #s = socket.socket()
    #host = socket.gethostname()
    #port = 54321
    
    #s.connect((host,port))
    s.send('1,0,1,'+ nombre)

def Desconectar():
    s.send('0,0,0,chao')
    s.close()

def Conectar():

    host = socket.gethostname() # Get local machine name
    port = 54321               # Reserve a port for your service.
    s.connect((host, port))

#Main:
s = socket.socket()         # Create a socket object
Conectar()

while True:
    opc=input("1. Solicitar archivo\n0. Terminar conexión\n")
    if opc==0:
        Desconectar()
        break
    else:
        n_archivo=raw_input("Ingrese nombre del archivo solicitado: ")
        Solicitar_Archivo(n_archivo)
        while True:
            hs=Recibir_Mensaje()
            if hs:
                s.send('0,0,1,'+n_archivo)
            else:
                break