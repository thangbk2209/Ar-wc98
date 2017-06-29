import numpy as np
a= np.array([1,2,3,4]).reshape(2,2)
print a
c = np.array([2,3,4,5]).reshape(2,2)
print c
b = np.array([1,2,3,2,3,4,4,5,6]).reshape(3,3)
print b
print a*c
d=np.array([[3,4,5]])
e= d.shape # dua ra co cua ma tran
print e
zz = np.concatenate([d,d],axis=0)# axis =0 de them mot hang moi or axis=1 de them mot cot moi.
print zz
k = np.linspace(-1,1,11)
print k

def heaviside(x):
	return 1 if x>0 else 0
x = np.linspace(-5,5,11)
# print heaviside(x)  --> Loi
heaviside = np.vectorize(heaviside) # Su dung ham cho mang
print heaviside(x)