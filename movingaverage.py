import numpy as np
from matplotlib import pyplot as plt
M=int(input("enter order of the M.A"))
n=np.arange(0,500,2)
y=10*np.random.rand(100)
z=np.zeros(len(y))
for n in range(0,len(y)):
	s=0
	for k in range(0,M):
		if n-k>=0:
			s=s+y[n-k]
	z[n]=s/M
print(y)
print(z)
plt.subplot(211)
plt.stem(y)
plt.subplot(212)
plt.stem(z)
plt.show()




