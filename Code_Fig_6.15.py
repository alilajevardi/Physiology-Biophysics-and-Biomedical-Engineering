
import numpy as np
import matplotlib.pyplot as plt



#function HHCLAMP2  does the analytic solution of the voltage clamped axon



# evenly sampled time at 50ms intervals
t = np.arange(0., 7., 0.05)

# The membrane patch is held at specified voltage (Vm) of
v = +30.0 #mV



# The n-type subunits
a1 = 0.01 * (-50-v) / (np.exp((-50 - v) / 10) - 1)
b1 = 0.125 * np.exp((-v - 60) / 80)

#The m-type subunits
a2 = 0.1 * (-35 - v)/(np.exp((-35 - v) / 10) - 1)
b2 = 4 * np.exp((-v - 60) / 18)

#The h-type subunits
a3 = 0.07 * np.exp((-v - 60)/ 20)
b3 = 1 / (np.exp((-30 - v) / 10) + 1)


n_inf = a1 / (a1 + b1)
m_inf = a2 / (a2 + b2)
h_inf = a3 / (a3 + b3)
n0 = 0.3
m0 = 0.05
h0 = 0.6


n = n_inf - (n_inf - n0) * np.exp(-t * a1 / n_inf)
m = m_inf - (m_inf - m0) * np.exp(-t * a2 / m_inf)
h = h_inf - (h_inf - h0) * np.exp(-t * a3 / h_inf)

y1 = 120.* m**3 * h * (v - 55) / 1000
y2 = 36. * n**4 * (v + 72) / 1000
y3 = y1 + y2


#simple plot
plt.plot(t, y1, 'r', t, y2, 'b', t, y3, 'g');



# plot includes lables
plt.suptitle('Total current, ${}$ and ${}$ for ${}$ = +30 mV'.format('I_{Na}', 'I_{K}', 'V_{m}'))
plt.xlabel('Time (ms)')
plt.ylabel('I (mA)')
plt.plot(t, y1, 'r', t, y2, 'b', t, y3, 'g')
plt.show()

