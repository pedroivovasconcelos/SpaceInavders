---INTRUNSTRÇÕES PARA EXECUCAÇÃO DO GAME---

 -Olá defensor da Terra, primeiro é preciso instalar a biblioteca "pyagme",
 que é utilizada para gerar a tela gráfica e acrescentar outras funcionalidades
 ao python. No terminal execute:

    python3 -m pip install -U pygame --user

 Se não tiver python 3 execute no seu terminal(Ubuntu e outras distribuições
 Linux podem vir com python):

   sudo apt-get install python3

 Para executar o servidor, execute a partir do arquivo "servidor_udp.py" com o seguinte comando:
    
    python3 servidor_udp.py

 Para executar o game, execute a partir do arquivo "gamestart.py" com o seguinte comando:

    python3 gamestart.py

 Caso queira executar o game com número de fichas maior e level diferente, execute:

   python3 gamestart.py "fichas" "level"

 *Não se pode começar o game com número de fichas negativo, nem level negativo ou level
  acima de 20, que é o level final
 *Jogo se encerra se as fichas acabarem ou se completar os 20 levéis
 *É necessário instalar python 3.X
 *Versão utilizada no desenvolvimento do jogo é 3.8x64

 Mais Info: https://www.pygame.org/wiki/GettingStarted#Pygame%20Installation