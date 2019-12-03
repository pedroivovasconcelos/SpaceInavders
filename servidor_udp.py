import socket

HOST = "127.0.0.1"
PORT = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))
 
while True:
    data, addr = sock.recvfrom(4096)
    data = data.decode()
    print ("received message:", data)