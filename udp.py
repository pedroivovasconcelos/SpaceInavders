import socket, sys, gamestart, time

def comunicacao(gv):
    HOST = '127.0.0.1'
    PORT = 5000
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(gv.inicio.strftime("%d/%m/%Y, %H:%M:%S").encode(), (HOST, PORT))
    agora = round(time.time()*1000)
    print('Ativo')
    while(gv.fim == None):
        #Obtem os segundos atuais
        HOST = '127.0.0.1'
        PORT = 5000
        if (round(time.time()*1000) - agora) >= 5000:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto('Placeholder'.encode(), (HOST, PORT))
            agora = round(time.time()*1000)