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

size = int(len(series) * 0.02)
test = series[len(series)-size:len(series)]
df = DataFrame(test)
print df
fig, ax = plt.subplots(1, 1)
model = smf.poisson("count ~ 1", data=df)
result = model.fit(method='nm', maxiter=5000, maxfun=5000)
print(result.summary())
lmbda = np.exp(result.params)
print lmbda
df.plot(kind='bar', ax=ax)
plt.show()