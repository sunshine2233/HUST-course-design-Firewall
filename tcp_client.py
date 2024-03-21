from socket import *
 
HOST = '192.168.202.40' 
PORT = 21568
BUFSIZ =1024
ADDR = (HOST,PORT)
 
conn_socket = socket(AF_INET,SOCK_STREAM)
conn_socket.connect(ADDR)
while True:
     data = 'TCP message'
     if not data:
         break
     conn_socket.send(data.encode())
     data = conn_socket.recv(BUFSIZ)
     if not data:
         break
     print("RECV DATA:" + data.decode('utf-8'))
conn_socket.close()
