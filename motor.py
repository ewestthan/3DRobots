
import constants as c
import pyrosim.pyrosim as pyrosim
import pybullet as p
import numpy

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.motorValues = numpy.zeros(1000)
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.AMPLITUDE
        self.frequency = c.FREQUENCY
        self.offset = c.PHASEOFFSET
        print(self.jointName)
        if self.jointName == b"Torso_BackLeg":
            
            for i in range(1000):
                self.motorValues[i] = self.amplitude * numpy.sin(self.frequency * (i + self.offset))
        else:
            for i in range(1000):
                self.motorValues[i] = self.amplitude * numpy.sin((self.frequency / 2) * (i + self.offset))
    
    def Set_Value(self, robotId, t):
        pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = self.jointName, controlMode = p.POSITION_CONTROL, targetPosition = self.motorValues[t], maxForce = 50)
