import math
import numpy as np
import matplotlib.pyplot as plt

# test
SA = 150
mag = 300
avg_intensity = 210
temp = 87
rh = 86
wind = 8

totalEval = avg_intensity + ((avg_intensity/255) * (mag)) + ((mag/(360*240*255))*SA)
totalEval += (mag/(360*240*255)) * SA * (temp+(100-rh)+wind)
print(totalEval)

# this risk evaluation only applies to one "bubble"
# num_ATRs should be stored in an outside variable as with the the intensity variable
def risk_calculation(radius, intensity, temp, rh, wind):
    SA = math.pi*2*radius
    mag = math.pi*math.pow(radius, 2)
    totalEval = intensity + ((intensity/255) * (mag)) + ((mag/(360*240*255))*SA)
    totalEval += (mag/(360*240*255)) * SA * (temp+(100-rh)+wind)

    # sigmoid to improve time-complexity
    # condenses to a value between 0 and 100
    output = 100/(1 + np.exp(-0.005*totalEval+4))


# sigmoid graph for reference
x = np.linspace(0, 1600, 100)
z = 100/(1 + np.exp(-0.005*x+4))

plt.plot(x, z)
plt.xlabel("x")
plt.ylabel("Sigmoid(X)")

plt.show()


