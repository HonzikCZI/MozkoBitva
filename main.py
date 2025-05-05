import pygame
import random

#  Inicializace hry
pygame.init()

# obrazovka
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("MozkoBitva")

# nastavení hry
fps = 60
clock = pygame.time.Clock()

# classy
class mozkomor(pygame.sprite.Sprite):
    # constructor
    def __init__(self, x, y,):
        super().__init__()
        self.image = pygame.image.load("img/mozkomor-zeleny.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.speed = random.randint(1, 6)

    def update(self):
        self.rect.y += self.speed


class Player(pygame.sprite.Sprite):
    # construktor
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("img/potter-icon.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.speed = random.randint(1, 6)

    def update(self):
        self.move()

    def move(self):
        self.rect.y -= self.speed
        


# skupina mozkomorů
mozkomor_group = pygame.sprite.Group()
for i in range(10):
    one_mozkomor = mozkomor(i * 70 , 50)
    mozkomor_group.add(one_mozkomor)


# skupina hráčů
Player_group = pygame.sprite.Group()
for i in range(10):
    one_player = Player(i * 70, 500)
    Player_group.add(one_player)


# =================HLAVNÍ CYKLUS=================== #
lets_continue = True
while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False 

    # Vyplníme obrazovku černou barvou
    screen.fill((0, 0, 0))

    # updajtujeme skupinu mozkomorů
    mozkomor_group.update()
    mozkomor_group.draw(screen)

    # ubdajtujeme skupine hráčů
    Player_group.update()
    Player_group.draw(screen)


    # updatujeme obrazovku
    pygame.display.update()


    # Zpomalení cyklu
    clock.tick(fps)


# ukončení hry
pygame.quit()