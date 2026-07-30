import pygame


def init_pygame(largeur_pixels, hauteur_pixels):
    pygame.init()  # initialise la bibliothèque

    screen = pygame.display.set_mode((largeur_pixels, hauteur_pixels))

    # affiche tout ce qu'on vient de dessiner (sinon rien n'apparaît)
    pygame.display.flip()

    return screen


CELL_SIZE = 40
COLORS = {
    "W": (100, 100, 100),   # gris pour les murs
    ".": (58, 137, 35),      # fond
    "H": (0, 100, 255),     # tête, bleu foncé
    "S": (0, 150, 255),     # corps, bleu
    "G": (133, 193, 126),   # pomme verte
    "R": (255, 0, 0),       # pomme rouge
}


def draw_board(screen, board):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    grille = board.get_grid()
    screen.fill(COLORS["."])
    for y, ligne in enumerate(grille):
        for x, valeur in enumerate(ligne):
            couleur = COLORS[valeur]
            rect = (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, couleur, rect)
    pygame.display.flip()
