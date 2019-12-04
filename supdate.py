import pygame, sys, time, gamestart

black = 0, 0, 0

def screenupdate(gv):
    screen = gv.screen
    font = pygame.font.Font('freesansbold.ttf', 16)
    
    while True:
        time.sleep(gv.fps)
        playerdict = gv.playerdict
        aliendict = gv.aliendict
        obstaclelist = gv.obstaclelist
        screen.fill(black)

        if not aliendict == False:
            if 'alien' in aliendict and len(aliendict['alien'][1]) != 0:
                for aliens in aliendict['alien'][1]:
                    screen.blit(aliendict['alien'][0], aliens)
            if 'laser' in aliendict and len(aliendict['laser'][1].keys()) != 0:
                for lasers in aliendict['laser'][1].values():
                    screen.blit(aliendict['laser'][0], lasers)

        if not obstaclelist == False:
            if len(obstaclelist) != 0:
                for obstacle in obstaclelist:
                    screen.blit(obstacle[0],obstacle[2])

        if not playerdict == False:
            if 'player' in playerdict:
                screen.blit(playerdict['player'][0],playerdict['player'][1])

            if 'shoots' in playerdict and len(playerdict['shoots'][1]) != 0:
                for shoots in playerdict['shoots'][1]:
                    screen.blit(playerdict['shoots'][0], shoots)

        credittext = str(gv.creditgame) + ' X CREDITS'
        text = font.render(credittext, True, [255,255,255], None)
        textrect = text.get_rect()
        textrect = textrect.move(20,475)
        screen.blit(text,textrect) 
    
        credittext = str(gv.score) + ' SCORE'
        text = font.render(credittext, True, [255,255,255], None)
        textrect = text.get_rect()
        textrect = textrect.move(200,475)
        screen.blit(text,textrect) 

        pygame.display.flip()