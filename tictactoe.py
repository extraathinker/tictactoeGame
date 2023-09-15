import pygame

pygame.init()

status10 = False


def play():
    global status10
    status10 = False
    screen = pygame.display.set_mode((600,700))
    pygame.display.set_caption('Tic Tac Toe')


    box1 = pygame.Rect(0,0,200,200)
    status1 = 'empty'
    box2 = pygame.Rect(200, 0, 200, 200)
    status2 = 'empty'
    box3 = pygame.Rect(400, 0, 200, 200)
    status3 = 'empty'
    box4 = pygame.Rect(0, 200, 200, 200)
    status4 = 'empty'
    box5 = pygame.Rect(200, 200, 200, 200)
    status5 = 'empty'
    box6 = pygame.Rect(400, 200, 200, 200)
    status6 = 'empty'
    box7 = pygame.Rect(0, 400, 200, 200)
    status7 = 'empty'
    box8 = pygame.Rect(200, 400, 200, 200)
    status8 = 'empty'
    box9 = pygame.Rect(400, 400, 200, 200)
    status9 = 'empty'
    box10 = pygame.Rect(0, 600, 400, 100)
    
    box11 = pygame.Rect(400, 600, 200, 100)

    def drawLine(x1,y1,x2,y2):
        pygame.draw.line(screen,(255,255,0),(x1,y1),(x2,y2),width=2)


    def writeText(tex,x,y,a):
        textFont = pygame.font.Font('freesansbold.ttf',a)
        texts = textFont.render(tex,True, (255,255,255))
        screen.blit(texts,(x,y))
    def checkWin():
        global status10
        if ((status1 == 'X' and status2 == 'X' and status3 == 'X') or 
        (status4 == 'X' and status5 == 'X' and status6 == 'X') or 
        (status7 == 'X' and status8 == 'X' and status9 == 'X') or
        (status1 == 'X' and status4 == 'X' and status7 == 'X') or
        (status2 == 'X' and status5 == 'X' and status8 == 'X') or 
        (status3 == 'X' and status6 == 'X' and status9 == 'X') or 
        (status1 == 'X' and status5 == 'X' and status9 == 'X') or
        (status3 == 'X' and status5 == 'X' and status7 == 'X')):
            if not status10:
                writeText('player2 wins!',60,630,30)
                status10 = True
        elif ((status1 == 'O' and status2 == 'O' and status3 == 'O') or 
        (status4 == 'O' and status5 == 'O' and status6 == 'O') or 
        (status7 == 'O' and status8 == 'O' and status9 == 'O') or
        (status1 == 'O' and status4 == 'O' and status7 == 'O') or
        (status2 == 'O' and status5 == 'O' and status8 == 'O') or 
        (status3 == 'O' and status6 == 'O' and status9 == 'O') or 
        (status1 == 'O' and status5 == 'O' and status9 == 'O') or
        (status3 == 'O' and status5 == 'O' and status7 == 'O')):
            if not status10:
                writeText('player1 wins!',60,630,30)
                status10 = True

    player = 'player1'


    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if box1.collidepoint(event.pos) and status1 not in ['X','O']:
                    if player == 'player1':
                        writeText('O',60,60,100)
                        player = 'player2'
                        status1 = 'O'
                    else:
                        writeText('X',60,60,100)
                        player = 'player1'
                        status1 = 'X'
                if box2.collidepoint(event.pos) and status2 not in ['X','O']:
                    if player == 'player1':
                        writeText('O',260,60,100)
                        player = 'player2'
                        status2 = 'O'
                    else:
                        writeText('X',260,60,100)
                        player = 'player1'
                        status2 = 'X'
                if box3.collidepoint(event.pos) and status3 not in ['X','O']:
                    if player == 'player1':
                        writeText('O',460,60,100)
                        player = 'player2'
                        status3 = 'O'
                    else:
                        writeText('X',460,60,100)
                        player = 'player1'
                        status3 = 'X'
                if box4.collidepoint(event.pos) and status4 not in ['X','O']:
                    if player == 'player1':
                        writeText('O',60,260,100)
                        player = 'player2'
                        status4 = 'O'
                    else:
                        writeText('X',60,260,100)
                        player = 'player1'
                        status4 = 'X'
                if box5.collidepoint(event.pos) and status5 not in ['X','O']:
                    if player == 'player1':
                        writeText('O',260,260,100)
                        player = 'player2'
                        status5 = 'O'
                    else:
                        writeText('X',260,260,100)
                        player = 'player1'
                        status5 = 'X'
                if box6.collidepoint(event.pos) and status6 not in ['X','O']:
                    if player == 'player1':
                        writeText('O',460,260,100)
                        player = 'player2'
                        status6 = 'O'
                    else:
                        writeText('X',460,260,100)
                        player = 'player1'
                        status6 = 'X'
                if box7.collidepoint(event.pos) and status7 not in ['X','O']:
                    if player == 'player1':
                        writeText('O',60,460,100)
                        player = 'player2'
                        status7 = 'O'
                    else:
                        writeText('X',60,460,100)
                        player = 'player1'
                        status7 = 'X'
                if box8.collidepoint(event.pos) and status8 not in ['X','O']:
                    if player == 'player1':
                        writeText('O',260,460,100)
                        player = 'player2'
                        status8 = 'O'
                    else:
                        writeText('X',260,460,100)
                        player = 'player1'
                        status8 = 'X'
                if box9.collidepoint(event.pos) and status9 not in ['X','O']:
                    if player == 'player1':
                        writeText('O',460,460,100)
                        player = 'player2'
                        status9 = 'O'
                    else:
                        writeText('X',460,460,100)
                        player = 'player1'
                        status9 = 'X'
                if box11.collidepoint(event.pos):
                    play()

        
        checkWin()    
        writeText('New',430,630,50)
        drawLine(200,0,200,600)
        drawLine(400,0,400,600)
        drawLine(0,200,600,200)
        drawLine(0,400,600,400)
        drawLine(0,600,600,600)
        drawLine(400,600,400,700)
        pygame.display.update()

play()