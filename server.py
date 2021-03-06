# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 22:07:48 2018

@author: gus19
"""

import socket
import sys
import json
import traceback
from thread import *
import threading 
  
print_lock = threading.Lock() 
  
  
def PreguntarATodos(archivo):
    for i in Clientes:
        Preguntar_ip(i,archivo)
def Preguntar_ip(ip, archivo):
    print 'preguntado a ip: '+ip
    
# thread fuction 
def threaded(c): 
    while True: 
  
        # data received from client 
        data = c.recv(1024) 
        if not data: 
            print('Chao') 
              
            # lock released on exit 
            print_lock.release() 
            break
  
        # reverse the given string from client 
        #data = data[::-1] 
        Recibir_Mensaje(c)
        # send back reversed string to client 
        c.send(data) 
  
    # connection closed 
    c.close() 
    

def Start_Server():
    
    print 'Starting Server'
    s = socket.socket()
    host = socket.gethostname()
    port = 12345
    try:
        print 'Binding to the port',port
        s.bind((host, port))
    except:
        print("Bind failed. Error: " + str(sys.exc_info()))
        sys.exit()
    s.listen(5)
    print 'Server now listening...'

    threads = list()    
    
    # Conectando con cliente:
    while True: 
       c, addr = s.accept()
       #print_lock.acquire()
       ip, port2 = str(addr[0]), str(addr[1])
       print 'Got connection from', ip,'at port',port2
       Clientes[ip]=[port2]
       t=threading.Thread(target=Recibir_Mensaje, args=(c,ip,))
       threads.append(t)
       t.start()
    s.close()       
      
      
      
      
def Recibir_Mensaje(c,ip):
       
       # Leyendo el mensaje:
       while True:
           mesage= c.recv(1024)
           if not mesage: 
            print('Chao') 
              
            # lock released on exit 
            print_lock.release() 
            break
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
                      Clientes[ip]=archivo
                      print Clientes[ip]
                      print 'Asking for "' + archivo +'" to other hosts...'
                      PreguntarATodos(archivo)
                      break
                      # TODO: Preguntar a demas clientes:
                      
                      
           else:
               # 3. Si ya se terminó la comunicación:
               if (archivo=='chao'):
                   del Clientes[ip]
                   break
               
               #4. Si es un archivo solicitado:
               print 'Archivo '+ archivo + 'encontrado. Enviando a cliente que lo solicitó.'
               # TODO: Reenviar archivo a cliente que solicitó:
               
           
           
           
        

       
                  
#Main:
Clientes = {}

Start_Server()

