from pandas import Series
from matplotlib import pyplot
from pandas import DataFrame
from pandas import concat
from statsmodels.tsa.ar_model import AR
from sklearn.metrics import mean_squared_error
from pandas.tools.plotting import autocorrelation_plot
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.arima_model import ARIMA

# prepare situation
# series = Series.from_csv('daily-minimum-temperatures-in-me.csv', header=0)
series = Series.from_csv('wc98_workload_hour.csv', header=0)
#summary statistics
print series.describe()
# autocorrelation_plot(series)
# pyplot.show()
# split dataset
X = series.values
X = X.astype('float32')
train_size = int(len(X) * 0.80)
train, test = X[1:train_size], X[train_size:]
# train autoregression
model = ARIMA(train, order=(1,0,2))
model_fit = model.fit(disp=0)
print len(model_fit.params)
# make predictions
predictions = model_fit.predict(start=len(train), end=len(train)+len(test)-1, dynamic=False)
# for i in range(len(predictions)):
# 	print('predicted=%f, expected=%f' % (predictions[i], test[i]))
error = mean_squared_error(test, predictions)
print('Test MSE: %.3f' % error)
# plot results
# pyplot.plot(train)
series.hist()
# pyplot.plot([None for i in train] + [x for x in test])
# pyplot.plot([None for i in train] + [x for x in predictions], color='red')
pyplot.show()