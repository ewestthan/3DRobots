from solution import SOLUTION
import constants
import copy

class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()

    def Evolve(self):

        self.parent.Evaluate("DIRECT")

        for currentGeneration in range(constants.NUMBEROFGENERATIONS):
            self.Evolve_For_One_Generation(currentGeneration)

    def Evolve_For_One_Generation(self, gen):
        self.Spawn()
        self.Mutate()
        if(gen == 0):
            self.child.Evaluate("GUI")
        else:
            self.child.Evaluate("DIRECT")
        self.Print()
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()
        
    def Select(self):
        if self.parent.fitness < self.child.fitness:
            self.parent = self.child

    def Print(self):
        print(self.parent.fitness, self.child.fitness)

    def Show_Best(self):
        self.parent.Evaluate("GUI")