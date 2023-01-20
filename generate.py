import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

for j in range(5):
    for k in range(5):
        for i in range(10, 0, -1):
            pyrosim.Send_Cube(name="Box", pos=[k,j,(10 - i + 0.5)] , size=[i / 10, i / 10, i / 10])


pyrosim.End()

