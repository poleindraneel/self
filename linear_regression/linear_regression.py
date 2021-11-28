import numpy as np
import matplotlib.pyplot  as plot
import pandas as pa
from scipy import stats

pd = pa.read_csv("regression.csv")
features = pd["age"]
labels = pd["speed"]

# r - relationship
slope, intercept, r, p, std_err = stats.linregress(features, labels)

def lineFunc(x):
  return slope * x + intercept

lineY = list(map(lineFunc, features))
print(lineY)

plot.scatter(features,labels)
plot.plot(features,lineY)
plot.show()

speedY = lineFunc(6)
print(speedY)

# Bad data
# x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
# y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]
