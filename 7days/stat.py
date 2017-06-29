import statsmodels.api as sm 
import pandas
from patsy import dmatrices
df = sm.datasets.get_rdataset("guerry", "HistData").data 
vars = ['Department', 'Lottery' , 'Literacy' , 'Wealth' , 'Region']
df = df[vars]
print df[-5:]