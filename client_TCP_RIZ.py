import socket
import sys
import config as con


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)

sock.connect(server_address)

sock.sendall(con.filename)
#sock.sendall(lastname)

dataIsFileExist = sock.recv(1024000)

if(dataIsFileExist=='True'):
    print 'File already exist. Please select another file name on config.py!'
else:
    f = open(con.filepath, 'r+')
    filecontent = f.read(1024000)
    sock.sendall(filecontent)
    print 'File sent to server using TCP!'

sock.close()
