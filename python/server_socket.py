import socket
import sys
from thread import *

HOST=''
PORT=8888

msocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    msocket.bind((HOST,PORT))
except socket.error,msg:
    print 'bind failed. error code:'+str(msg[0])+'\nmessage:'+str(msg[1])
    sys.exit()
print 'mind OK'

msocket.listen(10)
print 'socket listening'

def client_thread(conn):
    conn.send('Welcome to socket server!')

    while True:
        data = conn.recv(1024)
        reply = 'OK...'+data
        if not data:
            break
        conn.sendall(reply)
    conn.close()

while 1:
    conn,addr=msocket.accept()
    print 'connect with '+addr[0]+':'+str(addr[1])

    start_new_thread(client_thread,(conn,))

msocket.close()