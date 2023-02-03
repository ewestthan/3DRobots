import numpy as numpy
import matplotlib.pyplot as matplot
import constants as c
# backLegSensorValues = numpy.load('data/backLegData.npy')
# frontLegSensorValues = numpy.load('data/frontLegData.npy')

# matplot.plot(backLegSensorValues, linewidth=4)
# matplot.plot(frontLegSensorValues)
# matplot.legend(["Back Leg", "Front Leg"])
# matplot.show()
FrontLegmotorValues = numpy.zeros(1000)
BackLegMotorValues = numpy.zeros(1000)

for i in range(1000):
    FrontLegmotorValues[i] = c.AMPLITUDE * numpy.sin(c.FREQUENCY * (i + c.PHASEOFFSET))
    BackLegMotorValues[i] = c.AMPLITUDE * numpy.sin(c.FREQUENCY * (i + c.PHASEOFFSET))


matplot.plot(BackLegMotorValues, linewidth = 4)
matplot.plot(FrontLegmotorValues)
matplot.xlabel('Steps')
matplot.ylabel('Values in radians')
matplot.show()