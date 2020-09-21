import numpy as np
import matplotlib.pyplot as plt


# time = 20 second in 40 steps
t = np.linspace(0., 20, 40)



# Initial values
L = 20.
w = 500.
Qb = 150.
Qd = 500.
b0 = 100.


alpha = 0.05*(1/Qb - 1/Qd)
Z = np.exp(-alpha*w*L)/Qd - 1/Qb
b = b0*(np.exp(-alpha*w*L)/Qd - np.exp(-alpha*w*t)/Qb)/Z
d = b0*(np.exp(-alpha*w*L)/Qd - np.exp(-alpha*w*t)/Qd)/Z


plt.plot(t, b, 'r', t, d, 'b')
plt.show()



beta = 0.05*((1/Qb) + (1/Qd));
d1 = b0*Qd*(1 - np.exp(-beta*w*t))/(Qb + Qd);
b1 = d1 + b0*np.exp(-beta*w*t);


plt.plot(t, b1, 'r', t, d1, 'b')
plt.show()



