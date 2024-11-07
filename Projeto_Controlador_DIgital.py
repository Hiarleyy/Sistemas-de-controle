#%%
import control as ct
import matplotlib.pyplot as plt
import numpy as np
#%%
K = 1.2
tau = 0.1
num = K
den = [tau, 1]
G = ct.tf(num, den)
t, y= ct.step_response(G)
print(G)
#%%
plt.figure(figsize= (6,3))
plt.plot(t, y)
plt.grid()
plt.show()
#%%
ts = 5*tau
Ts = ts/15
Gz = ct.c2d(G, Ts, 'zoh')
print(Gz)
print(ts)
#%%
td, yd = ct.step_response(Gz, T=3)
plt.figure(figsize= (6,3))
plt.stem(td, yd, '.r')
plt.plot(td, yd, 'b')
plt.grid()
plt.show()

#%%
ct.pzmap(Gz)

#%%
kp = 5.5
Hz = ct.feedback(ct.series(kp, Gz), 1)
ct.rlocus(Gz)
ct.pzmap(Hz)

#%%
td1, yd1 = ct.step_response(Hz, T=3)
plt.figure(figsize= (6,3))
plt.stem(td1, yd1, '.r')
plt.grid()
plt.show()
#%%
zc = 15
C1 = ct.tf([1, zc], [1, 0])
kp = 2
l = ct.series(C1, G)
Hs = ct.feedback(ct.series(kp, l), 1)
ct.rlocus(ct.series(C1, G))
print(Hs)
#%%
Cs = ct.series(kp, C1)
Cs
#%%
Cz = ct.c2d(Cs, Ts, 'bilinear')
Cz 
#%%
Hz = ct.feedback(ct.series(Cz,Gz), 1)
tc, yc = ct.step_response(Hs, T=0.8)
td, yd = ct.step_response(Hz, T=0.8)
plt.figure(figsize= (6,3))
plt.plot(tc, yc)
plt.stem(td, yd, '.g')
plt.grid()
plt.show()