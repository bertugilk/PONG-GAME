import pygame
import sys
import Single_Player
import Two_Players
import Settings

pygame.init()

screen_width=1000
screen_heigth=600
size=(screen_width,screen_heigth)
screen=pygame.display.set_mode(size)

pygame.display.set_caption("PONG-GAME")
logo=pygame.image.load("Images/logo.jpg")
pygame.display.set_icon(logo)

# Colors:
black=(0,0,0)
chocalate=(210,105,30)
white=(255,255,255)
green=(0,128,0)
red=(255,0,0)
blue=(0,0,255)
aqua=(0,255,255)
yellow=(255,255,0)
purple=(255,0,255)
orange=(255,165,0)
lime=(0,255,0)
gold=(255,215,0)
salmon=(250,128,114)
deepPink=(255,0,127)
brown=(204,102,0)
deepPurple=(138,36,114)

time=pygame.time.Clock()
background=pygame.image.load("Images/bg.jpg")

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

class Intro():
    def intro(self):
        color=aqua
        text="WELCOME TO AİR HOCKEY"
        txtXyon=1
        txtX=0

        pygame.mixer_music.load("Music/intro_music.mp3")
        pygame.mixer_music.play(0)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            screen.fill(black)
            screen.blit(background, (0, 0))
            txt=texts()

            txtX-=txtXyon*4

            if(txtX<-50):
                color=yellow
                text = "GOOD GAMES :)"
                txtXyon*=-1
            if( txtX>550):
                color=lime
                text = "WELCOME TO AİR HOCKEY"
                txtXyon *= -1

            txt.write(text,color,txtX,30,80)

            pygame.draw.rect(screen,lime,(100,500,200,80))
            pygame.draw.rect(screen, aqua, (370, 500, 200, 80))
            pygame.draw.rect(screen, deepPink, (640, 500, 200, 80))
            pygame.draw.rect(screen, red, (963, 559, 40, 40))

            mousePosition = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            if 963 + 40 > mousePosition[0] > 963 and 559 + 40 > mousePosition[1] > 559:
                pygame.draw.rect(screen, salmon, (963, 559, 40, 40))
                if click[0] == 1:
                    quit()
            else:
                pygame.draw.rect(screen, red, (963, 559, 40, 40))

            if 100 + 200 > mousePosition[0] > 100 and 500 + 80 > mousePosition[1] > 500:
                pygame.draw.rect(screen, green, (100, 500, 200, 80))
                if click[0] == 1:
                    size_single=(1200,600)
                    pygame.display.set_mode(size_single)
                   # pygame.mixer_music.stop()
                    sng=Single_Player.singlePlayer_game_loop()
                    sng.singleGame()
            else:
                pygame.draw.rect(screen, lime, (100, 500, 200, 80))

            if 370 + 200 > mousePosition[0] > 370 and 500 + 80 > mousePosition[1] > 500:
                pygame.draw.rect(screen, blue, (370, 500, 200, 80))
                if click[0] == 1:
                    size_two = (1200, 600)
                    pygame.display.set_mode(size_two)
                    sng = Two_Players.TwoPlayers_game_loop()
                    sng.TwoplayerGame()
            else:
                pygame.draw.rect(screen, aqua, (370, 500, 200, 80))

            if 640 + 200 > mousePosition[0] > 640 and 500 + 80 > mousePosition[1] > 500:
                pygame.draw.rect(screen, purple, (640, 500, 200, 80))
                size2=(800,500)
                if click[0] == 1:
                    pygame.display.set_mode(size2)
                    stng=Settings.Settings()
                    stng.options()
            else:
                pygame.draw.rect(screen, deepPink, (640, 500, 200, 80))

            txt.write("SINGLE", black, 145, 510, 40)
            txt.write("PLAYER", black, 145, 545, 40)
            txt.write("TWO", black, 435, 510, 40)
            txt.write("PLAYERS", black, 415, 545, 40)
            txt.write("SETTINGS", black, 660, 530, 45)
            txt.write("X",white, 967, 560, 60)

            time.tick(20)
            pygame.display.update()

intro=Intro()
intro.intro()