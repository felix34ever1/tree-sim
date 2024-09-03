import pygame


class Tile:

    def __init__(self,position:list[int]) -> None:
        """ Creates a tile that is able to hold a cell and its grid position."""
        self.position = position
        self.occupied:bool = False
        self.cell:object = None

    def occupy(self,newcell):
        """ Overrides the current cell with a new cell or empty."""
        self.cell = newcell
        if self.cell == None:
            self.occupied = False
        else:
            self.occupied = True
    
    def isOccupied(self):
        return self.occupied
    
