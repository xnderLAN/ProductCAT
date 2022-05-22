import socket
from _thread import *

def threaded_client(connection):
    data = connection.recv(2048).decode()
    print(data)
    connection.send(data[6:8].encode())
    connection.close()

listner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listner.bind(("192.168.203.187",1290))
listner.listen(5)



while True:
    conn, add = listner.accept()
    start_new_thread(threaded_client, (conn, ))
    