import matplotlib.pyplot as plt
import numpy as np

def MBdist(T, v):
    """ Maxwell Boltzmann distribution of velocities dependent on temperature. """
    return (v**2/T**(3.0/2.0))*np.exp( -B*(v**2/T) )

# m = 4.67e-26 kg mass of nitrogen gas N_2
# k = 1.38064 J/K
B = (4.67/(2*1.38))*1e-3 # factor beta m/2k
print('the exponential factor beta = B = m/2k is: {}' .format(B))
"""
runexample:
>python3 E32MBdist.py
the exponential factor beta = B = m/2k is: 0.0016920289855072465
"""

v = np.linspace(0, 2e3, 1e6)
DvT1 = MBdist(300, v)
DvT2 = MBdist(600, v) 

s = 0
normT1 = DvT1/np.sum(DvT1)
for i in range(len(v)): 
    s+= normT1[i]
    if v[i] > 300:
        break

print("percentage of particles with velocities of 300 m/s and less for temperature T = 300 K: ", s)


plt.figure()
plt.plot(v, DvT1, label=r'T = 300 K')
plt.plot(v, DvT2, label=r'T = 600 K')
plt.xlabel('v')
plt.ylabel(r"$4\sqrt{ m / 2\pi^{1/3}\, k } \cdot D(v)$")
plt.legend()
plt.show()

"""
runexample:
> python3 E32MBdist.py
the exponential factor beta = B = m/2k is: 0.0016920289855072465
percentage of particles with velocities of 300 m/s and less for temperature T = 300 K:  0.20243226483074644
"""
