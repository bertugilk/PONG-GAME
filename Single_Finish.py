import pygame
import Single_Player

pygame.init()

screen_width=800
screen_heigth=500
size=(screen_width,screen_heigth)
screen_finish=pygame.display.set_mode(size)

pygame.display.set_caption("PONG-GAME")
logo=pygame.image.load("Images/logo.jpg")
pygame.display.set_icon(logo)

time=pygame.time.Clock()

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
Pink=(255,153,204)
brown=(204,102,0)
deepPurple=(138,36,114)
deepWhite=(255,200,200)

class texts():
    def write(self, message, color, x, y, size):
        self.message = message
        self.color = color
        self.x = x
        self.y = y
        self.size = size
        font = pygame.font.SysFont(None, size)
        text = font.render(message, True, color)
        screen_finish.blit(text, [x, y])
class Single_Finish():
    pygame.mixer_music.load("Music/intro_music.mp3")
    pygame.mixer_music.play(0)
    def Finish(self):
        back = pygame.image.load("Images/home.png")
        repeat = pygame.image.load("Images/repeat.png")
        quitImg = pygame.image.load("Images/quit.png")
        bg = pygame.image.load("Images/bgfinish.jpg")

        sngplyr = Single_Player.singlePlayer_game_loop()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            screen_finish.fill(black)
            screen_finish.blit(bg,(0,0))
            mousePosition = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            txt=texts()
            txt.write("PONG GAME", purple, 120, 25, 120)

            if 60 + 128 > mousePosition[0] > 60 and 210 + 128 > mousePosition[1] > 210:
                screen_finish.blit(back, (60, 210))
                screen_finish.blit(repeat, (320, 210))
                screen_finish.blit(quitImg, (600, 210))
                if click[0] == 1:
                    size_intro = (1000, 600)
                    pygame.display.set_mode(size_intro)
                    import Intro
                    intr=Intro.Intro()
                    intr.intro()
            else:
                screen_finish.blit(back, (60, 210))
                screen_finish.blit(repeat, (320, 210))
                screen_finish.blit(quitImg, (600, 210))
            time.tick(40)
            pygame.display.update()

            if 320 + 128 > mousePosition[0] > 320 and 210 + 128 > mousePosition[1] > 210:
                screen_finish.blit(repeat, (320, 210))
                screen_finish.blit(back, (60, 210))
                screen_finish.blit(quitImg, (600, 210))
                if click[0] == 1:
                    size_intro = (1200, 600)
                    pygame.display.set_mode(size_intro)
                    sngplyr.singleGame()
            else:
                screen_finish.blit(repeat, (320, 210))
                screen_finish.blit(back, (60, 210))
                screen_finish.blit(quitImg, (600, 210))

            if 600 + 128 > mousePosition[0] > 600 and 210 + 128 > mousePosition[1] > 210:
                screen_finish.blit(quitImg, (600, 210))
                screen_finish.blit(repeat, (320, 210))
                screen_finish.blit(back, (60, 210))
                if click[0] == 1:
                    quit()
            else:
                screen_finish.blit(quitImg, (600, 210))
                screen_finish.blit(repeat, (320, 210))
                screen_finish.blit(back, (60, 210))

            time.tick(40)
            pygame.display.update()


#sngfns=Single_Finish()
#sngfns.Finish()