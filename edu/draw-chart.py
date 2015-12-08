import csv
import os
from os.path import normpath, join, dirname

import matplotlib.pyplot as plt

data1 = 'data.csv'
data2 = 'data2.csv'
appdir = dirname(os.getcwd())
source = normpath(join(appdir, 'data/' + data2))
target = normpath(join(appdir, 'data/example01.png'))

y = []
# if data new-line-separated
with open(source) as my_file:
    y = my_file.readlines()

# if data comma-separated
# with open(source) as f:
#     r = csv.reader(f, delimiter=",")
#     for row in r:
#         y = row

plt.plot(y)
plt.show()
plt.savefig(target)
