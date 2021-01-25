import math
import os
import pygame

pygame.display.init()

WIDTH, HEIGHT = 270, 270  #taille de la fenêtre
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Morpion")

FPS = 60

WHITE = (255,255,255)
BLACK = (0, 0, 0)

SIZE_BARE = 10 
HORIZONTAL_BORDER_1 = pygame.Rect(0, HEIGHT // 3 - 5, WIDTH, SIZE_BARE)
HORIZONTAL_BORDER_2 = pygame.Rect(0, 2 * HEIGHT // 3 - 5, WIDTH, SIZE_BARE)

VERTICAL_BORDER_1 = pygame.Rect(WIDTH // 3 - 5, 0 , SIZE_BARE, HEIGHT)
VERTICAL_BORDER_2 = pygame.Rect(2 * WIDTH // 3 - 5, 0 , SIZE_BARE, HEIGHT)


CROSS_SIZE = int ( (HEIGHT // 3 - 10) // math.sqrt(2) ) # pythagore


CROSS_IMAGE = pygame.image.load(
    os.path.join('Morpion\\Sprites', 'cross.jpg'))
CROSS = pygame.transform.rotate(pygame.transform.scale(
    CROSS_IMAGE, (CROSS_SIZE, CROSS_SIZE)), 45)

CIRCLE_IMAGE = pygame.image.load(
    os.path.join('Morpion\\Sprites', 'circle.jpg'))
CIRCLE = pygame.transform.rotate(pygame.transform.scale(
    CIRCLE_IMAGE, (CROSS_SIZE, CROSS_SIZE)), 45)

PLAYER_1 = 1 
PLAYER_2 = 2 

GAME_BOARD = [0, 0, 0,
              0, 0, 0, 
              0, 0, 0 ] # represente le jeu à l'instant t

def draw_window():
    WIN.fill(WHITE) # fenêtre blanche

    pygame.draw.rect(WIN,BLACK, HORIZONTAL_BORDER_1) # créer les lignes
    pygame.draw.rect(WIN,BLACK, HORIZONTAL_BORDER_2)
    pygame.draw.rect(WIN,BLACK, VERTICAL_BORDER_1)
    pygame.draw.rect(WIN,BLACK, VERTICAL_BORDER_2)

    pygame.display.update() # mettre à jour la fenêtre


def draw_box(player, x, y):

    if player == PLAYER_1:
        WIN.blit(CROSS, (x, y))
    else :
        WIN.blit(CIRCLE, (x, y))
    pygame.display.update() # mettre à jour la fenêtre


def handle_mouse(player, box_free):
    pos_mouse = pygame.mouse.get_pos()
    box = -1
    x, y = -1, -1
    if pos_mouse[0] <= WIDTH // 3 - 5 and pos_mouse[1] <= HEIGHT // 3 - 5: # 1ere case 
        if GAME_BOARD[0] == 0:
            box = 0 
            x = 0
            y = 0 
    elif pos_mouse[0] <= 2 * (WIDTH // 3 - 5) and pos_mouse[1] <= (HEIGHT // 3 - 5): # 2e case 
        if GAME_BOARD[1] == 0:
            box = 1   
            x = WIDTH // 3 + 5
            y = 0  
    elif pos_mouse[0] <= 3 *  (WIDTH // 3 - 5) and pos_mouse[1] <= (HEIGHT // 3 - 5): # 3e case
        if GAME_BOARD[2] == 0:
            box = 2 
            x = 2 * WIDTH // 3 + 5
            y = 0   
    elif pos_mouse[0] <= (WIDTH // 3 - 5) and pos_mouse[1] <= 2 * (HEIGHT // 3 - 5): # 4e case
        if GAME_BOARD[3] == 0:
            box = 3 
            x = 0
            y = HEIGHT // 3 + 5 
    elif pos_mouse[0] <= 2 * (WIDTH // 3 - 5) and pos_mouse[1] <= 2 * (HEIGHT // 3 - 5): # 5e case
        if GAME_BOARD[4] == 0:
            box = 4 
            x = WIDTH // 3 + 5
            y = HEIGHT // 3 + 5
    elif pos_mouse[0] <= 3 * (WIDTH // 3 - 5) and pos_mouse[1] <= 2 * (HEIGHT // 3 - 5): # 6e case
        if GAME_BOARD[5] == 0:
            box = 5
            x = 2 * WIDTH // 3 + 5
            y = HEIGHT // 3 + 5 
    elif pos_mouse[0] <= (WIDTH // 3 - 5) and pos_mouse[1] <= 3 *(HEIGHT // 3 - 5): # 7e case
        if GAME_BOARD[6] == 0:
            box = 6 
            x = 0
            y = 2 * HEIGHT // 3 + 5
    elif pos_mouse[0] <= 2 * (WIDTH // 3 - 5) and pos_mouse[1] <=  3 * (HEIGHT // 3 - 5): # 8e case
        if GAME_BOARD[7] == 0:
            box = 7
            x = WIDTH // 3 + 5
            y = 2 * HEIGHT // 3 + 5
    else :                                                                          # 9e case
        if GAME_BOARD[8] == 0:
            box = 8
            x = 2 * WIDTH // 3 + 5
            y = 2 * HEIGHT // 3 + 5
    GAME_BOARD[box] = player
    draw_box(player, x, y)
    check_winner(player, box_free - 1)

def check_winner(player, box_free):
    if GAME_BOARD[0] != 0 and GAME_BOARD[0] == GAME_BOARD[1] and GAME_BOARD[1] == GAME_BOARD[2] : # ligne horizontal haut
        print("Player " + str(player) + " WIN")
        pygame.time.delay(5000)
        pygame.quit()
    elif GAME_BOARD[0] != 0 and GAME_BOARD[0] == GAME_BOARD[3] and GAME_BOARD[3] == GAME_BOARD[6] : # ligne verticale gauche
        print("Player " + str(player) + " WIN")
        pygame.time.delay(5000)
        pygame.quit()
    elif GAME_BOARD[0] != 0 and GAME_BOARD[0] == GAME_BOARD[4] and GAME_BOARD[4] == GAME_BOARD[8] : # ligne diagonale gauche
        print("Player " + str(player) + " WIN")
        pygame.time.delay(5000)
        pygame.quit()
    elif GAME_BOARD[1] != 0 and GAME_BOARD[1] == GAME_BOARD[4] and GAME_BOARD[4] == GAME_BOARD[7] : # ligne verticale milieu
        print("Player " + str(player) + " WIN")
        pygame.time.delay(5000)
        pygame.quit()
    elif GAME_BOARD[2] != 0 and GAME_BOARD[2] == GAME_BOARD[4] and GAME_BOARD[4] == GAME_BOARD[6] : # ligne diagonale droite
        print("Player " + str(player) + " WIN")
        pygame.time.delay(5000)
        pygame.quit()
    elif GAME_BOARD[2] != 0 and GAME_BOARD[2] == GAME_BOARD[5] and GAME_BOARD[5] == GAME_BOARD[8] : # ligne verticale droite
        print("Player " + str(player) + " WIN")
        pygame.time.delay(5000)
        pygame.quit()
    elif GAME_BOARD[3] != 0 and GAME_BOARD[3] == GAME_BOARD[4] and GAME_BOARD[4] == GAME_BOARD[5] : # ligne verticale droite
        print("Player " + str(player) + " WIN")
        pygame.time.delay(5000)
        pygame.quit()
    elif GAME_BOARD[6] != 0 and GAME_BOARD[6] == GAME_BOARD[7] and GAME_BOARD[7] == GAME_BOARD[8] : # ligne horizontale droite
        print("Player " + str(player) + " WIN")
        pygame.time.delay(5000)
        pygame.quit()
    else :
        print(box_free)
        if box_free == 0:
            print("Tie")
            pygame.time.delay(5000)
            pygame.quit()


def play(player, box_free):  # détermine quel joueur joue 
    if player == PLAYER_1:
        if pygame.mouse.get_pressed() == (1, 0, 0) :
            handle_mouse(player, box_free)
        return PLAYER_2 # au tour de joueur 2
    else :
        if pygame.mouse.get_pressed() == (1, 0, 0) :
            handle_mouse(player, box_free)
        return PLAYER_1 # au tour de joueur 1
            

def main():
    run = True 
    clock = pygame.time.Clock()
    player = PLAYER_1
    box_free = 9 
    draw_window()
    while(True):
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                player = play(player, box_free)
                box_free -= 1

    return 0


if __name__ == "__main__":
    main()