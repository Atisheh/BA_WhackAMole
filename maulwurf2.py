# IDEA
# Import & Init
import pygame
from pygame.locals import *
import random
pygame.init()

# Display
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Maulwurfjagd!")

back_img = pygame.image.load("images/rasen.jpg")
background = pygame.transform.scale(back_img, (640, 480))
pygame.display.update()

# Entities
img_maulwurf = pygame.image.load("images/maulwurf.gif")
img_schaufel = pygame.image.load("images/schaufel.png")

img_maulwurf = pygame.transform.scale(img_maulwurf, (100, 100))
img_schaufel = pygame.transform.scale(img_schaufel, (50, 50))

sound_waffe = pygame.mixer.Sound("sound/peng.wav")
sound_fail = pygame.mixer.Sound("sound/fail.wav")

# Action ==> ALTER
# Assign key variables
f = pygame.font.Font(None, 25)

clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 20)
keepGoing = True
maulwurfzaehler = 0
text = f.render("Hits: " + str(maulwurfzaehler), 1, (255, 255, 255))
pos_x = pos_y = 0
pos_maulwurf = img_maulwurf.get_rect()

# Maus-icon
pygame.mouse.set_visible(False)


# Loop
while keepGoing:
    # timing
    clock.tick(30)

    # Event
    x, y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        x, y = pygame.mouse.get_pos()
        if event.type == QUIT:
            keepGoing = False
            break
        elif event.type == USEREVENT:
            # neuen Timer setzen
            pygame.time.set_timer(pygame.USEREVENT, 1000)
            # maulwurfPos = zufallx, zufally
            pos_x = random.randint(50, 540)
            pos_y = random.randint(50, 380)
            #neue position - aktuelle Position, move = offset und nicht aktueller wert
            pos_maulwurf = pos_maulwurf.move(pos_x - pos_maulwurf.x, pos_y - pos_maulwurf.y)
            pass
        elif event.type == MOUSEBUTTONDOWN and pos_maulwurf.collidepoint(x, y):
            sound_waffe.play()
            maulwurfzaehler += 1
            # neuen Timer setzen
            pygame.time.set_timer(pygame.USEREVENT, 1000)
            # maulwurfPos = zufallx, zufally
            pos_x = random.randint(50, 540)
            pos_y = random.randint(50, 380)
            #neue position - aktuelle Position, move = offset und nicht aktueller wert
            pos_maulwurf = pos_maulwurf.move(pos_x - pos_maulwurf.x, pos_y - pos_maulwurf.y)
            
            if maulwurfzaehler == 2:
                back_img = pygame.image.load("images/grave.jpg")
                background = pygame.transform.scale(back_img, (640, 480))
                sound_waffe = pygame.mixer.Sound("sound/gun.wav")
                img_maulwurf = pygame.image.load("images/zombie.gif")
                img_schaufel = pygame.image.load("images/handgun.gif")
                img_maulwurf = pygame.transform.scale(img_maulwurf, (100, 100))
                img_schaufel = pygame.transform.scale(img_schaufel, (60, 60))
                pygame.display.update()
            elif maulwurfzaehler == 4:
                back_img = pygame.image.load("images/forest.jpg")
                background = pygame.transform.scale(back_img, (640, 480))
                sound_waffe = pygame.mixer.Sound("sound/power.wav")
                img_maulwurf = pygame.image.load("images/mew.png")
                img_schaufel = pygame.image.load("images/pball.png")
                img_maulwurf = pygame.transform.scale(img_maulwurf, (100, 100))
                img_schaufel = pygame.transform.scale(img_schaufel, (60, 60))
                pygame.display.update()
            elif maulwurfzaehler == 8:
                back_img = pygame.image.load("images/forest.jpg")
                background = pygame.transform.scale(back_img, (640, 480))
                sound_waffe = pygame.mixer.Sound("sound/pball.wav")
                img_maulwurf = pygame.image.load("images/mew.png")
                img_schaufel = pygame.image.load("images/pball.png")
                img_maulwurf = pygame.transform.scale(img_maulwurf, (100, 100))
                img_schaufel = pygame.transform.scale(img_schaufel, (60, 60))
                pygame.display.update()
            pass
        elif event.type == MOUSEBUTTONDOWN and not pos_maulwurf.collidepoint(x, y):
            sound_fail.play()

    # Refresh Display,
    text = f.render("Treffer: " + str(maulwurfzaehler), 1, (255, 255, 255))
    screen.blit(background, (0, 0))
    screen.blit(text, (10, 10))
    screen.blit(img_maulwurf, (pos_x, pos_y, 100, 100))
    screen.blit(img_schaufel, (x-10, y-10))
    pygame.display.update()
