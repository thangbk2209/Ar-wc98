# from pandas import Series
# from matplotlib import pyplot
# from statsmodels.tsa.ar_model import AR
# from sklearn.metrics import mean_squared_error
# series = Series.from_csv('wc98_workload_min.csv', header=0)
# # split dataset
# X = series.values
# train_size = int(len(X) * 0.66)
# train, test = X[1:train_size], X[train_size:]
# print X
# print train_size
# print train 
# print test
# # train autoregression
# model = AR(train)
# model_fit = model.fit()
# print('Lag: %s' % model_fit.k_ar)
# print('Coefficients: %s' % model_fit.params)
# # make predictions
# predictions = model_fit.predict(start=len(train), end=len(train)+len(test)-1, dynamic=False)
# for i in range(len(predictions)):
# 	print('predicted=%f, expected=%f' % (predictions[i], test[i]))
# error = mean_squared_error(test, predictions)
# print('Test MSE: %.3f' % error)
# # plot results
# pyplot.plot(train)
# pyplot.plot([None for i in train] + [x for x in test])
# pyplot.plot([None for i in train] + [x for x in predictions])
# pyplot.show()
# from sklearn.utils.validation import check_arrays
import numpy as np 
from pandas import Series
from matplotlib import pyplot
from pandas import DataFrame
from pandas import concat
from statsmodels.tsa.ar_model import AR
from sklearn.metrics import mean_squared_error
from pandas.tools.plotting import autocorrelation_plot
from statsmodels.graphics.tsaplots import plot_acf
from pandas.tools.plotting import lag_plot
from pandas.tools.plotting import autocorrelation_plot
def mean_absolute_percentage_error(y_true, y_pred): 
    # y_true, y_pred = check_arrays(y_true, y_pred)

    ## Note: does not handle mix 1d representation
    #if _is_1d(y_true): 
    #    y_true, y_pred = _check_1d_array(y_true, y_pred)

    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100
# series = Series.from_csv('daily-minimum-temperatures-in-me.csv', header=0)
series = Series.from_csv('wc98_workload_hour.csv', header=0)
# split dataset
X = series.values
train_size = int(len(X) * 0.95)
train, test = X[1:train_size], X[train_size:]
# autocorrelation_plot(series)
# plot_acf(series, lags=31)
# train autoregression
model = AR(train)
model_fit = model.fit()
print('Lag: %s' % model_fit.k_ar)
print('Coefficients: %s' % model_fit.params)
print len(model_fit.params)
# make predictions
predictions = model_fit.predict(start=len(train), end=len(train)+len(test)-1, dynamic=False)
for i in range(len(predictions)):
	print('predicted=%f, expected=%f' % (predictions[i], test[i]))
error = mean_squared_error(test, predictions)
error1 = mean_absolute_percentage_error(test, predictions)

print('Test MSE: %.3f' % error)
print('Test MAPE: %.3f' % error1)
# plot results
pyplot.plot(train)
pyplot.plot([None for i in train] + [x for x in test])
pyplot.plot([None for i in train] + [x for x in predictions], color='red')
pyplot.show()