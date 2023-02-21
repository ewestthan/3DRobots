
import pybullet as p
import pybullet_data
from world import WORLD
from robot import ROBOT
import time

class SIMULATION:
    def __init__(self, directOrGui):
        if directOrGui == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)

        self.world = WORLD()
        self.robot = ROBOT()

    def __del__(self):
        p.disconnect()

    def Run(self):
        for i in range(1000):
            
            p.stepSimulation()

            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act()

            time.sleep(0.0001)

    def Get_Fitness(self):
        self.robot.Get_Fitness()



