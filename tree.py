import pygame

import grid
class Tree:

    def __init__(self,tilegrid:grid.Grid,ppcell:int,SCREEN:pygame.surface.Surface,starting_position) -> None:
        self.tilegrid:grid.Grid = tilegrid
        self.ppcell = ppcell # Pixels per cell
        self.SCREEN = SCREEN
        self.cell_list:list[cell.Cell] = []
        # Initialise first cell
        self.createCell(starting_position,1)
    
    def createCell(self,position:list[int],genome):
        """ Attempts to create a new cell, calls to this should be only made on tree creation and by active cells"""
        # Check if position available
        if not self.tilegrid.checkIfOccupied(position):
        # Check if enough resources

        # Add to position
            self.cell_list.append(cell.Cell(self,[0,255,0],position))
            self.tilegrid.placeOnTile(position,self.cell_list[-1])


    def update(self):
        for cell in self.cell_list:
            pygame.draw.rect(self.SCREEN,cell.colour,pygame.rect.Rect(cell.position[0]*self.ppcell,cell.position[1]*self.ppcell,self.ppcell,self.ppcell))

import cell