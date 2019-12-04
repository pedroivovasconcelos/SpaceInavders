import socket

HOST = "127.0.0.1"
PORT = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))
cmd = ''


f = open('log.txt','w')

while cmd != 'sair':
    data, addr = sock.recvfrom(4096)
    data = data.decode()
    f.write(data+'\n')
    aux = data.split('Dano: 0')
    if len(aux) > 1:
        cmd = 'sair'
    print("received message:", data)

f.close()