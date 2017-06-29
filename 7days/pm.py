import statsmodels.api as sm
import statsmodels.formula.api as smf 
import statsmodels.graphics.api as smg 
import patsy
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
from scipy import stats 

y = np.array([1,2,3,4,5])
x1 = np.array([6,7,8,9,10])
x2 = np.array([11,12,13,14,15])
X = np.vstack([np.ones(5),x1,x2,x1*x2]).T
# print X
data = {"y": y, "x1":x1, "x2":x2}
y,X = patsy.dmatrices("y~ 1+x1+x2+x1*x2",data)
print y
print type(X)
np.array(X)
df_data = pd.DataFrame(data)
print df_data
y,X = patsy.dmatrices("y~ 1+x1+x2+x1*x2",df_data,return_type="dataframe")
print y
print X
model = sm.OLS(y,X) # Mo hinh tong binh phuong sai so la nho nhat
result = model.fit()
print result.params

model1 = smf.ols("y~ 1+x1+x2+x1*x2",df_data)
print model1.fit().params

