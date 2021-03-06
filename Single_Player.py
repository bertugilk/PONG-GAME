import pygame
import sys
import random
import Single_Finish

pygame.init()

screen_width = 1200
screen_heigth = 600
size = (screen_width, screen_heigth)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("PONG-GAME")
logo = pygame.image.load("Images/logo.jpg")
pygame.display.set_icon(logo)


# Colors:
black = (0, 0, 0)
chocalate = (210, 105, 30)
white = (255, 255, 255)
green = (0, 128, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
aqua = (0, 255, 255)
yellow = (255, 255, 0)
purple = (255, 0, 255)
orange = (255, 165, 0)
lime = (0, 255, 0)
gold = (255, 215, 0)
salmon = (250, 128, 114)
deepPink = (255, 0, 127)
brown = (204, 102, 0)
deepPurple = (138, 36, 114)

clock = pygame.time.Clock()


class texts():
    def write(self, message, color, x, y, size):
        self.message = message
        self.color = color
        self.x = x
        self.y = y
        self.size = size
        font = pygame.font.SysFont(None, size)
        text = font.render(message, True, color)
        screen.blit(text, [x, y])


class Pause():
    def pause(self):
        bg = pygame.image.load("Images/bgfinish.jpg")
        paused = True
        pygame.mixer_music.load("Music/intro_music.mp3")
        pygame.mixer_music.play(0)
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        size_pause = (1200, 600)
                        pygame.display.set_mode(size_pause)
                        paused = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    elif event.key==pygame.K_m:
                        pygame.display.set_mode((1000,600))
                        import Intro
                        intr=Intro.Intro()
                        intr.intro()

            screen.fill((0, 0, 0))
            screen.blit(bg,(0,0))
            txt = texts()
            txt.write("- PAUSE -", aqua, 200, 80, 120)
            txt.write("- SPACE TO CONTINUE", red, 200, 250, 50)
            txt.write("- Q TO EXIT", red, 200, 350, 50)
            txt.write("- M TO MENU", red, 200, 450, 50)
            pygame.display.update()
            clock.tick(5)

class singlePlayer_game_loop():
    def singleGame(self):
        pause = pygame.image.load("Images/pause3.png")
        ball = pygame.image.load("Images/ball2.png")

        playerX = 60
        playerY = 260
        pcX = 1100
        pcY = 260
        player_score=0
        pc_score=0
        ballX = 570
        ballY = 220
        ballMovingX = 10
        ballMovingY = -10

        counter, counterText = 60, '60'.rjust(3)
        pygame.time.set_timer(pygame.USEREVENT, 1000)

        pygame.mixer_music.load("Music/game_music.mp3")
        pygame.mixer_music.play(0)

        fnsh=Single_Finish.Single_Finish()

        pygame.key.set_repeat(10, 10)
        while True:
            key = pygame.key.get_pressed()
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.USEREVENT:
                    counter -= 1
                    counterText = str(counter).rjust(3) if counter > 0  else fnsh.Finish() if pygame.display.set_mode((800,500)) and pygame.mixer_music.stop() else fnsh.Finish()
                if event.type == pygame.KEYDOWN:
                    if key[pygame.K_p]:
                        size_pause = (800, 600)
                        pygame.display.set_mode(size_pause)
                        ps=Pause()
                        ps.pause()
                    if key[pygame.K_UP]:
                        playerY -= 10
                    if key[pygame.K_DOWN]:
                        playerY += 10


            screen.fill(black)
            pygame.draw.rect(screen,deepPink,(0,0,600,5))
            pygame.draw.rect(screen, aqua, (560,0, 700, 5))
            pygame.draw.rect(screen, blue, (0, 0, 5, 600))
            pygame.draw.rect(screen, red, (1195, 0, 5, 600))
            pygame.draw.rect(screen, lime, (5, 595, 600, 5))
            pygame.draw.rect(screen, purple, (600, 595, 590, 5))

            pygame.draw.rect(screen, white, (588,0,17, 600))
            txt = texts()

            pygame.draw.rect(screen, black, (550, 0, 100, 40))
            txt.write(str(player_score), blue, 555, 10, 32)
            txt.write("-", yellow, 592, 10, 60)
            txt.write(str(pc_score) , red, 625, 10, 32)

            mousePosition = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            if 588 + 32 > mousePosition[0] > 588 and 570 + 32 > mousePosition[1] > 570:
                screen.blit(pause, (580, 570))
                if click[0] == 1:
                    size_pause = (800, 600)
                    pygame.display.set_mode(size_pause)
                    ps = Pause()
                    ps.pause()
            else:
                screen.blit(pause, (580, 570))

            if (playerY <= 10):
                playerY = 20
            if (playerY >= 460):
                playerY = 460

            if (pcY <= 10):
                pcY = 20
            if (pcY >= 460):
                pcY = 460


            Player1Rect = pygame.Rect(playerX,playerY,20,120)
            BallRect = pygame.Rect(ballX,ballY,40,40)
            PcRect=pygame.Rect(pcX,pcY,20,120)

            if BallRect.colliderect(Player1Rect):
                if abs(Player1Rect.right - BallRect.left) < 20:
                    ballMovingX *=-1
                if abs(Player1Rect.left - BallRect.right) < 20:
                    ballMovingX *=-1
                if abs(Player1Rect.top - BallRect.bottom) < 20:
                    ballMovingY *=-1
                if abs(Player1Rect.bottom - BallRect.top) < 20:
                    ballMovingY *=-1

            if BallRect.colliderect(PcRect):
                if abs(PcRect.right - BallRect.left) < 20:
                    ballMovingX *= -1
                if abs(PcRect.left - BallRect.right) < 20:
                    ballMovingX *= -1
                if abs(PcRect.top - BallRect.bottom) < 20:
                    ballMovingY *= -1
                if abs(PcRect.bottom - BallRect.top) < 20:
                    ballMovingY *= -1

            ballX += ballMovingX
            ballY += ballMovingY

            if PcRect.y<BallRect.y and abs(PcRect.y-BallRect.y)>12:
                pcY-=10
            elif PcRect.y>BallRect.y and abs(PcRect.y-BallRect.y)<12:
                pcY += 10

            if (ballX >= 1150):
                pygame.mixer_music.load("Music/goal.wav")
                pygame.mixer_music.play(0)
                player_score+=1
                ballX=580
                ballY=260
                ballMovingX = 10
                ballMovingY = -10

            if (ballX <= 10):
                pygame.mixer_music.load("Music/goal.wav")
                pygame.mixer_music.play(0)
                pc_score += 1
                ballX = 580
                ballY = 260
                ballMovingX = -10
                ballMovingY = 10
            if (ballY <= 10):
                ballMovingY *= -1
            if (ballY >= 525):
                ballMovingY *= -1

            pygame.draw.rect(screen,blue,Player1Rect)
            pygame.draw.rect(screen, red, PcRect)
            screen.blit(ball,(ballX,ballY))
            txt.write(counterText,orange,580,5,30)
            clock.tick(100)
            pygame.display.update()

#sng = singlePlayer_game_loop()
#sng.singleGame()