from scipy import stats
from scipy import optimize
import numpy as np 
# from matplotlib import pyplot as plt 
import matplotlib.pyplot as plt
import seaborn as sns
print "lol"
sns.set(style="whitegrid")
fig, axes = plt.subplots(1, 3, figsize=(12, 3))
axes[0].hist(np.random.rand(10000))
# axes[0].plot(np.random.rand(10000))
axes[0].set_title("rand")
axes[1].hist(np.random.randn(10000))
axes[1].set_title("randn")
axes[2].hist(np.random.randint(low=1, high=10, size=10000), bins=9, align='left')
axes[2].set_title("randint(low=1, high=10)")
plt.show()