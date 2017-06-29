import statsmodels.api as sm
import statsmodels.formula.api as smf 
import statsmodels.graphics.api as smg 
import patsy
import matplotlib.pyplot as plt 
from matplotlib import pyplot
import numpy as np 
import pandas as pd 
from scipy import stats 

# N =100
# x1 = np.random.randn(N)  #Taoj mang random 100 phan tu
# x2 = np.random.randn(N)
# print len(x1)
# data = pd.DataFrame({"x1": x1, "x2":x2})
# data["y"] = 1+ 2*x1+3*x2 + 4*x1*x2 + 0.5*np.random.randn(N)
# model = smf.ols("y~ x1+x2+x1*x2", data)
# result = model.fit()
# print result.params
# fig,ax = plt.subplots(figsize=(8,4))
# smg.qqplot(result.resid, ax=ax)
# # smg.qqline(ax=ax)
# # smg.show()
# # result.resid.plot(style='k.')
# plt.show()

dataset = sm.datasets.get_rdataset("Icecream", "Ecdat")
print dataset.title
print dataset.data.info()
print dataset.data.temp.unique()
model = smf.ols("cons~ -1+ price + temp", data = dataset.data)
result = model.fit()
fig, (ax1, ax2) = plt.subplots(1,2,figsize=(20,4))
smg.plot_fit(result, 0 , ax = ax1)
smg.plot_fit(result, 1 , ax = ax2)
plt.show()