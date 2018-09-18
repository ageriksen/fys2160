"""
generate 10**4 microstates of N=60 paramagnets with spin 
s = +1 or -1 for spin up or down respectively.
P(s) = 0.5. Therfore, make random int 0 or 1 for spin ups, while
total spin S = 2N_up - N
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

#declaring variables
M = 10**4; N = 60
#initiating array
Nu = np.zeros(M)
#number of spin-up states
for i in range(M):
    Nu[i] = np.sum(np.random.randint(2, size=N))
#Total spin, N_dwn = N - N_up
S = 2*Nu - N
#extracting expectation value and standard deviation
(mu, sigma) = norm.fit(S)
#histogram and plots
n, bins, patches = plt.hist(S, N-1, density=True)
G = norm.pdf(bins, mu, sigma)
l = plt.plot(bins, G)
plt.xlabel('total sum of spins')
plt.ylabel('number of microstates')
plt.title('distribution of total energy for N=60 paramgnet system')
plt.show()
