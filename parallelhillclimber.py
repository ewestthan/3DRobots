from solution import SOLUTION
import constants
import copy
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(constants.POPULATIONSIZE):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1

    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(constants.NUMBEROFGENERATIONS):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Spawn(self):
        self.children = {}
        for k in self.parents:
            self.children[k] = copy.deepcopy(self.parents[k])
            self.children[k].Set_ID(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1

    def Mutate(self):
        for k in self.children:
            self.children[k].Mutate()
        
    def Select(self):
        for i in self.parents:
            if self.parents[i].fitness > self.children[i].fitness:
                self.parents[i] = self.children[i]

    def Print(self):
        print("\n")
        for i in self.parents:
            print(self.parents[i].fitness, self.children[i].fitness)
        print("\n")

    def Show_Best(self):
        best = 100
        bestIndex = 0 
        for x in range(len(self.parents)) :
            if self. parents[x].fitness < best:
                bestIndex = x
                best = self.parents[x].fitness
        self.parents[bestIndex].Start_Simulation("GUI")
        print(best)
    
    def Evaluate(self, solutions):
        directOrGUI = "DIRECT"
        for k in solutions:
            solutions[k].Start_Simulation(directOrGUI)

        for k in solutions:
            solutions[k].Wait_For_Simulation_To_End()