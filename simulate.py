from simulation import SIMULATION
import sys

directOrGui = sys.argv[1]
solutionId = sys.argv[2]

simulation = SIMULATION(directOrGui, solutionId)

simulation.Run() 

simulation.Get_Fitness()