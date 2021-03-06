import numpy as np
from matplotlib import pyplot as plt
n=np.arange(1,500,2)
n1=np.arange(1,500,2)
n2=np.arange(1,500,2)
F1=250;
F2=250;
fs=10000;
f1=F1/fs;
f2=F2/fs;
s=2*np.cos(2*np.pi*f1*n+np.pi/2)
s1=1*np.cos(2*np.pi*f2*n+np.pi/2)
plt.subplot(5,1,1);
plt.stem(n,s)
plt.subplot(5,1,2);
plt.stem(n,s1);
s2=s+s1;
plt.subplot(5,1,3);
plt.stem(n,s2);
s3=2*np.cos(2*np.pi*(250/10000)*n1+np.pi/2)
s4=2*np.cos(2*np.pi*(500/10000)*n1+np.pi/2)
s5=s3+s4;
plt.subplot(5,1,4);
plt.stem(n1,s5);
s6=2*np.cos(2*np.pi*(250/10000)*n2+np.pi/4)
s7=2*np.cos(2*np.pi*(200/10000)*n2+np.pi/2)
s8=s6+s7;
plt.subplot(5,1,5);
plt.stem(n2,s8);plt.show();
