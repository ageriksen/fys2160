"""
program to plot PV isotherms. 
Should scale P(V, T, N) and to do that, see
schroeder where he derives van der Waals gas model.
"""

def P(V, T):
    return N*k*T/(V - N*b) - a*N**2*(1/V)
