import pygame

CELLS = [30,30] # Map Size
PPCELL = 20 # Pixels per cell
CELLSDISPLAYED = CELLS # Screen size
pygame.init()

SCREEN = pygame.display.set_mode((CELLSDISPLAYED[0]*PPCELL,CELLSDISPLAYED[1]*PPCELL),0,0,0,1) # Created display window, with VSYNC



# GAME FLAGS
GAME_RUNNING = True
SHOW_GRID = False

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

    SCREEN.fill((0,0,0))
    if SHOW_GRID:
        for i in range(CELLSDISPLAYED[0]):
            pygame.draw.line(SCREEN,(255,255,255),(i*PPCELL,0),(i*PPCELL,CELLS[1]*PPCELL))
            for j in range(CELLSDISPLAYED[1]):
                pygame.draw.line(SCREEN,(255,255,255),(0,j*PPCELL),(CELLS[0]*PPCELL,j*PPCELL))
    
    pygame.display.flip()