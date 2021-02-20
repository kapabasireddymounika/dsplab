import numpy as np
from matplotlib import pyplot as plt
w=np.arange(-1*np.pi,np.pi,0.01*np.pi)
m=np.arange(0,500)
x=np.cos(2*np.pi*(250/10000)*m)
X=[]
for i in range(0,len(w)):
	s=0
	for n in range(0,len(x)):
		s=s+x[n]*np.exp(-1*1j*w[i]*n)
	X.append(s)
plt.subplot(211)
plt.plot(w,np.abs(X))
plt.subplot(212)
plt.plot(w,np.angle(X))
plt.show()
