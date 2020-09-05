import pygame
import sys

pygame.init()

screen_width=800
screen_heigth=500
size=(screen_width,screen_heigth)
screen_setting=pygame.display.set_mode(size)

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
        screen_setting.blit(text, [x, y])

class Key():
    def key_option(self):
        screen_width = 500
        screen_heigth = 600
        size = (screen_width, screen_heigth)
        screen_key = pygame.display.set_mode(size)
        back = pygame.image.load("Images/back.png")

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            screen_key.fill(black)
            txt=texts()
            txt.write("-Single Player-",white,60,20,80)
            txt.write("- KLAVYE YÖN TUŞLARI İLE HAREKET SAĞLANIR.",yellow,10,130,30)
            txt.write("- RAKİBİN KALESİNE HER GOL ATTIĞINIZDA", yellow, 10, 180, 30)
            txt.write("  BİR SAYI KAZANIRSINIZ.", yellow, 10, 210, 30)
            txt.write("-TWO Players-", white, 60, 270, 80)
            txt.write("- 1. OYUNCU W-S TUŞLARI İLE",yellow,10,370,30)
            txt.write("- 2. OYUNCU İSE AŞAĞI VE YUKARI YÖN TUŞLARI", yellow, 10, 430, 30)
            txt.write("  İLE HAREKETİ SAĞLAR.", yellow, 10, 470, 30)
            pygame.draw.rect(screen_key,red,(450,550,50,50))

            mousePosition = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            if 450 + 50 > mousePosition[0] > 450 and 550 + 50 > mousePosition[1] > 550:
                pygame.draw.rect(screen_key,salmon, (450, 550, 50, 50))
                screen_key.blit(back, (460, 560))
                if click[0] == 1:
                   size_option=(800,500)
                   pygame.display.set_mode(size_option)
                   stng=Settings()
                   stng.options()
            else:
                pygame.draw.rect(screen_key, red, (450, 550, 50, 50))

            screen_key.blit(back, (460, 560))
            pygame.display.update()

class Settings():
    def options(self):
        turn_off_sound = pygame.image.load("Images/mute.png")
        turn_on_sound = pygame.image.load("Images/volume.png")
        option_background = pygame.image.load("Images/bg2.jpg")
        back = pygame.image.load("Images/back.png")
        gamepad=pygame.image.load("Images/gamepad.png")

        color = red
        txtXyon = 1
        txtX = 250

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            screen_setting.fill(black)
            screen_setting.blit(option_background, (0, 0))

            mousePosition = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            txt=texts()
            txtX += txtXyon * 4

            if (txtX <= 0):
                color = lime
                txtXyon *= -1
            if (txtX > 460):
                color = red
                txtXyon *= -1

            txt.write("-OPTIONS-",color,txtX,30,100)

            pygame.draw.rect(screen_setting, purple, (50, 200, 150, 150))
            pygame.draw.rect(screen_setting, orange, (300, 200, 150, 150))
            pygame.draw.rect(screen_setting, aqua, (550, 200, 150, 150))
            pygame.draw.rect(screen_setting, white, (756, 457, 50, 50))

            if 50 + 150 > mousePosition[0] > 50 and 200 + 150 > mousePosition[1] > 200:
                pygame.draw.rect(screen_setting, deepPurple, (50, 200, 150, 150))
                screen_setting.blit(turn_off_sound, (60, 210))
                screen_setting.blit(turn_on_sound, (310, 210))
                screen_setting.blit(gamepad, (560, 200))
                screen_setting.blit(back, (760, 460))
                if click[0] == 1:
                    pygame.mixer_music.pause()
            else:
                pygame.draw.rect(screen_setting, purple, (50, 200, 150, 150))

                if 300 + 150 > mousePosition[0] > 300 and 200 + 150 > mousePosition[1] > 200:
                    pygame.draw.rect(screen_setting, brown, (300, 200, 150, 150))
                    screen_setting.blit(turn_on_sound, (310, 210))
                    screen_setting.blit(turn_off_sound, (60, 210))
                    screen_setting.blit(gamepad, (560, 200))
                    screen_setting.blit(back, (760, 460))
                    if click[0] == 1:
                        pygame.mixer_music.play(0)
                else:
                    pygame.draw.rect(screen_setting, orange, (300, 200, 150, 150))

                if 550 + 150 > mousePosition[0] > 550 and 200 + 150 > mousePosition[1] > 200:
                    pygame.draw.rect(screen_setting, blue, (550, 200, 150, 150))
                    screen_setting.blit(turn_on_sound, (310, 210))
                    screen_setting.blit(turn_off_sound, (60, 210))
                    screen_setting.blit(gamepad, (560, 200))
                    screen_setting.blit(back, (760, 460))
                    if click[0] == 1:
                        ky=Key()
                        ky.key_option()
                else:
                    pygame.draw.rect(screen_setting, aqua, (550, 200, 150, 150))

                if 756 + 150 > mousePosition[0] > 756 and 457 + 40 > mousePosition[1] > 457:
                    pygame.draw.rect(screen_setting, deepWhite, (756, 457, 50, 50))
                    screen_setting.blit(turn_on_sound, (310, 210))
                    screen_setting.blit(turn_off_sound, (60, 210))
                    screen_setting.blit(gamepad, (560, 200))
                    screen_setting.blit(back, (760, 460))
                    if click[0] == 1:
                        size_intro = (1000, 600)
                        pygame.display.set_mode(size_intro)
                        import Intro
                        intr=Intro.Intro()
                        intr.intro()
                else:
                    pygame.draw.rect(screen_setting, white, (756, 457, 50, 50))

                screen_setting.blit(turn_off_sound, (60, 210))
                screen_setting.blit(turn_on_sound, (310, 210))
                screen_setting.blit(gamepad,(560,200))
                screen_setting.blit(back, (760, 460))

            time.tick(40)
            pygame.display.update()

#st=Settings()
#st.options()