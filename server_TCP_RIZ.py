import socket
import os.path


def isFileNameExist(filename):
    #fullfilepath = 'D:\\' + filename
    if(os.path.isfile(filename)):
        return True
    else:
        return False

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)

sock.bind(server_address)
sock.listen(1)

connection, client_address = sock.accept()

dataFileName = connection.recv(1024000)

if(isFileNameExist(dataFileName)):
    connection.sendall('True')
else:
    connection.sendall('False')

dataFileContent = connection.recv(1024000)

f = open(dataFileName, 'w+')
f.write(dataFileContent)
f.close()

connection.close()