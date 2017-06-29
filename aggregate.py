import numpy as np 
data = np.random.normal(size = (5,10,15))
print data
mean = np.mean(data) #Tinh trung binh tat ca cac phan tu
print 'mean = ' , mean
print data.mean()
print "data.sum(axis=0).shape = " , data.sum(axis=0).shape
