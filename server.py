# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 22:07:48 2018

@author: gus19
"""

import socket
import sys
import json
import traceback
    

def Start_Server():
    
    print 'Starting Server'
    s = socket.socket()
    host = socket.gethostname()
    port = 54321
    try:
        print 'Binding to the port',port
        s.bind((host, port))
    except:
        print("Bind failed. Error: " + str(sys.exc_info()))
        sys.exit()
    s.listen(5)
    print 'Server now listening...'
    
    # Conectando con cliente:
    while True: 
       c, addr = s.accept()
       ip, port2 = str(addr[0]), str(addr[1])
       print 'Got connection from', ip,'at port',port2
       Recibir_Mensaje(c)       
       
def Recibir_Mensaje(c):
       
       # Leyendo el mensaje:
       while True:
           mesage= c.recv(1024)
           print 'Message recieved: '+ mesage
           mesage= mesage.split(',')
           syn, ack, modo, archivo= int(mesage[0]), int(mesage[1]), int(mesage[2]), mesage[3]
           
           #Accion dependiendo del mensaje:
           #1. Si es una solicitud:
           if (modo==1):
               # 2. Verificando handshake:
                  if (syn==1):
                      if (ack==0):
                          syn=1
                          ack=1
                          mens = str(syn) + ',' + str(ack) + ',' + str(modo) + ',' + archivo              
                          c.send(mens)  
                      else:
                          print 'Error en handshake. Se perdió la conección?'
                  else:
                      print 'Asking for "' + archivo +'" to other hosts...'
                      # TODO: Preguntar a demas clientes:
                      
                      
           #3. Si es un archivo solicitado:
           else:
               print 'Archivo '+ archivo + 'encontrado. Enviando a cliente que lo solicitó.'
               # TODO: Reenviar archivo a cliente que solicitó:
               
           
           
           # 4. Si ya se terminó la comunicación:
           if (archivo=='chao'):
               break

       
                  
#Main:

Start_Server()

