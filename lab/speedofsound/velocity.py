import numpy as np
from scipy import stats

def fit(x, y):
    slope = stats.linregress(x, y)[0]
    std_err = stats.linregress(x, y)[4]
    return slope, std_err

def vel(slope, slope_err):
    velocity = slope*2*L
    error = velocity*np.sqrt( (slope_err/slope)**2 + (dL/L)**2 )
    return velocity, error


#length of Kundt's pipe and standard error of length
L = 1.243
dL = 0.0015

# measured harmonies, Argon Ar, Hz
y_Ar = [180, 269, 388, 522, 652, 779, 907, 1036, 1166, 1296, 1426, 1554, 1684, 1814, 1943, 2072, 2202, 2332]
x_Ar = np.arange(2, 20)

a, da  = fit(x_Ar, y_Ar) # slope and standard error of fit
c, dc = vel(a, da) # speed of sound and standard error for Argon

print(
        "slope a_Ar= ", a, 
        "std. error d_Ar = ", da)
print("vel c_Ar = ",  c )
print( "error for velocity dc_Ar = ", dc )

# measured harmonies, carbon dioxide CO2, Hz
y_CO2 = [105, 232, 332, 445, 554, 662, 771, 879, 990, 1100, 1210, 1320, 1429, 1540, 1649, 1761, 1869, 1980, 2091]
x_CO2 = np.arange(2, len(y_CO2)+2)


a, da  = fit(x_CO2, y_CO2) # slope and standard error of fit
c, dc = vel(a, da) # speed of sound and standard error for CO2

print(
        "slope a_CO2= ", a, 
        "std. error da_CO2 = ", da)
print("vel c_CO2 = ",  c )
print( "error for velocity dc_CO2 = ", dc )

""""
run example:
> python3 velocity.py
slope a_Ar=  128.41073271413833 std. error d_Ar =  0.4803556681204771
vel c_Ar =  319.22908152734794
error for velocity dc_Ar =  1.2547637074074742
slope a_CO2=  109.78245614035087 std. error da_CO2 =  0.13592345984151977
vel c_CO2 =  272.9191859649123
error for velocity dc_CO2 =  0.47185799292011504
