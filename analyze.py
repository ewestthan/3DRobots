import numpy as numpy
import matplotlib.pyplot as matplot

backLegSensorValues = numpy.load('data/backLegData.npy')
frontLegSensorValues = numpy.load('data/frontLegData.npy')

matplot.plot(backLegSensorValues, linewidth=4)
matplot.plot(frontLegSensorValues)
matplot.legend(["Back Leg", "Front Leg"])
matplot.show()

