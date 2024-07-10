import pygame

import grid
class Tree:

    def __init__(self,tilegrid:grid.Grid,ppcell:int,SCREEN:pygame.surface.Surface,starting_position:list[int],newgenome) -> None:
        
        self.tilegrid:grid.Grid = tilegrid
        self.ppcell = ppcell # Pixels per cell
        self.SCREEN = SCREEN

        newgenome:genome.Genome = newgenome
        if newgenome == None:
            self.genome = genome.Genome()
        else:
            self.genome = newgenome
        self.genome:genome.Genome

        self.active_cell_list:list[cell.Cell] = [] # Holds cells that still try to create branches
        self.cell_list:list[cell.Cell] = []
        # Initialise first cell
        self.createCell(starting_position,1) # Creates a cell from the root chromosome
        
    
    def createCell(self,position:list[int],chromosome):
        """ Attempts to create a new cell, calls to this should be only made on tree creation and by active cells"""
        # Check if position available
        if self.tilegrid.checkIfInBounds(position):
            if not self.tilegrid.checkIfOccupied(position):
            # Check if enough resources

            # Add to position
                if self.genome.genome[chromosome][0] != None:
                    newcell:cell.Cell = self.genome.genome[chromosome][0](self,[0,255,0],position)
                    newcell.genome = self.genome.getChromosomeForCell(chromosome)
                    self.active_cell_list.append(newcell)
                    self.cell_list.append(newcell)
                    self.tilegrid.placeOnTile(position,self.cell_list[-1])


    def update(self):
        for cell in self.active_cell_list:
            cell.update()

    def updatescreen(self):
        # Updates all the cells where they are
        for cell in self.cell_list:
            pygame.draw.rect(self.SCREEN,cell.colour,pygame.rect.Rect(cell.position[0]*self.ppcell,cell.position[1]*self.ppcell,self.ppcell,self.ppcell))

import cell
import genome
