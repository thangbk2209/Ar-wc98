# Load birth data
from pandas import Series
from matplotlib import pyplot
from pandas.tools.plotting import lag_plot
from pandas.tools.plotting import autocorrelation_plot
series = Series.from_csv('daily-minimum-temperatures-in-me.csv', header = 0)
# autocorrelation_plot(series)
series.plot()
pyplot.show()

# Load birth data using read_csv
# from pandas import read_csv
# series = read_csv('daily-births.csv', header=0, parse_dates=[0], index_col=0, squeeze=True)
# print(type(series))
# print(series.head())


