import random
import pygame


class Personnage:
    def __init__(self):
        self.width = 25
        self.height = 39
        self.x = 0
        self.y = 0
        self.case = (0,0)
        self.hautGauche = (self.x, self.y)
        self.hautDroit = (self.x + self.width, self.y)
        self.basGauche = (self.x, self.y+self.height)
        self.basDroit = (self.x + self.width, self.y+self.height)
        self.inventaire = []
        self.image = pygame.image.load('images/personnage.png')

    def move_right(self):
        if self.x+self.width + 5 +pas < width:
            self.x = self.x + pas
            self.case = (int(self.x/50), int(self.y/50))

    def move_left(self):
        if self.x-pas > 0:
            self.x = self.x - pas
            self.case = (int(self.x/50), int(self.y/50))

    def move_up(self):
        if self.y + 5 - pas > 0:
            self.y = self.y - pas
            self.case = (int(self.x/50), int(self.y/50))

    def move_down(self):
        if self.y+pas < height:
            self.y = self.y + pas
            self.case = (int(self.x/50), int(self.y/50))


def drawGrid(w, h, lines, rows, surface):

    for i in range(len(carte)):
        for j in range(len(carte[0])):
            if carte[j][i] == 0:
                surface.blit(pygame.image.load('images/route2.jpg'), (50*j, 50*i, 50, 50))
                if (j,i) in listDechet:
                    surface.blit(pygame.image.load('images/canette1.png'), (50 * j, 50 * i, 50, 50))

            elif carte[j][i] == 1:
                if i != 0:
                    if carte[j][i-1] == 0:
                        surface.blit(pygame.image.load('images/maison.png'), (50 * j, 50 * i, 50, 50))
                if j != len(carte)-1:
                    if carte[j+1][i] == 0:
                        surface.blit(pygame.image.load('images/maison-droite.png'), (50 * j, 50 * i, 50, 50))
                if i != len(carte[0])-1:
                    if carte[j][i+1] == 0:
                        surface.blit(pygame.image.load('images/maison-bas.png'), (50 * j, 50 * i, 50, 50))
                if j != 0:
                    if carte[j-1][i] == 0:
                        surface.blit(pygame.image.load('images/maison-gauche.png'), (50 * j, 50 * i, 50, 50))
            elif carte[j][i] == 2:
                surface.blit(pygame.image.load('images/immeuble.png'), (50 * j, 50 * i, 50, 50))
            elif carte[j][i] == 3:
                surface.blit(pygame.image.load('images/park.png'), (50 * j, 50 * i, 50, 50))
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


def texte(surface):
    font = pygame.font.SysFont("comicsansms", 30)
    txtTitre = "EcoTown"
    titre = font.render(txtTitre, True, (255, 255, 255))
    surface.blit(titre, (width+(widthTexte/3), 50))
    if (int(personnage.x/50), int(personnage.y/50)) in listDechet:
        fontTexte = pygame.font.SysFont("comicsansms", 15)
        txtTexte = "ESPACE pour ramasser"
        texte = fontTexte.render(txtTexte, True, (0, 255, 0))
        surface.blit(texte, (width, 100))
    elif personnage.inventaire:
        fontTexte = pygame.font.SysFont("comicsansms", 15)
        txtTexte = "Ramasser "+ objectifCannette +" objets pour améliorer la ville"
        texte = fontTexte.render(txtTexte, True, (0, 255, 0))
        surface.blit(texte, (width, 100))
    if personnage.inventaire:
        x = 0
        y = 300
        fontInventaire = pygame.font.SysFont("comicsansms", 30)
        txtInventaire = fontInventaire.render("Inventaire", True, (255, 255, 255))
        surface.blit(txtInventaire, (width + (widthTexte / 5), 250))

        for l in range(int(len(personnage.inventaire)/3)+1):
            pygame.draw.line(surface, (255, 255, 255), (width, y), (width+widthTexte, y))
            pygame.draw.line(surface, (255, 255, 255), (width, y+50), (width+widthTexte, y+50))
            pygame.draw.line(surface, (255, 255, 255), (width+widthTexte/3, y), (width+widthTexte/3, y+50))
            pygame.draw.line(surface, (255, 255, 255), (width+2*widthTexte/3, y), (width+2*widthTexte/3, y+50))
            y = y + 50

        x = width
        y = 250
        for i in range(len(personnage.inventaire)):

            if i%3 == 0:
                y += 50
                x = width
            if personnage.inventaire[i][2] == 'cannette':
                surface.blit(pygame.image.load('images/canette1.png'), (x, y, 50, 50))
            x += widthTexte/3


    pass


