
from pandas import Series
from pandas import DataFrame
from pandas import concat
from matplotlib import pyplot
series = Series.from_csv('daily-minimum-temperatures-in-me.csv', header=0)
print series.head()
# dataframe = concat([values.shift(1), values], axis=1)
# series.plot()
# pyplot.show()
