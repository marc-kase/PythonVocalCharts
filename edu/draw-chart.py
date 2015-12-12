import csv
import os
from os.path import normpath, join, dirname
import matplotlib.pyplot as plt
import numpy

source = 'source.csv'
data = 'source.csv'
data0 = 'data0.csv'
data1 = 'data.csv'
data2 = 'data2.csv'
appdir = dirname(os.getcwd())
source = normpath(join(appdir, 'data/' + data0))
target = normpath(join(appdir, 'data/example01.png'))

y = []
## if data new-line-separated
with open(source) as my_file:
    y = my_file.readlines()

## if data comma-separated
# with open(source) as f:
#     r = csv.reader(f, delimiter=",")
#     for row in r:
#         y = row

print(len(y))
freq = 16384.

t = freq / (len(y))
if t == 0: t = 1

x = numpy.arange(0., freq, t)
# print(len(x))

# plt.plot(y)
plt.plot(x, y)
plt.show()
plt.savefig(target)
