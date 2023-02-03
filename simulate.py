# from turtle import back
# import time
# import numpy as numpy
# import random
# import constants as c



#
# 
# 
# 

# targetAnglesFrontLeg = numpy.zeros(5000)
# targetAnglesBackLeg = numpy.zeros(5000)

# # targetAngles = numpy.sin(numpy.linspace(0, 2*numpy.pi, num=1000)) * numpy.pi/4

# # 

# for i in range(5000):
#     targetAnglesFrontLeg[i] = c.FRONTLEGAMPLITUDE * numpy.sin(c.FRONTLEGFREQUENCY * i + c.FRONTLEGPHASEOFFSET)
#     targetAnglesBackLeg[i] = c.BACKLEGAMPLITUDE * numpy.sin(c.BACKLEGFREQUENCY * i + c.BACKLEGPHASEOFFSET)

# # with open('data/targetAnglesData.npy', 'wb') as f:
# #     numpy.save(f, targetAngles)

# # exit()
# for i in range(5000):
#     p.stepSimulation()
#     pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b"Torso_BackLeg", controlMode = p.POSITION_CONTROL, targetPosition = targetAnglesFrontLeg[i], maxForce = 50)
#     pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b"Torso_FrontLeg", controlMode = p.POSITION_CONTROL, targetPosition = targetAnglesBackLeg[i], maxForce = 50)
#     time.sleep(0.0001)

# # with open('data/backLegData.npy', 'wb') as f:
# #     numpy.save(f, backLegSensorValues)
# # with open('data/frontLegData.npy', 'wb') as f:
# #     numpy.save(f, frontLegSensorValues)



from simulation import SIMULATION


simulation = SIMULATION()

simulation.Run()