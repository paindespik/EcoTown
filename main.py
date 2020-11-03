import random
import pygame


class Personnage:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = pygame.image.load('images/personnage.png')

    def move_right(self):
        if self.x != rows-1:
            self.x = self.x + 1

    def move_left(self):
        if self.x != 0:
            self.x = self.x - 1

    def move_up(self):
        if self.y != 0:
            self.y = self.y - 1

    def move_down(self):
        if self.y != lines-1:
            self.y = self.y + 1


def drawGrid(w, h, lines, rows, surface):
    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwnX
        pygame.draw.line(surface, (0, 0, 0), (x, 0), (x, h))
    for L in range(lines):
        y = y + sizeBtwnY
        pygame.draw.line(surface, (0, 0, 0), (0, y), (w, y))


def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)
    target.blit(temp, location)


def placerPersonnage(surface, personnage):
    surface.blit(personnage.image, (personnage.x, personnage.y, 50, 30))
    pass


def redrawWindow(surface):
    global rows, width, s, snack, personnage
    surface.fill((0, 0, 0))
    blit_alpha(surface, background, (0, 0), 128)
    drawGrid(width, height, lines, rows, surface)
    placerPersonnage(surface, personnage)

    pygame.display.update()







def main():
    pygame.init()
    global width, height, rows, s, snack, background, lines, soldats, sizeBtwnX, sizeBtwnY, joueur, possibilities, personnage
    personnage = Personnage()
    personnage.x = 50
    personnage.y = 50
    width = 1000
    height = 1000
    background = pygame.image.load('images/background.png')
    soldats = []
    rows = 20
    lines = 20
    sizeBtwnX = width // rows
    possibilities = []
    for i in range(8):
        possibilities.append(False)
    sizeBtwnY = height // lines
    win = pygame.display.set_mode((width, height))
    background = pygame.image.load('images/background.png')
    running = True
    pressed = {}
    clock = pygame.time.Clock()
    while running:
        switcher = {
            0: "pas de gagnant",
            1: "équipe 1",
            2: "équipe 2",
            3: "execo",
        }
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
               pressed[event.key] = True
            elif event.type == pygame.KEYUP:
                pressed[event.key] = False

        if pressed.get(pygame.K_UP):
            personnage.move_up()
        if pressed.get(pygame.K_DOWN):
            personnage.move_down()
        if pressed.get(pygame.K_RIGHT):
            personnage.move_right()
        if pressed.get(pygame.K_LEFT):
            personnage.move_left()

        clock.tick(10)
        redrawWindow(win)
    pass


main()
