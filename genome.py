import cell
import random
class Genome:
    
    def __init__(self) -> None:
        """Genome class holds information about the genome of a tree, which is a set of instructions that tells a tree how to grow.\n
        Each genome holds a number of chromosomes. Each chromosome holds the blueprint for a cell, telling it what type of cell it is, and what kind of cell to build each direction to it, 
        with the 0th chromosome always being the null cell and 1 being the root cell (though can be created later)."""
        self.genome={0:[None,0,0,0,0],
                     1:[cell.Cell,5,0,0,0],
                     2:[cell.Cell,1,3,0,3],
                     3:[cell.Cell,0,2,0,2],
                     4:[cell.Cell,1,0,0,0],

                     5:[cell.Cell,6,0,0,0],
                     6:[cell.Cell,0,7,0,0],
                     7:[cell.Seed,0,0,0,0]}
    
    def getChromosomeForCell(self,index):
        value = self.genome[index]
        
        return value[1:]
    
    def mutateChromosome(self)->None:
        genomesize = len(self.genome) # Get size of genome
        mutatedgenome = self.genome[random.randint(1,genomesize-1)] # Choose which genome to mutate, can't be the none gene
        if mutatedgenome[0] == cell.Cell: # Don't mutate seed
            changed_branch = random.randint(1,4) # Choose a direction to mutate
            mutatedgenome[changed_branch] = random.randint(1,genomesize-1)