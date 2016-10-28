import socket
import sys

try:
    msocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error,msg:
    print 'failed to create socket, error code'+msg[0]+'\nerror message:'+msg[1]
    sys.exit();
print 'socket created'

host='www.zhihu.com'
port=80

try:
    remote_ip=socket.gethostbyname(host)
except socket.gaierror:
    print 'failed to resolve host name'
    sys.exit();

print 'IP addr of '+host+' is '+remote_ip 

msocket.connect((remote_ip,port))
print 'Socket Connected to ' + host + ' on ip ' + remote_ip

message="GET / HTTP/1.1\r\n\r\n"

try:
    msocket.sendall(message)
except socket.error:
    print 'send failed'
    sys.exit()

print 'message send successfully'

while 1:
    reply=msocket.recv(4096)
    if not reply:
        break
    print reply

msocket.close()