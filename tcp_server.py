#!/usr/bin/python
#coding:utf-8
 
from socket import *
HOST = '192.168.202.40'   #不指定的话就默认'localhost' 
PORT = 21568 #监<e5><80>大长度
BUFSIZ = 1024  #指定接收TCP消息的最大长度
ADDR = (HOST,PORT) #
 
#listSock是服务端的监听socket
listSock = socket(AF_INET,SOCK_STREAM) #不指定参数默认为:AF_INET,SOCK_STREAM
listSock.bind(ADDR) #将主机号、端口号绑定到套接字
listSock.listen(5)  #开启TCP监听
 
while True:
    print('等待链接...')
    #connSock是连接socket 其实就是一个具体的socket连接.
    connSock, addr = listSock.accept()
    print('...连接来自:', addr)
 
    while True:
        data = connSock.recv(BUFSIZ)
        print("接受信息:",data)
        if not data:
            break
        #prefix = b'reply:'
        rsp = data.upper()
        connSock.send(rsp)
        '''
        注意:下面打出来的并不一定是每次真正send回去的字符串,尤其是bufsize小于收发字符串大小的时候
        '''
        #print("send back:",rsp)
    connSock.close()
listSock.close()
