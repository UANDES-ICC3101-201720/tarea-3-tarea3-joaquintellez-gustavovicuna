# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 22:08:34 2018

@author: gus19
"""
#Create socket: s = socket.socket (socket_family, socket_type, protocol=0)

import socket               # Import socket module

def Solicitar_Archivo(nombre):
    #s = socket.socket()
    #host = socket.gethostname()
    #port = 54321
    
    #s.connect((host,port))
    s.send('0,0,0,'+ nombre)
    
    
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 54321               # Reserve a port for your service.

s.connect((host, port))
print s.recv(1024)
s.send('1,1,0,hola')

Solicitar_Archivo('texto.txt')

print s.recv(1024)