import numpy as np
from matplotlib import pyplot as plt
n=np.arange(0,500,2)
F=250
Fs=10000
f=F/Fs
r1=0.5*np.cos(2*np.pi*n*f+np.pi/2)
r2=2*np.cos(2*np.pi*n*f+np.pi/2)
s=r1+r2
plt.subplot(3,1,1);plt.stem(n,s)
r3=0.5*np.cos(2*np.pi*n*(500/10000)+np.pi/2)
r4=0.5*np.cos(2*np.pi*n*(250/10000)+np.pi/2)
s1=r3+r4
plt.subplot(3,1,2);plt.stem(n,s1)
r5=0.5*np.cos(2*np.pi*n*(250/10000)+np.pi/4)
r6=0.5*np.cos(2*np.pi*n*(250/10000)+np.pi/2)
s2=r5+r6
plt.subplot(3,1,3);plt.stem(n,s2);plt.show();
