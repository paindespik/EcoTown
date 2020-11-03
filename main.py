import random
import pygame


class Personnage:
    def __init__(self):
        self.width = 25
        self.height = 39
        self.x = 0
        self.y = 0
        self.hautGauche = (self.x, self.y)
        self.hautDroit = (self.x + self.width, self.y)
        self.basGauche = (self.x, self.y+self.height)
        self.basDroit = (self.x + self.width, self.y+self.height)
        self.image = pygame.image.load('images/personnage.png')

    def move_right(self):
        if self.x+pas < width:
            self.x = self.x + pas

    def move_left(self):
        if self.x-pas > 0:
            self.x = self.x - pas

    def move_up(self):
        if self.y-pas > 0:
            self.y = self.y - pas

    def move_down(self):
        if self.y+pas < height:
            self.y = self.y + pas


def drawGrid(w, h, lines, rows, surface):

    for i in range(len(carte)):
        for j in range(len(carte[0])):
            if carte[j][i] == 0:
                surface.blit(pygame.image.load('images/route.jpg'), (50*j, 50*i, 50, 50))
            if carte[j][i] == 1:
                surface.blit(pygame.image.load('images/maison.png'), (50 * j, 50 * i, 50, 50))
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
    surface.blit(personnage.image, (personnage.x, personnage.y, personnage.width, personnage.height))
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
    global width, height, rows, s, snack, background, lines, soldats, sizeBtwnX, sizeBtwnY, joueur, possibilities, personnage, carte, pas
    pas = 3

    carte = [
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    personnage = Personnage()
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
            x = int(personnage.x/50)
            y = int((personnage.y+personnage.height-8-pas)/50)
            x2 = int((personnage.x+personnage.width)/50)
            if carte[x][y] == 0 and carte[x2][y] == 0:
                personnage.move_up()
        if pressed.get(pygame.K_DOWN):
            x = int(personnage.x/50)
            y = int((personnage.y+personnage.height+pas)/50)
            x2 = int((personnage.x+personnage.width)/50)
            if carte[x][y] == 0 and carte[x2][y] == 0:
                personnage.move_down()
        if pressed.get(pygame.K_RIGHT):
            x = int((personnage.x+pas+personnage.width)/50)
            y = int((personnage.y+personnage.height)/50)
            if carte[x][y] == 0:
                personnage.move_right()
        if pressed.get(pygame.K_LEFT):
            x = int((personnage.x-pas)/50)
            y = int((personnage.y+personnage.height)/50)
            if carte[x][y] == 0:
                personnage.move_left()

        clock.tick(40)
        redrawWindow(win)
    pass


main()
