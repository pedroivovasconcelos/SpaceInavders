import socket, sys, gamestart, time, datetime

def comunicacao(gv):
    HOST = '127.0.0.1'
    PORT = 5000
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(('Início: ' + gv.inicio.strftime("%d/%m/%Y, %H:%M:%S")).encode(), (HOST, PORT))
    agora = round(time.time()*1000)
    creditos_atuais = gv.creditgame
    print('Ativo')
    while(gv.fim == None):
        if (round(time.time()*1000) - agora) >= 5000:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(('Placar: ' + str(gv.score)).encode(), (HOST, PORT))
            agora = round(time.time()*1000)
            time.sleep(.01)
        if(gv.creditgame != creditos_atuais):
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto( ('Dano: ' + str(gv.creditgame) + ' Momento: '+datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S") ).encode() , (HOST, PORT))
            agora = round(time.time()*1000)
            creditos_atuais = gv.creditgame
            time.sleep(.01)
    print('Saí do loop')
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto('Término: ' + gv.fim.strftime("%d/%m/%Y, %H:%M:%S\\1").encode(), (HOST, PORT))