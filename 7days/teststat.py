# from pandas import Series
# from pandas import DataFrame
# from pandas import concat
# from matplotlib import pyplot
# series = Series.from_csv('daily-minimum-temperatures-in-me.csv', header=0)
# print series.head()
# # dataframe = concat([values.shift(1), values], axis=1)
# series.plot()
# pyplot.show()

from pandas import Series
from matplotlib import pyplot
from pandas.tools.plotting import lag_plot
series = Series.from_csv('wc98_workload_hour.csv', header=0)
lag_plot(series)
pyplot.show()