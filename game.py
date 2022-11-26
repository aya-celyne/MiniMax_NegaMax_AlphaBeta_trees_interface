import pygame, sys
from node import *
from vars import *
from button import Button


Tree = creat_tree()

pygame.init()
pygame.display.set_caption("Search-Algorithms")
#BG = pygame.image.load("assets/Background.png")
window.fill(BG_Color)

Draw_Tree(Tree)

def MiniMax_(player):
    if player == 1 :
        MinMax(Tree, player)
    elif player == -1:
        MinMax(Tree, player)

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/Poppins-Medium.ttf", size)

def select():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        window.fill(BG_Color)

        MENU_TEXT = get_font(80).render("Select a search algorithm", True, "#00CCCC")
        MENU_RECT = MENU_TEXT.get_rect(center=(Width/2, 150))


        MiniMax_BUTTON = Button(image=pygame.image.load("assets/Rectangle_1.png"), pos=(Width/3, Height/2), 
                                text_input="MinMax", font=get_font(35), base_color="#000000", hovering_color="#4B3305")

        NegaMax_BUTTON = Button(image=pygame.image.load("assets/Rectangle_3.png"), pos=(2*Width/3, Height/2), 
                                text_input="Negamax", font=get_font(35), base_color="#000000", hovering_color="#4B3305")

        AlphaBeta_BUTTON = Button(image=pygame.image.load("assets/Rectangle_2.png"), pos=(Width/2,Height/3), 
                                text_input="Negamax Alpha Beta", font=get_font(35), base_color="#000000", hovering_color="#4B3305")

        QUIT_BUTTON = Button(image=pygame.image.load("assets/Rectangle_1.png"), pos=(Width/2,2*Height/3), 
                            text_input="QUIT", font=get_font(35), base_color="#000000", hovering_color="#4B3305")

        window.blit(MENU_TEXT, MENU_RECT)

        for button in [MiniMax_BUTTON, NegaMax_BUTTON, AlphaBeta_BUTTON,QUIT_BUTTON]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(window)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MiniMax_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    select_Player_MiniMax()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if NegaMax_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    select_Player_NegaMax()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if AlphaBeta_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    select_Player_AlphaBeta()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if QUIT_BUTTON.checkForInput(PLAY_MOUSE_POS ):
                    pygame.quit()
                    sys.exit()


        pygame.display.update()

def select_Player_MiniMax():
    while True:
        window.fill(BG_Color)

        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("Choose a player", True, "#00CCCC")
        MENU_RECT = MENU_TEXT.get_rect(center=(Width/2, 100))

        Min_BUTTON = Button(image=pygame.image.load("assets/Rectangle_1.png"), pos=(Width/3, Height/2), 
                                text_input="Min", font=get_font(40), base_color="#000000", hovering_color="#4B3305")

        Max_BUTTON = Button(image=pygame.image.load("assets/Rectangle_1.png"), pos=(2 *Width/3, Height/2), 
                                text_input="Max", font=get_font(40), base_color="#000000", hovering_color="#4B3305")
        window.blit(MENU_TEXT, MENU_RECT)
        
        for button in [Min_BUTTON, Max_BUTTON]:
                button.changeColor(PLAY_MOUSE_POS)
                button.update(window)
        
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if Min_BUTTON.checkForInput(PLAY_MOUSE_POS):
                            Display_MiniMax(-1)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if Max_BUTTON.checkForInput(PLAY_MOUSE_POS):
                            Display_MiniMax(1)

        pygame.display.update()

