import socket, time

while True:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect(("192.168.203.187",1290))
    server.send("463032071902".encode())
    data = server.recv(1024)
    print(data.decode())
    server.close()
    time.sleep(5)    