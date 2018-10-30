import matplotlib.pyplot as plt
import numpy as np

def MBdist(T, v, B):
    """ Maxwell Boltzmann distribution of velocities dependent on temperature. """
    return (v**2/T**(3.0/2.0))*np.exp( -B*(v**2/T) )

def normalize(distribution):
    return distribution/np.sum(distribution)

def probability(velTarget, dist, vel, direction):
    """ func estimates prob of velocity above or below a target. """
    normed = normalize(dist)
    print(np.sum(normed))
    integ = 0
    if direction > 0: 
        print( "finding probability above ", velTarget)
        for i in range(len(normed)):
            if vel[i] > velTarget:
                #print(normed[i])
                integ += normed[i]
    elif direction < 0:
        print( "finding probability below ", velTarget)
        for i in range(len(normed)):
            if vel[i] < velTarget:
                integ += normed[i]
    else:
        print("please supply a direction. everything up to, or everything over target (-1 / +1)?")
        return NaN
    return integ

# m = 4.67e-26 kg mass of nitrogen gas N_2
# k = 1.38064 J/K
B = (4.67/(2*1.38))*1e-3 # factor beta m/2k
print('the exponential factor beta = B = m/2k is: {}' .format(B))



############# exercise 3.2, plot of distributions for temperatures 300 and 600 K #######################

v = np.linspace(0, 2e3, 1e6)
DvT1 = MBdist(300, v, B)
DvT2 = MBdist(600, v, B) 

plt.figure()
plt.plot(v, DvT1, label=r'T = 300 K')
plt.plot(v, DvT2, label=r'T = 600 K')
plt.xlabel('v')
plt.ylabel(r"$4\sqrt{ m / 2\pi^{1/3}\, k } \cdot D(v)$")
plt.legend()
plt.show()

############ exercise 3.3 ratio of particles below a velocity of 300 m/s at temperature 300 K #########
s = probability(300, DvT1, v, -1)
print("percentage of particles with velocities of 300 m/s and less for temperature T = 300 K: ", s)

################# exercise 3.4 probability of velocity above 11 km/s with temperature 1kK ################
""" Here, we can use a simlar method as in 3.3, but now, we can sum up the posibility of being less than necessary.
    The probability we're looking for is then 1 - this probability. """
escapevelEarth = 11e3
T_1k = 1e3
v_1k = np.linspace(0, 15e3, 1e7)
DvT1k = MBdist(T_1k, v_1k, B)
P1kup = probability(escapevelEarth, DvT1k, v_1k, +1)
print("probability of reaching 11km/s speeds at temperature of 1k K: ", P1kup)

################ exercise 3.5 repeat for hyrdogen and Helium ################
MH = 0.071 # how many N2 masses there are in hydrogen gas
MHe = 2*MH # H masses in a He atom
BH = B*MH
BHe = B*MHe
DvT1kH = MBdist(T_1k, v_1k, BH)
DvT1kHe = MBdist(T_1k, v_1k, BHe)

ProbH = probability(escapevelEarth, DvT1kH, v_1k, +1)
ProbHe = probability(escapevelEarth, DvT1kHe, v_1k, +1)

print(" probability of escape velocity for H2 and He: \n", ProbH, '\n', ProbHe)

################ exercise 3.6 consider the moon! ##################
""" We're on the moon and have a bunch of N2 molecules. chances of reaching the stars? """
escapevelMoon = 2.4e3 # m/s
DvT1kMoon = MBdist(T_1k, v_1k, B)
probMOON = probability(escapevelMoon, DvT1kMoon, v_1k, +1)
print("probability of N2 molecules reaching escape velocity on the MOON \n", probMOON)

"""
Runexample:
> python3 Exercise3.py 
the exponential factor beta = B = m/2k is: 0.0016920289855072465
0.9999999999999998
finding probability below  300
percentage of particles with velocities of 300 m/s and less for temperature T = 300 K:  0.2024289896401181
1.000000000000001
finding probability above  11000.0
probability of reaching 11km/s speeds at temperature of 1k K:  1.966118913531021e-88
0.9999999999999982
finding probability above  11000.0
0.9999999999999978
finding probability above  11000.0
 probability of escape velocity for H2 and He: 
 2.1622828677256284e-06 
 1.4637954508031133e-12
1.000000000000001
finding probability above  2400.0
probability of N2 molecules reaching escape velocity on the MOON 
 0.00021625927936643762
"""
