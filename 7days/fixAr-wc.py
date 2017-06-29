import numpy as np
from pandas import Series
from matplotlib import pyplot
from pandas import DataFrame
from pandas import concat
from statsmodels.tsa.ar_model import AR
from sklearn.metrics import mean_squared_error
from pandas.tools.plotting import autocorrelation_plot
from statsmodels.graphics.tsaplots import plot_acf
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
print 'X: ', len(X)
train_size = int(len(X) * 0.8)
train, test = X[1:train_size], X[train_size:]
# train autoregression
print len(train)
model = AR(train)
model_fit = model.fit()
# model_fit = model.fit(10,ic='bic')
print('Lag: %s' % model_fit.k_ar)
# lag= round(12*(len(train)/100.)**(1/4.))
# print 'Gia tri lag theo cach tinh', lag
print('Coefficients: %s' % model_fit.params)
print len(model_fit.params), len(test)
window = model_fit.k_ar
print 'window: ', window
coef = model_fit.params
# make predictions
history = train[len(train)-window:]
history = [history[i] for i in range(len(history))]
predictions = list()
for t in range(len(test)):
	length = len(history)
	lag = [history[i] for i in range(length-window,length)]
	yhat = coef[0]
	for d in range(window):
		yhat += coef[d+1] * lag[window-d-1]
	obs = test[t]
	# obs = yhat
	predictions.append(yhat)
	history.append(obs)
	# print('predicted=%f, expected=%f' % (yhat, obs))
error = mean_squared_error(test, predictions)
error1 = mean_absolute_percentage_error(test, predictions)

print('Test MSE: %.3f' % error)
print('Test MAPE: %.3f' % error1)


# plot results
pyplot.plot(train)
pyplot.plot([None for i in train] + [x for x in test])
pyplot.plot([None for i in train] + [x for x in predictions], color='red')
pyplot.show()