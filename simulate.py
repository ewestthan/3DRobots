from turtle import back
import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy as numpy
import random

frontLegAmplitude = numpy.pi/4
frontLegFrequency = 5
frontLegPhaseOffset = 0
backLegAmplitude = numpy.pi/4
backLegFrequency = 3
backLegPhaseOffset = 0

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())


p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(5000)
frontLegSensorValues = numpy.zeros(5000)
targetAnglesFrontLeg = numpy.zeros(5000)
targetAnglesBackLeg = numpy.zeros(5000)

# targetAngles = numpy.sin(numpy.linspace(0, 2*numpy.pi, num=1000)) * numpy.pi/4

# 

for i in range(5000):
    targetAnglesFrontLeg[i] = frontLegAmplitude * numpy.sin(frontLegFrequency * i + frontLegPhaseOffset)
    targetAnglesBackLeg[i] = backLegAmplitude * numpy.sin(backLegFrequency * i + backLegPhaseOffset)

# with open('data/targetAnglesData.npy', 'wb') as f:
#     numpy.save(f, targetAngles)

# exit()
for i in range(5000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b"Torso_BackLeg", controlMode = p.POSITION_CONTROL, targetPosition = targetAnglesFrontLeg[i], maxForce = 50)
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b"Torso_FrontLeg", controlMode = p.POSITION_CONTROL, targetPosition = targetAnglesBackLeg[i], maxForce = 50)
    time.sleep(0.0001)

# with open('data/backLegData.npy', 'wb') as f:
#     numpy.save(f, backLegSensorValues)
# with open('data/frontLegData.npy', 'wb') as f:
#     numpy.save(f, frontLegSensorValues)



p.disconnect()

