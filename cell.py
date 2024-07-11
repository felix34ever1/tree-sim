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

    def update(self):
        """ On update, cell attempts to propogate by executing its genome and then it stops being active."""
        for i in range(4):
            if self.genome[i]!=0: # Checks that its not trying to make nothing
                if i == 0: # Up
                    self.tree.createCell([self.position[0],self.position[1]-1],self.genome[i])
                elif i == 1: # Right
                    self.tree.createCell([self.position[0]+1,self.position[1]],self.genome[i])
                elif i == 2: # Down
                    self.tree.createCell([self.position[0],self.position[1]+1],self.genome[i])
                elif i == 3: # Left
                    self.tree.createCell([self.position[0]-1,self.position[1]],self.genome[i])
        self.tree.active_to_remove_cell_list.append(self)