def redrawWindow(surface):
    global rows, width, s, snack, personnage
    surface.fill((0, 0, 0))
    blit_alpha(surface, background, (0, 0), 128)
    drawGrid(width, height, lines, rows, surface)
    placerPersonnage(surface, personnage)
    texte(surface)
    pygame.display.update()


def main():
    pygame.init()
    global width, height, rows, s, snack, background, lines, soldats, sizeBtwnX, sizeBtwnY, joueur, possibilities, personnage, carte, pas, widthTexte, listDechet, objectifCannette
    pas = 6

    carte = [
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        [0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 2],
        [0, 1, 0, 1, 1, 1, 1, 3, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 2],
        [0, 1, 0, 1, 3, 3, 3, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 1, 0, 3, 3, 3, 3, 3, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 2],
        [0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 2],
        [0, 1, 1, 1, 1, 1, 0, 2, 2, 0, 2, 2, 0, 1, 1, 0, 1, 1, 0, 2],
        [0, 1, 1, 1, 1, 1, 0, 2, 2, 0, 2, 2, 0, 1, 1, 0, 1, 1, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 1, 0, 1, 1, 1, 0, 2, 2, 0, 2, 2, 0, 1, 1, 0, 2, 2, 0, 1],
        [3, 1, 0, 1, 3, 1, 0, 2, 2, 0, 2, 2, 0, 1, 1, 0, 2, 0, 0, 0],
        [3, 1, 0, 1, 3, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 2, 0, 3, 0],
        [3, 1, 0, 1, 3, 1, 0, 2, 2, 0, 2, 2, 0, 0, 0, 0, 0, 0, 3, 0],
        [3, 1, 0, 1, 3, 1, 0, 2, 2, 0, 2, 2, 0, 1, 1, 0, 3, 3, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
        [1, 1, 0, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 1, 3, 1, 0],
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    ]
    listDechet = []
    for i in range(len(carte)):
        for j in range(len(carte[0])):
            if carte[j][i] == 0:
                etatevenement = random.randrange(0, 10 , 1)
                if etatevenement == 1:
                    listDechet.append((j,i))

    objectifCannette = 4
    personnage = Personnage()
    # personnage.x=900
    # personnage.y=100
    width = 1000
    height = 1000
    widthTot = 1300
    widthTexte = widthTot - width
    background = pygame.image.load('images/background.png')
    soldats = []
    rows = 20
    lines = 20
    sizeBtwnX = width // rows
    possibilities = []
    for i in range(8):
        possibilities.append(False)
    sizeBtwnY = height // lines
    win = pygame.display.set_mode((widthTot, height))
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
            if (carte[x][y] == 0 or carte[x][y] == 3) and (carte[x2][y] == 0 or carte[x2][y] == 3):
                personnage.move_up()
        if pressed.get(pygame.K_DOWN):
            x = int(personnage.x/50)
            y = int((personnage.y+personnage.height+pas)/50)
            x2 = int((personnage.x+personnage.width)/50)
            if (carte[x][y] == 0 or carte[x][y] == 3) and (carte[x2][y] == 0 or carte[x2][y] == 3):
                personnage.move_down()
        if pressed.get(pygame.K_RIGHT):
            x = int((personnage.x+pas+personnage.width)/50)
            y = int((personnage.y+personnage.height)/50)
            if carte[x][y] == 0 or carte[x][y] == 3:
                personnage.move_right()
        if pressed.get(pygame.K_LEFT):
            x = int((personnage.x-pas)/50)
            y = int((personnage.y+personnage.height)/50)
            if carte[x][y] == 0 or carte[x][y] == 3:
                personnage.move_left()
        if pressed.get(pygame.K_SPACE):
            if personnage.case in listDechet:
                personnage.inventaire.append((personnage.case[0], personnage.case[1], 'cannette'))
                listDechet.remove(personnage.case)

        clock.tick(40)
        redrawWindow(win)
    pass


main()
