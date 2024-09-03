import pygame

import grid

import tree

CELLS = [64,32] # Map Size
PPCELL = 20 # Pixels per cell
CELLSDISPLAYED = CELLS # Screen size
pygame.init()

SCREEN = pygame.display.set_mode((CELLSDISPLAYED[0]*PPCELL,CELLSDISPLAYED[1]*PPCELL),0,0,0,1) # Created display window, with VSYNC

gameGrid = grid.Grid(SCREEN,CELLS)

tree_list:list[tree.Tree] = []
tree_list.append(tree.Tree(tree_list,gameGrid,PPCELL,SCREEN,(15,31),None))

# GAME FLAGS
GAME_RUNNING = True
SHOW_GRID = False
PAUSED = False

# GAME CLOCKS
clock = pygame.time.Clock()
gametime = 200
gametimer = 200
turn = 0

# GAME LOOP
while GAME_RUNNING:
    # EVENTS
    for event in pygame.event.get():
        # QUIT
        if event.type == pygame.QUIT:
            GAME_RUNNING = False
        # KEYS
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                SHOW_GRID = not SHOW_GRID
            if event.key == pygame.K_p:
                PAUSED = not PAUSED
            if event.key == pygame.K_SPACE and PAUSED:
                if turn==3:
                    pass
                for _tree in tree_list:
                    _tree.update()
                turn+=1
                

    SCREEN.fill((0,0,0))
    if SHOW_GRID:
        for i in range(CELLSDISPLAYED[0]):
            pygame.draw.line(SCREEN,(255,255,255),(i*PPCELL,0),(i*PPCELL,CELLS[1]*PPCELL))
            for j in range(CELLSDISPLAYED[1]):
                pygame.draw.line(SCREEN,(255,255,255),(0,j*PPCELL),(CELLS[0]*PPCELL,j*PPCELL))
    
    if not PAUSED:
        gametimer-=clock.tick()
        if gametimer<=0:
            for _tree in tree_list:
                _tree.update()
            gametimer = gametime
            turn+=1

    for _tree in tree_list:
        _tree.updatescreen()

    pygame.display.flip()