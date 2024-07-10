import pygame
from tile import Tile

# Grid class, holds the tiles of the world, and in turn the cells on those tiles.
class Grid:

    def __init__(self,SCREEN:pygame.surface.Surface,gridsize:list[int]) -> None:
        """ Creates a Grid object, able to hold all tiles in the game and to create the starting tile configuration. The main way to interact with tiles."""
        self.gridsize = gridsize
        self.tiles:list[list[Tile]] = [] # 2D array holding all the tiles.
        self.generateTiles()


    def generateTiles(self):
        """Generates empty tiles according to size of grid"""
        for i in range(self.gridsize[0]):
            self.tiles.append([])
            for j in range(self.gridsize[1]):
                self.tiles[i].append(Tile((i,j)))

    def placeOnTile(self,gridpos:list[int],newcell):
        """Places a new cell onto a tile, overriding it"""
        self.tiles[gridpos[0]][gridpos[1]].occupy(newcell)
    
    def checkIfOccupied(self,gridpos:list[int]):
        """Checks if tile is already occupied"""
        return self.tiles[gridpos[0]][gridpos[1]].isOccupied()
