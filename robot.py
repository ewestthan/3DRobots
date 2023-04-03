from turtle import position
import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os

class ROBOT:
    def __init__(self, solutionId):
        self.robotId = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK("brain" + str(solutionId) + ".nndf")
        self.motors = {}
        self.sensors = {}
        self.solutionId = solutionId
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        os.system("rm brain" + str(solutionId) + ".nndf")

    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        for i in self.sensors.values():
             i.Get_Value(t)

    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName.encode('UTF-8')].Set_Value(self.robotId, desiredAngle)

    def Think(self):
        self.nn.Update()
        # self.nn.Print()

    def Get_Fitness(self):
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robot)
        basePosition = basePositionAndOrientation[0]
        xPosition = basePosition[0]

        f = open("tmp" + str(self.solutionId) + ".txt", "w")
        f.write(str(xPosition))
        f.close()
        os.system("mv tmp" + str(self.solutionId) + ".txt fitness" + str(self.solutionId) + ".txt")