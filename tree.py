import pygame

import grid
class Tree:

    def __init__(self,tree_list:list,tilegrid:grid.Grid,ppcell:int,SCREEN:pygame.surface.Surface,starting_position:list[int],newgenome) -> None:
        
        self.tree_list:list[Tree] = tree_list
        self.tilegrid:grid.Grid = tilegrid
        self.ppcell = ppcell # Pixels per cell
        self.SCREEN = SCREEN

        newgenome:genome.Genome = newgenome
        if newgenome == None:
            self.genome = genome.Genome()
        else:
            self.genome = newgenome
        self.genome:genome.Genome = self.genome

        self.active_cell_list:list[cell.Cell] = [] # Holds cells that still try to create branches
        self.active_to_remove_cell_list:list[cell.Cell] = [] # Holds cells that need to be removed from active cell list
        self.next_turn_cell_list:list[cell.Cell] = [] # Holds cells that will next turn attempt to create branches
        self.cell_list:list[cell.Cell] = []
        # Initialise first cell
        self.createCell(starting_position,1) # Creates a cell from the root chromosome
        self.turns_alive = 0
        self.lifespan = 10

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
                    if newcell is not cell.Seed:
                        self.next_turn_cell_list.append(newcell)
                    self.cell_list.append(newcell)
                    self.tilegrid.placeOnTile(position,self.cell_list[-1])

    def moveCell(self,_cell,position:list[int]):
        """Attempts to move a cell one tile orthogonally."""
        _cell:cell.Cell = _cell
        # Checks if position is available:
        if self.tilegrid.checkIfInBounds(position):
            if not self.tilegrid.checkIfOccupied(position):
                # Check for resources

                # Move cell over - 1 - remove from current tile, 2 - add to new tile
                self.tilegrid.tiles[_cell.position[0]][_cell.position[1]].occupy(None)
                self.tilegrid.tiles[position[0]][position[1]].occupy(_cell)
                _cell.position = position

    def plantSelf(self,position:list[int]):
        """Attempts to delete the seed and plant the root cell in its place, only done once when a seed hits the ground."""
        self.tilegrid.tiles[position[0]][position[1]].occupy(None)
        self.cell_list.clear()
        self.active_cell_list.clear()
        self.createCell(position,1)

    def update(self):
        """Updates the tree by allowing all active cells to execute their updates and then correctly moving cells to active or inactive states, or activates the death sequence"""
        if self.turns_alive<self.lifespan:
            for _cell in self.active_cell_list:
                _cell.update()
            for _cell in self.active_to_remove_cell_list: # removes all active cells
                self.active_cell_list.remove(_cell)
            for _ in range(len(self.next_turn_cell_list)): # activates cells that need to be active for next turn
                self.active_cell_list.append(self.next_turn_cell_list.pop(0))
            self.active_to_remove_cell_list = []

            self.turns_alive+=1
        else: # Tree dies of old age
            
            # Check all cells, if they are seeds, create a new tree for them, then delete all cell references
            for _cell in self.cell_list: # BUG if a seed is frozen mid air for long enough it will make itself part of a new tree and mutate again
                if isinstance(_cell,cell.Seed): 
                    newtree = Tree(self.tree_list,self.tilegrid,self.ppcell,self.SCREEN,_cell.position,self.genome)
                    # Run a mutation algorithm on new genome
                    newtree.genome.mutateChromosome()
                    # Replace seed's tree, and activates it
                    _cell.tree = newtree
                    newtree.cell_list.append(_cell)
                    newtree.active_cell_list.append(_cell)
                    self.tree_list.append(newtree)
                    _cell.active=True
                else:
                    self.tilegrid.placeOnTile(_cell.position,None)
                # remove self at end and clears all cells
            self.cell_list.clear() # needs to be cleared after, because if removed before, it will mess with the for loop
            self.tree_list.remove(self)

    def updatescreen(self):
        """Draws the cells to the world"""
        # Updates all the cells where they are
        for cell in self.cell_list:
            pygame.draw.rect(self.SCREEN,cell.colour,pygame.rect.Rect(cell.position[0]*self.ppcell,cell.position[1]*self.ppcell,self.ppcell,self.ppcell))

import cell
import genome
