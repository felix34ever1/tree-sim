import tree

class Cell:

    def __init__(self,tree:tree.Tree,colour:list[int],position:list[int]) -> None:
        """ Creates a cell, able to occupy a tile. Should be a held by a tree object which will manage how it interacts. The tile should hold its genome and colour."""
        self.tree = tree
        self.colour = colour
        self.position = position
        self.genome = [0,0,0,0] # Up, Left, Down, Right, holding what cell it would make
        self.active = True # Describes if it is trying to make more cells or not

    def getColour(self):
        return self.colour

