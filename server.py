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
    while True: #revisar
        c, addr = s.accept()
        ip, port2 = str(addr[0]), str(addr[1])
        print 'Got connection from', ip,'at port',port2
        c.send('Thank you for connecting')
        #s.close()
        
        Recibir_mensaje(c)
    
       
def Recibir_mensaje(c):
       # Leyendo el mensaje:
       print 'Leyendo...'
       
       #c.send('Thank you for connecting')
       #while True:
        #   Recibir_mensaje(c)
       #s.listen(5)
       
       mesage= c.recv(1024)
       mesage= mesage.split(',')
       syn, ack, modo, archivo= int(mesage[0]), int(mesage[1]), int(mesage[2]), mesage[3]
       
       #Accion dependiendo del mensaje:
       #Si es un archivo:
       if (modo==0):
           # Verificando handshake:
              if (syn==1):
                  if (ack==0):
                      print 'Error with handshake. Sending message again.'
                  else:
                      syn=0
                      ack=0
       mens = str(syn) + ' ' + str(ack) + ' ' + str(modo) + ' ' + archivo              
       c.send(mens)               
       print syn, ack, modo, archivo
      
       
                  


#Main:

Start_Server()

