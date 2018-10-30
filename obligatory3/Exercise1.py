"""
program to plot PV isotherms. 
Should scale P(V, T, N) and to do that, see
schroeder where he derives van der Waals gas model.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def scaledPressure(v, t):
    """ Scaled formula for pressure in a van der Waals gas """
    return ( 8/( 3*v -1 ) )*t - 3/v**2

def fit(x, y):
    std_err = stats.linregress(x, y)[4]
    slope = stats.linregress(x, y)[0]
    return slope, std_err

Pc = 33.6 # atm of pressure
Vc = 0.089 # l/mol 
Tc = 126 # K critical temperature
T = np.array((77, 100, 110, 115, 120, 125)) # K temperature isotherms
Weights = np.array( (0.36, 0.545, 0.67, 0.818, 0.9682) ) # weights for lines of equal Maxwell area
t = T/Tc # scaled temperature

v = np.linspace(0, 10, 1e6)

#plt.figure()
#for i in range(1, len(t)):
#    plt.plot(v, scaledPressure(v, t[i]), label='T={}'.format(t[i]*Tc))
##    plt.plot(v, Weights[i-1]*np.ones(len(v)))
#plt.legend()
#plt.xlabel(r'v')
#plt.ylabel(r'$\rho$')
#plt.grid()
#plt.ylim(-2,2)
#plt.show()

################### Exercise 1.5, plot Vl - Vg as a function of temperature T ##################
""" find the intersection with T = 0 """

Vl = np.array( (0.107, 0.096, 0.003, 0.092, 0.089) )
Vg = np.array( (0.400, 0.262, 0.205, 0.153, 0.108) )
print(
        'T[1::]: ', T[1::], '\n',
        'Vl - Vg: ', Vl - Vg )
#slope, error = fit(T[1::], Vl - Vg)
linfit = stats.linregress(T[1::], Vl - Vg)
slope, intercept = linfit[0], linfit[1]
print(
        'With a linear fit of slope: ', slope, '\n',
        'and intercept: ', intercept)


plt.figure()
plt.plot(T[1::], Vl-Vg, 'o', label='volume difference pts')
#plt.plot(T[1::], slope*T[1::], label=r'linear fit, $\epsilon$ {error}')
plt.plot(T[1::], slope*T[1::]+intercept) 
plt.xlabel('T')
plt.ylabel(r'$V_l - V_g$')
plt.legend()
plt.show()

"""
runexample:
> python3 Exercise1.py
T[1::]:  [100 110 115 120 125] 
 Vl - Vg:  [-0.293 -0.166 -0.202 -0.061 -0.019]
With a linear fit of slope:  0.010781081081081082 
 and intercept:  -1.3772432432432433
"""
