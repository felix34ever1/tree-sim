
import tree

class Cell:

    def __init__(self,tree,colour:list[int],position:list[int]) -> None:
        """ Creates a cell, able to occupy a tile. Should be a held by a tree object which will manage how it interacts. The tile should hold its genome and colour."""
        self.tree = tree
        self.colour = colour
        self.position = position
        self.genome = [0,0,0,0] # Up, Left, Down, Right, holding what cell it would make
        self.active = True # Describes if it is trying to make more cells or not

    def update(self)->None:
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

class Seed(Cell):

    def __init__(self, tree: tree.Tree, colour: list[int], position: list[int]) -> None:
        """Creates a seed, a type of cell that retains the genetic information of the tree, and if the tree dies, it will fall to the ground in hopes of replanting."""
        super().__init__(tree, (255,245,245), position)
        self.genome:genome.Genome = tree.genome
        self.active = False

    def update(self):
        # The seed should only be active when it has just transferred to a new tree.
        if self.active:
            if self.tree.tilegrid.checkIfInBounds([self.position[0],self.position[1]+1]): # if has reached the ground:
                self.tree.moveCell(self,[self.position[0],self.position[1]+1])
            else:
                # Otherwise delete itself and create a root cell at its location
                self.tree.plantSelf(self.position)
            



import genome