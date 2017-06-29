# import statsmodels.api as sm
# import statsmodels.formula.api as smf 
# import statsmodels.graphics.api as smg 
# import patsy
# import matplotlib.pyplot as plt 
# from matplotlib import pyplot
# import numpy as np 
# import pandas as pd 
# from scipy import stats 
# dataset = sm.datasets.get_rdataset("discoveries")
# print dataset.data
# df = dataset.data.set_index("time")
# print df.head(10).T
# fig, ax = plt.subplots(1,1,figsize=(16,4))
# df.plot(kind='bar', ax=ax)

# model = smf.poisson("discoveries ~ 1", data = df)
# result = model.fit()
# print result.summary()
# print 'result.params: ' , result.params
# lmbda = np.exp(result.params)
# print lmbda
# X = stats.poisson(lmbda)
# # print X
# plt.show()


# dataset = pd.read_csv("wc98_workload_hour.csv", header=None)
# df = pd.DataFrame(dataset)
# print df
# # print df.head(10).T
# # print df
# df =df.set_index("timestamp")
# fig, ax = plt.subplots(1,1,figsize=(16,4))
# df.plot(kind='bar', ax=ax)
# model = smf.poisson("count ~ 1",data = df)
# result = model.fit()
# print result.summary()
# plt.show()
from statsmodels.tsa.ar_model import AR
from sklearn.metrics import mean_squared_error
from pandas.tools.plotting import autocorrelation_plot
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import Series
from pandas import read_csv
from pandas import DataFrame

series = read_csv('wc98_workload_hour.csv', header=0, parse_dates=[0], index_col=0, squeeze=True)
print len(series)
size = 12
# size = 22
lenTest = int(len(series)/size)
print lenTest
arlamda=[]
for i in range(lenTest):
	# series[0: size]
	test = series[i*size+1: (i+1)*size]
	df = DataFrame(test)
	print df
	model = smf.poisson("count ~ 1", data=df)
	result = model.fit(method='nm', maxiter=5000, maxfun=5000)
	# print(result.summary())
	# print 'abc'
	print result.params
	lmbda = np.exp(result.params)
	arlamda.append(lmbda)
	print lmbda
print arlamda
fig, ax = plt.subplots(1, 1)
train_size = int(len(arlamda) * 0.95)
train, test = arlamda[1:train_size], arlamda[train_size:]
model1 = AR(train)
model_fit1 = model1.fit()
print('Lag: %s' % model_fit1.k_ar)
print('Coefficients: %s' % model_fit1.params)
print len(model_fit1.params)
# make predictions
predictions = model_fit1.predict(start=len(train), end=len(train)+len(test)-1, dynamic=False)
# df1 = DataFrame(arlamda)
error = mean_squared_error(test, predictions)

print('Test MSE: %.3f' % error)
plt.plot(train)
plt.plot([None for i in train] + [x for x in test])
plt.plot([None for i in train] + [x for x in predictions], color='red')
plt.show()
# df.plot(kind='bar', ax=ax)
# plt.show()