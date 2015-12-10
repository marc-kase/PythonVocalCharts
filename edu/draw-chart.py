import csv
import os
from os.path import normpath, join, dirname
import matplotlib.pyplot as plt
import numpy

source = 'source.csv'
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

t = numpy.arange(0., 32768, 4.)

# plt.plot(y)
plt.plot(t, y)
plt.show()
plt.savefig(target)