def select_Player_NegaMax():
    while True:
        window.fill(BG_Color)

        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("Choose a player", True, "#00CCCC")
        MENU_RECT = MENU_TEXT.get_rect(center=(Width/2, 100))

        Min_BUTTON = Button(image=pygame.image.load("assets/Rectangle_1.png"), pos=(Width/3, Height/2), 
                                text_input="Min", font=get_font(40), base_color="#000000", hovering_color="#4B3305")

        Max_BUTTON = Button(image=pygame.image.load("assets/Rectangle_1.png"), pos=(2 *Width/3, Height/2), 
                                text_input="Max", font=get_font(40), base_color="#000000", hovering_color="#4B3305")

        window.blit(MENU_TEXT, MENU_RECT)
        
        for button in [Min_BUTTON, Max_BUTTON]:
                button.changeColor(PLAY_MOUSE_POS)
                button.update(window)
        
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if Min_BUTTON.checkForInput(PLAY_MOUSE_POS):
                            Display_NegaMax(-1)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if Max_BUTTON.checkForInput(PLAY_MOUSE_POS):
                            Display_NegaMax(1)

        pygame.display.update()

def select_Player_AlphaBeta():
    while True:
        window.fill(BG_Color)

        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("Choose a player", True, "#00CCCC")
        MENU_RECT = MENU_TEXT.get_rect(center=(Width/2, 100))

        Min_BUTTON = Button(image=pygame.image.load("assets/Rectangle_1.png"), pos=(Width/3, Height/2), 
                                text_input="Min", font=get_font(40), base_color="#000000", hovering_color="#4B3305")

        Max_BUTTON = Button(image=pygame.image.load("assets/Rectangle_1.png"), pos=(2 *Width/3, Height/2), 
                                text_input="Max", font=get_font(40), base_color="#000000", hovering_color="#4B3305")

        window.blit(MENU_TEXT, MENU_RECT)
        
        for button in [Min_BUTTON, Max_BUTTON]:
                button.changeColor(PLAY_MOUSE_POS)
                button.update(window)
        
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if Min_BUTTON.checkForInput(PLAY_MOUSE_POS):
                            Display_NegaMaxAlphaBetaPruning(-1)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if Max_BUTTON.checkForInput(PLAY_MOUSE_POS):
                            Display_NegaMaxAlphaBetaPruning(1)

        pygame.display.update()

def Display_MiniMax(player):
    loop = True
    while loop :
        window.fill(BG_Color)
        Draw_Tree(Tree)

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("Min-Max", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(Width/2, 100))
        window.blit(MENU_TEXT, MENU_RECT)

        MinMax(Tree, player)
        loop = False
    loop = True
    while loop:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BUTTON = Button(image=pygame.image.load("assets/rectangle_5.png"), pos=(100,100), 
                            text_input="Return", font=get_font(20), base_color="#000000", hovering_color="#4B3305")

        for button in [PLAY_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(window)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    select()
        pygame.display.update()

def Display_NegaMax(player):
    loop = True
    while loop :
        window.fill(BG_Color)
        Draw_Tree(Tree)

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("NegaMax", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(Width/2, 100))
        window.blit(MENU_TEXT, MENU_RECT)

        NegaMax(Tree, player)
        loop = False
    loop = True
    while loop:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BUTTON = Button(image=pygame.image.load("assets/rectangle_5.png"), pos=(100,100), 
                            text_input="Return", font=get_font(20), base_color="#000000", hovering_color="#4B3305")


        for button in [PLAY_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(window)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    select()
        pygame.display.update()

def Display_NegaMaxAlphaBetaPruning(player):
    loop = True
    while loop :
        window.fill(BG_Color)
        Draw_Tree(Tree)
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("NegaMax Alpha-Beta Pruning", True, "#00CCCC")
        MENU_RECT = MENU_TEXT.get_rect(center=(Width/2, 100))
        window.blit(MENU_TEXT, MENU_RECT)

        NegaMaxAlphaBetaPruning(Tree, player)
        loop = False
    loop = True
    while loop:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BUTTON = Button(image=pygame.image.load("assets/rectangle_5.png"), pos=(100,100), 
                            text_input="Return", font=get_font(20), base_color="#000000", hovering_color="#4B3305")

        for button in [PLAY_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(window)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    select()
        pygame.display.update()
   
select()

